try:
    import numpy as np
    numpy_installed = True
except ImportError:
    numpy_installed = False


class FloatRounder:
    """
    A structlog processor for rounding floats. Both as single numbers or in data structures like (nested) lists, dicts,
    or numpy arrays.

    Inspired by https://github.com/underyx/structlog-pretty/blob/master/structlog_pretty/processors.py
    """
    def __init__(self, digits=3, only_fields=None, not_fields=None, np_array_to_list=True):
        """
        Create a FloatRounder processor. That rounds floats to the given number of digits.

        :param digits: The number of digits to round to
        :param only_fields: An iterable specifying the fields to round (None = round all fields except not_fields)
        :param not_fields: An iterable specifying fields not to round
        :param np_array_to_list: Whether to cast np.array to list for nicer printing
        """
        self.digits = digits
        self.np_array_to_list = np_array_to_list
        try:
            self.only_fields = set(only_fields)
        except TypeError:
            self.only_fields = None
        try:
            self.not_fields = set(not_fields)
        except TypeError:
            self.not_fields = None

    def _round(self, value):
        """
        Round floats, unpack lists, convert np.arrays to lists

        :param value: The value/data structure to round
        :returns: The rounded value
        """
        # round floats
        if isinstance(value, float):
            return round(value, self.digits)
        # convert np.array to list
        if numpy_installed and self.np_array_to_list:
            if isinstance(value, np.ndarray):
                return self._round(list(value))
        # round values in lists recursively (to handle lists of lists)
        if isinstance(value, list):
            for idx, item in enumerate(value):
                value[idx] = self._round(item)
            return value
        # similarly, round values in dicts recursively
        if isinstance(value, dict):
            for k, v in value.items():
                value[k] = self._round(v)
            return value
        # return any other values as they are
        return value

    def __call__(self, _, __, event_dict):
        for key, value in event_dict.items():
            if self.only_fields is not None and key not in self.only_fields:
                continue
            if key in self.not_fields:
                continue
            if isinstance(value, bool):
                continue  # don't convert True to 1.0

            event_dict[key] = self._round(value)
        return event_dict

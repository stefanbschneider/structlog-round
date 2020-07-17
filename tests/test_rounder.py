import pytest
import numpy as np

import structlog_round


class TestFloatRounder:
    @pytest.mark.parametrize(['param', 'expected'], [
        (1/3, 0.333),
        (2/3, 0.667),
        ([1/3, 2/3], [0.333, 0.667]),
        ([[1/3], 2/3], [[0.333], 0.667]),
        ({'1': 1/3}, {'1': 0.333})
    ])
    def test_rounding_default(self, param, expected):
        """Test if individual floats and other data structures are rounded correctly to 3 digits."""
        rounder = structlog_round.FloatRounder()
        event_dict = rounder(None, None, {'param': param})
        assert event_dict == {'param': expected}

    @pytest.mark.parametrize(['param', 'expected', 'digits'], [
        (1/3, 0.33, 2),
        (2/3, 0.6667, 4),
        ([1/3, 2/3], [0.3, 0.7], 1),
        ([[1/3], 2/3], [[0.333], 0.667], 3),
        ({'1': 1/3}, {'1': 0.33}, 2)
    ])
    def test_rounding(self, param, expected, digits):
        """Test if individual floats and other data structures are rounded correctly to a custom number of digits."""
        rounder = structlog_round.FloatRounder(digits=digits)
        event_dict = rounder(None, None, {'param': param})
        assert event_dict == {'param': expected}

    @pytest.mark.parametrize(['p1', 'p2', 'e1', 'e2'], [
        (1/3, 2/3, 0.333, 2/3)
    ])
    def test_round_only_p1(self, p1, p2, e1, e2):
        # only_fields needs to be a list or set --> type error
        with pytest.raises(TypeError):
            rounder = structlog_round.FloatRounder(only_fields='p1')

        rounder = structlog_round.FloatRounder(only_fields=['p1'])
        event_dict = rounder(None, None, {'p1': p1, 'p2': p2})
        assert event_dict == {'p1': e1, 'p2': e2}

    @pytest.mark.parametrize(['p1', 'p2', 'e1', 'e2'], [
            (1/3, 2/3, 1/3, 0.667)
        ])
    def test_round_not_p1(self, p1, p2, e1, e2):
        # not_fields needs to be a list or set --> type error
        with pytest.raises(TypeError):
            rounder = structlog_round.FloatRounder(not_fields='p1')

        rounder = structlog_round.FloatRounder(not_fields=['p1'])
        event_dict = rounder(None, None, {'p1': p1, 'p2': p2})
        assert event_dict == {'p1': e1, 'p2': e2}

    def test_round_numpy(self):
        np_arr = np.array([1/3, 2/3])

        rounder = structlog_round.FloatRounder()
        event_dict = rounder(None, None, {'np': np_arr})
        assert event_dict == {'np': [0.333, 0.667]}

        rounder = structlog_round.FloatRounder(np_array_to_list=False)
        event_dict = rounder(None, None, {'np': np_arr})
        assert event_dict == {'np': np_arr}

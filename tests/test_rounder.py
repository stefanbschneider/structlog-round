import pytest

import structlog_round


class TestFloatRounder:
    @pytest.mark.parametrize(['param', 'expected'], [
        (1/3, 0.333),
        (2/3, 0.667),
        ([1/3, 2/3], [0.333, 0.667]),
        ([[1/3], 2/3], [[0.333], 0.667]),
        ({'1': 1/3}, {'1': 0.333})
    ])
    def test_rounding(self, param, expected):
        """Test if individual floats and other data structures are rounded correctly."""
        rounder = structlog_round.FloatRounder()
        event_dict = rounder(None, None, {'param': param})
        assert event_dict == {'param': expected}

    # TODO: test digit, only_fields, not_fields, numpy

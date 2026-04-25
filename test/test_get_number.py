import unittest
from unittest import mock

import cutie

from . import MockException


class TestCutieGetNumber(unittest.TestCase):
    @mock.patch("cutie.print", side_effect=MockException)
    def test_invalid_number(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print", side_effect=MockException)
    def test_not_allow_float(self, mock_print):
        raise NotImplementedError

    def test_allow_float_returns_float(self):
        raise NotImplementedError

    def test_not_allow_float_returns_int(self):
        raise NotImplementedError

    @mock.patch("cutie.print", side_effect=MockException)
    def test_min_value_float_too_low(self, mock_print):
        raise NotImplementedError

    def test_min_value_float_equal(self):
        raise NotImplementedError

    def test_min_value_float_greater(self):
        raise NotImplementedError

    @mock.patch("cutie.print", side_effect=MockException)
    def test_min_value_int_too_low(self, mock_print):
        raise NotImplementedError

    def test_min_value_int_equal(self):
        raise NotImplementedError

    def test_min_value_int_greater(self):
        raise NotImplementedError

    @mock.patch("cutie.print", side_effect=MockException)
    def test_max_value_float_too_high(self, mock_print):
        raise NotImplementedError

    def test_max_value_float_equal(self):
        raise NotImplementedError

    def test_max_value_float_smaller(self):
        raise NotImplementedError

    @mock.patch("cutie.print", side_effect=MockException)
    def test_max_value_int_too_high(self, mock_print):
        raise NotImplementedError

    def test_max_value_int_equal(self):
        raise NotImplementedError

    def test_max_value_int_smaller(self):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_print_finalize(self, mock_print):
        raise NotImplementedError

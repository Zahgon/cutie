import string
import unittest
from unittest import mock

import readchar

from . import InputContext, MockException, PrintCall, cutie

print_call = PrintCall(
    {
        "selectable": "\x1b[K\x1b[1m[ ]\x1b[0m ",
        "selected": "\x1b[K\x1b[1m[\x1b[32;1mx\x1b[0;1m]\x1b[0m ",
        "caption": "\x1b[K",
    }
)


class TestSelect(unittest.TestCase):
    @mock.patch("cutie.print", side_effect=MockException)
    def test_print_list_newlines(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_move_to_first_item(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_selected_index_set(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_non_selectable(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_custom_prefixes(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_ignore_unrecognized_key(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_up(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_up_skip_caption(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down_skip_caption(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_keyboard_interrupt_ctrl_c_no_input(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_keyboard_interrupt_ctrl_c_selected(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_keyboard_interrupt_ctrl_d_no_input(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_keyboard_interrupt_ctrl_d_selected(self, *m):
        raise NotImplementedError

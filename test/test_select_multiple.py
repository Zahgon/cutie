import string
import unittest
from unittest import mock

import readchar

from . import InputContext, MockException, PrintCall, cutie, yield_input

print_call = PrintCall(
    {
        "selectable": "\x1b[K\x1b[1m( )\x1b[0m ",
        "selected": "\x1b[K\x1b[1m(\x1b[32mx\x1b[0;1m)\x1b[0m ",
        "caption": "\x1b[K",
        "active": "\x1b[K\x1b[32;1m{ }\x1b[0m ",
        "active-selected": "\x1b[K\x1b[32;1m{x}\x1b[0m ",
        "confirm": ("\x1b[1m(( confirm ))\x1b[0m \x1b[K", {"end": "", "flush": True}),
        "confirm-active": (
            "\x1b[1;32m{{ confirm }}\x1b[0m \x1b[K",
            {"end": "", "flush": True},
        ),
        "no_confirm_line": ("\033[K", {"end": "", "flush": True}),
    }
)


PRINT_CALL_END = (("\r\x1b[K",), {"end": "", "flush": True})


class TestSelectMultiplePrint(unittest.TestCase):
    @mock.patch("cutie.print", side_effect=MockException)
    def test_list_newlines(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_move_to_first_item(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_caption_indices(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_selected(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_selected_and_ticked(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_options_deselected_unticked(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_deselected_confirm(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_selected_confirm(self, mock_print, *m):
        raise NotImplementedError

    @mock.patch("cutie.readchar.readkey", side_effect=MockException)
    @mock.patch("cutie.print")
    def test_print_show_confirm(self, mock_print, *m):
        raise NotImplementedError


class TestSelectMultipleMoveAndSelect(unittest.TestCase):
    @mock.patch("cutie.print")
    def test_move_up(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_up_skip_caption(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down_skip_caption(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_min_too_few(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_max_too_many(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_min_sufficient(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_deselect_on_min_sufficient(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_max_okay(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_min_too_few_hide_confirm(self, mock_print):
        """
        This should prompt the user with an error message
        """
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_select_max_too_many_show_confirm(self, mock_print):
        """
        This should prompt the user with an error message
        """
        raise NotImplementedError


class TestSelectMultipleMisc(unittest.TestCase):
    @mock.patch("cutie.print")
    def test_keyboard_interrupt(self, mock_print):
        raise NotImplementedError

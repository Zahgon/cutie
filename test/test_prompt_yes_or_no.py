import unittest
from unittest import mock

import readchar

from . import InputContext, MockException, PrintCall, cutie

print_call = PrintCall(
    {
        "selected": "\x1b[K\x1b[31m>\x1b[0m ",
        "selectable": "\x1b[K  ",
    }
)


class TestPromtYesOrNo(unittest.TestCase):

    default_yes_print_calls = [
        (tuple(),),
        (("\x1b[K\x1b[31m>\x1b[0m Yes",),),
        (("\x1b[K  No",),),
        (("\x1b[3A\r\x1b[Kfoo (Y/N) Yes",), {"end": "", "flush": True}),
        (("\x1b[K\n\x1b[K\n\x1b[K\n\x1b[3A",),),
    ]

    default_no_print_calls = [
        (tuple(),),
        (("\x1b[K  Yes",),),
        (("\x1b[K\x1b[31m>\x1b[0m No",),),
        (("\x1b[3A\r\x1b[Kfoo (Y/N) No",), {"end": "", "flush": True}),
        (("\x1b[K\n\x1b[K\n\x1b[K\n\x1b[3A",),),
    ]

    @mock.patch("cutie.print")
    def test_print_message(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_print_message_custom_prefixes(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_print_message_custom_yes_no_text(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_print_message_default_is_yes(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_up(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_up_over_boundary(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_move_down_over_boundary(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_backspace_delete_char(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_ctrl_c_abort(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_ctrl_c_abort_with_input(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_ctrl_d_abort(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_ctrl_d_abort_with_input(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_enter_confirm_default(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_enter_confirm_selection(self, *m):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_tab_select(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_write_keypress_to_terminal(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_write_keypress_to_terminal_resume_selection(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_evaluate_written_input_yes_ignorecase(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_evaluate_written_input_yes_case_sensitive(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_evaluate_written_input_no_ignorecase(self, mock_print):
        raise NotImplementedError

    @mock.patch("cutie.print")
    def test_evaluate_written_input_no_case_sensitive(self, mock_print):
        raise NotImplementedError

#! /usr/bin/env python3
"""
Commandline User Tools for Input Easification
"""

__version__ = "0.3.2"
__author__ = "Hans / Kamik423"
__license__ = "MIT"


import getpass
from typing import List, Optional

import readchar
from colorama import init

init()


class DefaultKeys:
    """List of default keybindings.

    Attributes:
        interrupt(List[str]): Keys that cause a keyboard interrupt.
        select(List[str]): Keys that trigger list element selection.
        confirm(List[str]): Keys that trigger list confirmation.
        delete(List[str]): Keys that trigger character deletion.
        down(List[str]): Keys that select the element below.
        up(List[str]): Keys that select the element above.
    """

    interrupt: List[str] = [readchar.key.CTRL_C, readchar.key.CTRL_D]
    select: List[str] = [readchar.key.SPACE]
    confirm: List[str] = [readchar.key.ENTER]
    delete: List[str] = [readchar.key.BACKSPACE]
    down: List[str] = [readchar.key.DOWN, "j"]
    up: List[str] = [readchar.key.UP, "k"]


def get_number(
    prompt: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    allow_float: bool = True,
) -> float:
    """Get a number from user input.
    If an invalid number is entered the user will be prompted again.

    Args:
        prompt (str): The prompt asking the user to input.
        min_value (float, optional): The [inclusive] minimum value.
        max_value (float, optional): The [inclusive] maximum value.
        allow_float (bool, optional): Allow floats or force integers.

    Returns:
        float: The number input by the user.
    """
    raise NotImplementedError


def secure_input(prompt: str) -> str:
    """Get secure input without showing it in the command line.

    Args:
        prompt (str): The prompt asking the user to input.

    Returns:
        str: The secure input.
    """
    raise NotImplementedError


def select(
    options: List[str],
    caption_indices: Optional[List[int]] = None,
    deselected_prefix: str = "\033[1m[ ]\033[0m ",
    selected_prefix: str = "\033[1m[\033[32;1mx\033[0;1m]\033[0m ",
    caption_prefix: str = "",
    selected_index: int = 0,
    confirm_on_select: bool = True,
) -> int:
    """Select an option from a list.

    Args:
        options (List[str]): The options to select from.
        caption_indices (List[int], optional): Non-selectable indices.
        deselected_prefix (str, optional): Prefix for deselected option ([ ]).
        selected_prefix (str, optional): Prefix for selected option ([x]).
        caption_prefix (str, optional): Prefix for captions ().
        selected_index (int, optional): The index to be selected at first.
        confirm_on_select (bool, optional): Select keys also confirm.

    Returns:
        int: The index that has been selected.
    """
    raise NotImplementedError


def select_multiple(
    options: List[str],
    caption_indices: Optional[List[int]] = None,
    deselected_unticked_prefix: str = "\033[1m( )\033[0m ",
    deselected_ticked_prefix: str = "\033[1m(\033[32mx\033[0;1m)\033[0m ",
    selected_unticked_prefix: str = "\033[32;1m{ }\033[0m ",
    selected_ticked_prefix: str = "\033[32;1m{x}\033[0m ",
    caption_prefix: str = "",
    ticked_indices: Optional[List[int]] = None,
    cursor_index: int = 0,
    minimal_count: int = 0,
    maximal_count: Optional[int] = None,
    hide_confirm: bool = True,
    deselected_confirm_label: str = "\033[1m(( confirm ))\033[0m",
    selected_confirm_label: str = "\033[1;32m{{ confirm }}\033[0m",
) -> List[int]:
    """Select multiple options from a list.

    Args:
        options (List[str]): The options to select from.
        caption_indices (List[int], optional): Non-selectable indices.
        deselected_unticked_prefix (str, optional): Prefix for lines that are
            not selected and not ticked (( )).
        deselected_ticked_prefix (str, optional): Prefix for lines that are
            not selected but ticked ((x)).
        selected_unticked_prefix (str, optional): Prefix for lines that are
            selected but not ticked ({ }).
        selected_ticked_prefix (str, optional): Prefix for lines that are
            selected and ticked ({x}).
        caption_prefix (str, optional): Prefix for captions ().
        ticked_indices (List[int], optional): Indices that are
            ticked initially.
        cursor_index (int, optional): The index the cursor starts at.
        minimal_count (int, optional): The minimal amount of lines
            that have to be ticked.
        maximal_count (int, optional): The maximal amount of lines
            that have to be ticked.
        hide_confirm (bool, optional): Hide the confirm button.
            This causes <ENTER> to confirm the entire selection and not just
            tick the line.
        deselected_confirm_label (str, optional): The confirm label
            if not selected ((( confirm ))).
        selected_confirm_label (str, optional): The confirm label
            if selected ({{ confirm }}).

    Returns:
        List[int]: The indices that have been selected
    """
    raise NotImplementedError


def prompt_yes_or_no(
    question: str,
    yes_text: str = "Yes",
    no_text: str = "No",
    has_to_match_case: bool = False,
    enter_empty_confirms: bool = True,
    default_is_yes: bool = False,
    deselected_prefix: str = "  ",
    selected_prefix: str = "\033[31m>\033[0m ",
    char_prompt: bool = True,
) -> Optional[bool]:
    """Prompt the user to input yes or no.

    Args:
        question (str): The prompt asking the user to input.
        yes_text (str, optional): The text corresponding to 'yes'.
        no_text (str, optional): The text corresponding to 'no'.
        has_to_match_case (bool, optional): Does the case have to match.
        enter_empty_confirms (bool, optional): Does enter on empty string work.
        default_is_yes (bool, optional): Is yes selected by default (no).
        deselected_prefix (str, optional): Prefix if something is deselected.
        selected_prefix (str, optional): Prefix if something is selected (> )
        char_prompt (bool, optional): Add a [Y/N] to the prompt.

    Returns:
        Optional[bool]: The bool what has been selected.
    """
    raise NotImplementedError

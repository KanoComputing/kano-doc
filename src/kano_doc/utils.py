# utils.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Utility functions used in this project.


ANSI_CODES = {
    'fg_colour_template': u'\u001b[38;5;{}m',
    'bg_colour_template': u'\u001b[48;5;{}m',
    'reset': u'\u001b[0m',
}

COLOURS = {
    'value': 44,
}


def colourise(text, fg_colour_id, bg_colour_id=None):
    """Style a string with ANSI colour IDs.

    Args:
        text (str): Message to apply the styling to
        fg_colour_id (int): A value 0 to 255 representing the ANSI colour
            to be used as the font colour
        bg_colour_id (int): A value 0 to 255 representing the ANSI colour
            to be used as the highlight colour

    Returns:
        str: The ``text`` argument wrapped in the desired ANSI codes
    """
    fg_colour = ANSI_CODES['fg_colour_template'].format(fg_colour_id)

    if bg_colour_id:
        bg_colour = ANSI_CODES['bg_colour_template'].format(bg_colour_id)
    else:
        bg_colour = ''

    return '{}{}{}{}'.format(bg_colour, fg_colour, text, ANSI_CODES['reset'])


def confirm(text):
    """Ask the user to confirm.

    A confirmation is valid when 'y' or 'yes' was given as raw input.

    Args:
        text (str): Message passed to ``raw_input`` asking user for input

    Returns:
        bool: Whether the user confirmed or not
    """
    response = raw_input(text)
    ok = False

    try:
        ok = response.lower() in ['y', 'yes']
    except:
        pass

    return ok

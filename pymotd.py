#!/usr/bin/python

r"""
A python Message of the Day script. Configure it through the parameters passed
to the get_motd function in the if __name__ == '__main__' section at the end of
the file, or, if you are so inclined, by importing this file and calling the
get_motd function yourself. 

In this default configuration, it prints a message similar to this:



I surely do hope that's a syntax error.
             -- Larry Wall in <199710011752.KAA21624@wall.org>

      /#\
     /###\
    /p^###\
   /##P^q##\
  /##(   )##\
 /###P   q#,^\  Linux TARDIS 4.10.9-1-ARCH 
/P^         ^q\  7 updates available 



The Arch ASCII image is not hardcoded, but is rather loaded from ~/.motd_image
(this can be changed). More messages can also be added and the fortune message
at the top can be swapped out for something else or removed entirely. 
"""

import os
from collections import defaultdict

from colorama import init, Fore, Style
from termcolor import colored
import sh


def get_motd(pre_message, image_path, messages, image_color=None):
    """
        Get the message of the day for the parameters given. This function is a
        generator that yields the message one line at a time.

        :param pre_message: The string to be shown above the image could be
        used, for example, for a fortune message.

        :param image_path: Path to a text file containing the ascii image to be
        shown on the left of the message.
        
        :param messages: The messages that will be printed next to the
        picture. It is a list of strings the will be printed next to the image,
        in the bottom left. So, for example, the list ['test1', 'test2'] would
        result in:
        *********
        *       *
        * image *
        *       * test1
        ********* test2

        :param image_color: The colorama Foreground color in which the image
        will be printed. If None is passed or the argument is left empty then
        no color is used.
    """

    if image_path is not None:
        with open(os.path.expanduser(image_path)) as image:
            image_lines = [line.rstrip() for line in image.readlines()]
    else: 
        # list of empty strings as long as the messages list.
        image_lines = ['' for _ in messages] 

    yield pre_message

    yield image_color
    for i, image_line in enumerate(image_lines):
        try:
            # yield image line in color, and message without the image color
            yield ''.join([
                image_line, 
                Style.RESET_ALL, 
                messages[i - len(image_lines)], 
                image_color
            ])
        except IndexError:
            yield image_line

    yield Style.RESET_ALL

if __name__ == '__main__':
    # This is an example configuration that can be modified or used as-is. The
    # commands are called through the sh module (amoffat.github.io/sh). 

    # 'fortune' messages - only short ones though -
    fortune = sh.fortune('-s')

    # 'uname' output, including kernel name (-s), hostname (-n) and kernel
    # version (-r)
    uname = sh.uname('-snr').rstrip()

    # number of pacman updates available, counted through the 'checkupdates'
    # script included with pacman. Note:
    # a) This (obviously) only works in distros using pacman and
    # b) The checkupdates script is kinda slow (3-6 seconds in my experience),
    #    so, if the script takes a long time to run, try disabling this part.
    repo_update_count = sh.wc(sh.checkupdates(), '-l').rstrip()

    # The path the ASCII image.
    image_path = '~/.motd_image'
    # The color in which the image will be printed. This can be any string, but
    # you will probably want to pass either one of the constants in
    # colorama.Fore, such as Fore.RED, or a color format string such as
    # '\033[92m' (for red). 
    image_color = Fore.BLUE

    # The messages that will be printed next to the ASCII image. See the messages
    # parameter in the docstring of the get_motd function for details.
    messages = [
        uname, 
        f'{colored(repo_update_count, attrs=["bold"])} updates available'
    ]

    for line in get_motd(fortune, image_path, messages, image_color):
        print(line)

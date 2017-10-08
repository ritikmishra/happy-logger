import inspect
from inspect import currentframe, getframeinfo
import traceback
from log import bcolors
from log.string_builder import build_string
import os


def info(text):
    """
    Print out an error
    
    :param text: The stuff to print out
    :type text: str
    :return: None
    """
    print(bcolors.NORMAL + build_string("INFO", text))


if __name__ == '__main__':
    info("test")

import inspect
from inspect import currentframe, getframeinfo
import traceback
from log import bcolors
from log.string_builder import build_string
import os


def err(text):
    """
    Print out an error
    
    :param text: The stuff to print out
    :type text: str
    :return: None
    """
    print(bcolors.FAIL + build_string("ERR", text))


if __name__ == '__main__':
    err("test")

import inspect
from inspect import currentframe, getframeinfo
import traceback
from log import bcolors
from log.string_builder import build_string
import os


def success(text):
    """
    Print out an error
    
    :param text: The stuff to print out
    :type text: str
    :return: None
    """
    print(bcolors.OKGREEN + build_string("SUC", text))


if __name__ == '__main__':
    success("test")

from log import bcolors
from log.string_builder import build_string


def err(text, *args, **kwargs):
    """
    Print out an error
    
    :param text: The stuff to print out
    :type text: str
    :return: None
    """
    print(bcolors.FAIL + build_string("ERR", text), *args, **kwargs)


if __name__ == '__main__':
    err("test")

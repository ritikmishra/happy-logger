from log import bcolors
from log.string_builder import build_string


def warn(text):
    """
    Print out an error
    
    :param text: The stuff to print out
    :type text: str
    :return: None
    """
    print(bcolors.WARNING + build_string("WARN", text))


if __name__ == '__main__':
    warn("test")

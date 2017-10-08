"""
Nice logger that prints with colors, uses timestamps, and lets you add your own functions

Functions:



"""

import log._error
import log._info
import log._success
import log._warning

err = log._error.err
warn = log._warning.warn
info = log._info.info
success = log._success.success

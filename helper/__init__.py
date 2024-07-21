import sys

if sys.platform == "win32":
    from helper import parser
else:
    from helper import parser, unix as platform
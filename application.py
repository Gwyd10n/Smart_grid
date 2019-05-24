#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

import sys
from helpers.clui import clui
from helpers.clui_test import clui_test


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        clui_test()
    else:
        clui()

#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert


import os
from helpers.CLUI import CLUI


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    CLUI(path)


if __name__ == "__main__":
    main()

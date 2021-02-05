#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Using __name__ and __main__

print("This is mod_1 name → " + __name__)


def main():
    return " from mod 1 function"
#    pass  # key word that helps bypass without an error

# Syntax:
# if __name__ == "__main__":


if __name__ == "__main__":  # checks whether code is run from current file
    main()

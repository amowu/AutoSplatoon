#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
#
# SPDX-FileCopyrightText: 2014-2022 Fredrik Ahlberg, Angus Gratton,
# Espressif Systems (Shanghai) CO LTD, other contributors as noted.
#
# SPDX-License-Identifier: GPL-2.0-or-later

# This executable script is a thin wrapper around the main functionality
# in the esptool Python package

# When updating this script, please also update espefuse.py and espsecure.py

import contextlib
import os
import sys

if os.name != "nt":
    # Linux/macOS: remove current script directory to avoid importing this file
    # as a module; we want to import the installed esptool module instead
    with contextlib.suppress(ValueError):
        if sys.path[0].endswith("/bin"):
            sys.path.pop(0)
        sys.path.remove(os.path.dirname(sys.executable))

    # Linux/macOS: delete imported module entry to force Python to load
    # the module from scratch; this enables importing esptool module in
    # other Python scripts
    with contextlib.suppress(KeyError):
        del sys.modules["esptool"]

import esptool

if __name__ == "__main__":
    esptool._main()

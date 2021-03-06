import logging
import sys


def get_verbosity():
    verbosity = 0
    for el in sys.argv:
        if not el.startswith("-v"):
            continue
        el = el.replace("-", "")
        is_verbosity = True
        for letter in el:
            if letter != "v":
                is_verbosity = False
        if is_verbosity:
            verbosity = len(el)
            break
    return verbosity


def getLogger(name):
    verbosity = get_verbosity()
    log_level = logging.ERROR
    if verbosity >= 2:
        log_level = logging.DEBUG
    elif verbosity >= 1:
        log_level = logging.INFO
    logging.basicConfig(
        format="%(levelname)7s: %(message)s",
        stream=sys.stdout,
        level=log_level,
    )
    return logging.getLogger(name)

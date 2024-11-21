import logging
from sys import exit

def setup_log(debug=False) -> None:
    logging.basicConfig(format=f"%(levelname)s - %(name)s -> %(message)s", force=True, level=logging.DEBUG if debug else logging.WARNING)

def info(msg:str) -> None:
    """ Performs a normal info log """
    logging.info(msg)

def warning(msg:str) -> None:
    """ Performs a warning log """
    logging.warning(msg)

def debug(msg:str) -> None:
    """ Performs a debug log """
    logging.debug(msg)

def error(msg:str, do_exit=True) -> None:
    """
    Performs an error log and exits the software if do_exit is set to true
    """
    logging.error(msg)

    if do_exit:
        exit(1)
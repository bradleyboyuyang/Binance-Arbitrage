'''
@Description: logger configuration
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

import time
import logging
import coloredlogs

def add_logger_filehandler(logger: logging.Logger, log_file: str, level: int = logging.DEBUG,
                           fmt: str = '%(asctime)s %(filename)s(%(lineno)d):%(funcName)s %(levelname)s %(message)s', datefmt: str = '%Y-%m-%d %H:%M:%S') -> bool:
    try:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
        logger.addHandler(fh)
    except Exception as e:
        logger.error(e)
        return False
    return True


def get_logger(log_name: str, log_level: int = logging.DEBUG, log_file: str = None, file_level: int = logging.DEBUG,
               fmt: str = '%(asctime)s %(filename)s(%(lineno)d):%(funcName)s %(levelname)s %(message)s', datefmt: str = '%Y-%m-%d %H:%M:%S') -> logging.Logger:
    """info, debug, warning, error, critical"""
    logger = logging.getLogger(log_name)

    if log_file is not None:
        if add_logger_filehandler(logger, log_file, level=file_level, fmt=fmt, datefmt=datefmt) is False:
            logger.warning(
                'add logger filehandler:{log_file} failed.'.format(log_file=log_file))
    coloredlogs.install(level=log_level, logger=logger,
                        fmt=fmt, datefmt=datefmt)

    return logger

def get_local_timezone() -> str:
    """get local time zone"""
    return time.strftime('%z')
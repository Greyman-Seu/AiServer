# @File  : utils.py
# @Date  :  2020/08/19
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

import time
import logging.config
from pathlib import Path
from app.tools import get_yaml_data


def mkdir_log(paths):
    for path in paths:
        if not path.exists():
            path.mkdir()


def get_logger(path_log, path_logging_yml, loggername, getLoggerFunc=logging.getLogger):
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    now = time.strftime("%Y-%m-%d-%H", time.localtime(time.time()))
    # now = "2020"

    log_config = get_yaml_data(path_logging_yml)
    level = log_config["loggers"][loggername]["level"]
    log_config["handlers"]["file_{}".format(log_config.get("type", "size"))]["filename"] = Path(
        str(path_log).replace(".log", f"_{now}-{level}.log"))

    logging.config.dictConfig(log_config)
    logger = getLoggerFunc(loggername)
    return logger, log_config

# @File  : logging_celery.py
# @Date  :  2020/08/19
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com


# %% -------------------------------------
"""
import *
"""
from celery.utils.log import get_task_logger

from app.conf.project_setting import path_log, path_logging_celery_yml
from app.core.logging_core.utils import mkdir_log, get_logger

# %% -------------------------------------
"""
配置logging参数（fix）
todo:error info分开
"""

path_relative_celery = path_log / "celery"
path_relative_fastapi = path_log / "fastapi"
mkdir_log([path_log, path_relative_fastapi,path_relative_celery])

# %% -------------------------------------
"""
设置celery log
"""
celery_logger, _ = get_logger(path_relative_celery / "celery.log", path_logging_celery_yml, "tasks", get_task_logger)

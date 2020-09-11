# @File  : celery_app.py
# @Date  :  2020/08/14
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

# %% -------------------
"""
import *
"""
import os
import platform
from pathlib import Path

from celery import Celery
from app.tools import get_yaml_data
from app.conf.project_setting import path_celery_yml, path_api_yml, project_name

if platform.system() == "Windows":
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# %% ----------------------
"""
yaml文件读取
"""
if ~os.path.isdir(path_celery_yml):
    path_celery_yml = Path(__file__).parents[1] / "conf" / path_celery_yml

celery_config = get_yaml_data(path_celery_yml)


if ~os.path.isdir(path_api_yml):
    path_api_yml = Path(__file__).parents[1] / "conf" / path_api_yml
api_config = get_yaml_data(path_api_yml)
# %% ----------------------
"""
配置redis参数
"""

# 获取tasks
tasks = []
for api_name, api_info in api_config.get("tasks", {}).items():
    if api_name is not None:
        tasks.append("app.api.hub.tasks." + api_info.get("path", api_name))


celery_app = Celery(
    project_name,
    broker=celery_config["redis"].get("broker_url", "redis://redis:6379/0"),
    backend=celery_config["redis"].get("backend_url", "redis://redis:6379/1"),
    include=tasks
)

# %% ----------------------
"""
配置celery参数
"""
celery_app.conf.update(**celery_config["celery"])





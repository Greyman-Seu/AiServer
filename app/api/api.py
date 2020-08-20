# @File  : api.py
# @Date  :  2020/08/14
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

# %% ---------------------
"""
import *
"""

import os
import importlib
from pathlib import Path

from fastapi import APIRouter

from app.tools import get_yaml_data, print_api_config
from app.conf.project_setting import path_api_yml

from app.core.logging_core.logging_fastapi import fastapi_logger
# %% ----------------------
"""
yaml文件读取
"""
if ~os.path.isdir(path_api_yml):
    path_api_yml = Path(__file__).parents[1] / "conf" / path_api_yml
api_config = get_yaml_data(path_api_yml)

# todo:加入logging中
fastapi_logger.info("\n"+str(print_api_config(api_config)))

# %% ------------------------
"""
动态加载库以及注册服务
"""

api_router = APIRouter()

for kind in ["services", "tasks"]:
    for api_name, api_info in api_config.get(kind, {}).items():
        if api_name != None:
            # 动态加载
            api_func = importlib.import_module(name="app.api.hub." + kind + "." + api_info.get("path", api_name))
            # 注册服务
            api_router.include_router(api_func.router, prefix="/" + api_info["prefix"], tags=[api_info["tags"]])

# %% -------------------
"""
单文件可debug
"""

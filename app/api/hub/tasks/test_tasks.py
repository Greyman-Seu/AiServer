# @File  : test_tasks.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

# %% -----------------------------
"""
import *
"""
from fastapi import APIRouter

from app.core.celery_app import celery_app as capp
from app.api.hub.tasks.base_tasks import base_api_tasks
from app.api.src.tasks.test_tasks import add as add_func
from app.schemas.tasks.test_tasks import TestTaskConfig

from app.core.logging_core.logging_celery import celery_logger

# %% -----------------------------
"""
celery app setting
"""

@capp.task
def add_capp(x, y):
    celery_logger.info("[*]test add_capp func")
    sum_x_y = add_func(x, y)
    return str(sum_x_y)   # 返回只接受字符串

# %% -----------------------------
"""
fastapi app setting
"""

router = APIRouter()
add = base_api_tasks(router, add_capp, TestTaskConfig, "求和提交任务成果")
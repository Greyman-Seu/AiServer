# @File  : logging_fastapi.py
# @Date  :  2020/08/19
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com


# @File  : logging_core.py
# @Date  :  2020/08/14
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

# %% -------------------------------------
"""
import *
"""
from app.conf.project_setting import path_log, path_logging_fastapi_yml
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
设置fastapi log
"""
fastapi_logger, fastapi_log_config = get_logger(path_relative_fastapi / "fastapi.log", path_logging_fastapi_yml, "uvicorn.error") #"root"

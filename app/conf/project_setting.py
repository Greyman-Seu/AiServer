# @File  : project_setting.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

from pathlib import Path

# %% --------------------------
"""
项目基本配置
"""
project_name = "test1"
version_api = "1"
prefix_str = "/api/v" + version_api
cors_origins = []  # ["https://192.168.0.1:8080",,] #跨域共享

host = "127.0.0.1"
port = "8080"

# %% --------------------------
"""
配置参数路径
"""
path_log = Path(__file__).parents[1]/"log"
path_logging_fastapi_yml = Path(__file__).parents[1]/"conf"/"logging_fastapi.yml"
path_logging_celery_yml = Path(__file__).parents[1]/"conf"/"logging_celery.yml"
path_api_yml = "api.yml"  # can be absolute path
path_celery_yml = "celery.yml"

path_staticfiles = Path(__file__).parents[2]/"requirements"/"static_swagger_redoc"


# %% --------------------------
"""
设置统一的输出接口
"""
return_service = {
    "success": None,  # bool 0/1
    "messages": None
}

return_tasks = {
    "task_id": None,
    "messages": None
}
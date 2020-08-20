# @File  : test_services.py
# @Date  :  2020/08/14
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

from fastapi import APIRouter

from app.conf.project_setting import return_service
from app.api.src.services.test_services import print_name as print_name_func
from app.core.logging_core.logging_fastapi import fastapi_logger


router = APIRouter()

# todo:提示查找日志文件
@router.get("/{username}")
def print_name(username: str):
    fastapi_logger.info("[*] test print_name func")

    print_name_func(username)
    return_service["success"] = 1
    return_service["messages"] = "print name success"
    return return_service
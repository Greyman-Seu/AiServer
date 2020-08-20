# @File  : test_services.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

from app.core.logging_core.logging_fastapi import fastapi_logger

def print_name(name):
    fastapi_logger.info(f"name is {name}")


if __name__ == "__main__":
    print_name("sbo")

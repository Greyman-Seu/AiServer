# @File  : test_tasks.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com
from app.core.logging_core.logging_celery import celery_logger


def add(x, y):
    celery_logger.info("[*]test add_capp func")
    return x + y


if __name__ == "__main__":
    celery_logger.info(add(1, 2))

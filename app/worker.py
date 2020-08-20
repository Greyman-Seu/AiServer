# @File  : worker.py
# @Date  :  2020/08/18
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

# %% --------------------
"""
唤醒celery
"""
from app.core.celery_app import celery_app as capp


@capp.task(acks_late=True)
def run_celery():  # word: str
    return f"[*]celery[*] initialization is successful"


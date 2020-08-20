# @File  : task_query.py
# @Date  :  2020/08/18
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com



from fastapi import APIRouter
from app.core.celery_app import celery_app as capp


router = APIRouter()

# todo:提示查找日志文件
@router.get("/{task_id}")
def task_query(task_id: str):
    task_result = capp.AsyncResult(task_id)
    if task_result.successful():
        return {"status": "Finished", "message": "finish", "result": task_result.result}
    elif task_result.failed():
        if task_result.traceback:
            return {"status": "Fail", "message": "任务执行出现问题，具体原因如下：\n" + task_result.result}
        else:
            return {"status": "Fail", "message": "任务执行出现问题，具体原因见log文件"}
    else:
        return {"status": "Runing", "message": "任务正在执行"}

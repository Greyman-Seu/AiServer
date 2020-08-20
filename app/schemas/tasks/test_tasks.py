# @File  : test_tasks.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

from pydantic import BaseModel, Field


class TestTaskConfig(BaseModel):
    task_id: str = Field(None, description="任务id")
    x: int = Field(..., description="输入x")
    y: int = Field(..., description="输入y")

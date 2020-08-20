# @File  : base_tasks.py
# @Date  :  2020/08/18
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com
from app.conf.project_setting import return_tasks

def base_api_tasks(router, model, tasks_config, return_message):
    @router.post("/")
    async def api(config: tasks_config):
        config_dict = dict(config)
        task_id = config_dict.pop("task_id")
        if task_id is None:
            res = model.apply_async(kwargs=config_dict)
        else:
            res = model.apply_async(kwargs=config_dict, task_id=task_id)

        return_tasks["task_id"] = res.id
        return_tasks["messages"] = return_message

        return return_tasks

    return api

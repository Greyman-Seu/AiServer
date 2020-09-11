# @File  : run.py
# @Date  :  2020/08/14
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.tools import set_swagger_ui
from app.api.api import api_router
from app.conf import project_setting
from app.core.logging_core.logging_fastapi import fastapi_logger, fastapi_log_config


# todo:格式化打印
prefix_str = project_setting.prefix_str

app = FastAPI(
    title=project_setting.project_name,
    openapi_url=prefix_str+"/openapi.json",
    docs_url=None,
    redoc_url=None
)

# 解决离线无法使用swagger ui
app = set_swagger_ui(app, project_setting)

# 配置CORS
if ~project_setting.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=project_setting.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

# 添加并设置固定头部
app.include_router(api_router, prefix=prefix_str)

# 调试接口
fastapi_logger.info(f"RESTful: http://{project_setting.host}:{project_setting.port}/docs")

if __name__ == "__main__":
    uvicorn.run(app,
                host=project_setting.host,
                port=int(project_setting.port),
                log_level="info",
                log_config=fastapi_log_config)

    # todo(do): 可以全覆盖：https://www.cnblogs.com/zhangliang91/p/13388200.html

# @File  : tools_api.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com


# %% ------------------------
"""
格式化输出api配置文件
"""
import prettytable as pt


def print_api_config(config: dict):
    tb = pt.PrettyTable()
    tb.field_names = ["API Name", "Prefix", "Tags", "Kind", "Path"]

    for kind in ["services", "tasks"]:
        for key, vaule in config.get(kind, {}).items():
            if key != None:  # 可能没有service或者tasks
                tb.add_row(
                    [key,
                     vaule["prefix"],
                     vaule["tags"],
                     kind,
                     "hub." + kind + "." + vaule.get("path", key)
                     ])

    # print(tb)
    return tb


# %% ------------------------
"""
加载静态文件,在离线环境中可以使用
"""

from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)


def set_swagger_ui(app, project_setting):
    app.mount("/static", StaticFiles(directory=project_setting.path_staticfiles), name="static")

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
        )

    return app
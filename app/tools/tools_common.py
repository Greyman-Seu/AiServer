# @File  : tools_common.py
# @Date  :  2020/08/17
# @Author: zhuyangkun
# @Email:zyk_120403228@163.com


# %% ------------------------
"""
YAML 文件读取
"""
import yaml


def get_yaml_data(path_yaml):
    with open(path_yaml, "r", encoding="utf-8") as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


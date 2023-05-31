from aws_cdk import Environment
from collections import OrderedDict
from sysops import get_env, get_config

def test_get_config():
    config = get_config()
    assert type(config) == OrderedDict

def test_get_env():
    env = get_env()
    assert type(env) == Environment
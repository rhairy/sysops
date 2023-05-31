import dotenv
from aws_cdk import App, Environment, Stack
from sysops.sysops_stack import SysopsStack

def get_config() -> dict:
    config = dotenv.dotenv_values()
    if "AWS_ACCOUNT_ID" not in config.keys():
        raise ValueError("Set AWS_ACCOUNT_ID in dotenv file")
    if "AWS_REGION" not in config.keys():
        raise ValueError("Set AWS_REGION in dotenv file")
    if "VPC_ID" not in config.keys():
        raise ValueError("Set VPC_ID in dotenv file")
    return config
    
def get_env() -> Environment:
    env = get_config()
    return Environment(account=env['AWS_ACCOUNT_ID'], region=env['AWS_REGION'])

def stack_factory(construct: App, stack_type: str) -> Stack:
    config = get_config()
    env = get_env()

    if stack_type == "sysops":
        return SysopsStack(construct, "sysops-stack", config, env=env)

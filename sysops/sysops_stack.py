from aws_cdk import Stack
from aws_cdk.aws_logs import LogGroup

from constructs import Construct


class SysopsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.log_group = LogGroup(self, "LogGroup")

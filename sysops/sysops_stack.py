from aws_cdk import Stack
import aws_cdk.aws_logs as logs
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from collections import OrderedDict
from constructs import Construct


class SysopsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, stack_config: OrderedDict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.log_group = logs.LogGroup(self, "LogGroup")

        self.role = iam.Role(self, "logging-instance-iam-role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        self.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))

        self.ec2_instance = ec2.Instance(self, "logging-instance",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=ec2.Vpc.from_lookup(self, "vpc", 
                vpc_id=stack_config['VPC_ID'],
                region=self.region
            ),
            role=self.role
        )


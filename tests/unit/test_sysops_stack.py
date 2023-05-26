#import aws_cdk as core
#import aws_cdk.assertions as assertions
from aws_cdk import App
from aws_cdk.assertions import Template

from sysops.sysops_stack import SysopsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sysops/sysops_stack.py
def test_sqs_queue_created():
    app = App()
    stack = SysopsStack(app, "sysops")
    template = Template.from_stack(stack)

    # template.has_resource_properties("AWS::Logs::LogGroup", {
    #     "VisibilityTimeout": 300
    # })
    template.resource_count_is("AWS::Logs::LogGroup", 1)

import aws_cdk as cdk
import aws_cdk.assertions as assertions
import sysops

def test_sysops_stack():
    app = cdk.App()
    stack = sysops.stack_factory(app, "sysops")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Logs::LogGroup", 1)
    template.resource_count_is("AWS::EC2::Instance", 1)
    template.resource_count_is("AWS::IAM::Role", 1)

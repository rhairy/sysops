#!/usr/bin/env python3
import aws_cdk as cdk
import sysops

app = cdk.App()
stack = sysops.stack_factory(app, "sysops")

app.synth()

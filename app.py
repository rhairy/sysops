#!/usr/bin/env python3
import aws_cdk as cdk
import dotenv
import sysops

from sysops.sysops_stack import SysopsStack

app = cdk.App()
SysopsStack(app, "SysopsStack", sysops.get_config(), env=sysops.get_env())

app.synth()

#!/usr/bin/env python3
from aws_cdk import App

from sysops.sysops_stack import SysopsStack

app = App()
SysopsStack(app, "SysopsStack")

app.synth()

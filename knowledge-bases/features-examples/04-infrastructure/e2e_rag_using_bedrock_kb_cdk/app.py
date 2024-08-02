#!/usr/bin/env python3
import os

import aws_cdk as cdk
from constructs import DependencyGroup

from config import EnvSettings, KbConfig
# from e2e_rag_using_bedrock_kb_cdk.e2e_rag_using_bedrock_kb_cdk_stack import E2ERagUsingBedrockKbCdkStack
from stacks.kb_role_stack import KbRoleStack
from stacks.oss_infra_stack import OpenSearchServerlessInfraStack
from stacks.kb_infra_stack import KbInfraStack

app = cdk.App()
# create IAM role for e2e RAG

KbRoleStack(app, "KbRoleStack")

# setup OSS
OpenSearchServerlessInfraStack(app, "OpenSearchServerlessInfraStack")

# # create Knowledgebase and datasource
KbInfraStack(app, "KbInfraStack")
app.synth()

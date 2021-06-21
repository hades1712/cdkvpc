from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (
    aws_ec2 as ec2,
    core    
)


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, "VPC",
                        cidr="10.0.0.0/16",
                        max_azs=3,
                        subnet_configuration=[ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.PUBLIC,
                            name="Public",
                            cidr_mask=24
                        ), ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.PRIVATE,
                            name="Private",
                            cidr_mask=24
                        ), ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.ISOLATED,
                            name="DB",
                            cidr_mask=24
                        )
                        ],
                        # nat_gateway_provider=ec2.NatProvider.gateway(),
                        nat_gateways=3,
                        )
        core.CfnOutput(self, "Output",
                    value=self.vpc.vpc_id)

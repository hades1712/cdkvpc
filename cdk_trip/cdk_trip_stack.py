from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (
    aws_ec2 as ec2,
    core,
    aws_s3 as s3
)


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, "VPC",
                        cidr="10.0.0.0/17",
                        max_azs=3,
                        subnet_configuration=[ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.PUBLIC,
                            name="Public",
                            cidr_mask=21
                        ), ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.PRIVATE,
                            name="Private",
                            cidr_mask=20
                        ), ec2.SubnetConfiguration(
                            subnet_type=ec2.SubnetType.ISOLATED,
                            name="DB",
                            cidr_mask=22
                        )
                        ],
                        nat_gateways=2,
                        )
        self.vpc.add_s3_endpoint("prodctvpcgateway")             #endpoint
        bucket=s3.Bucket(self,"IBU-dongshichao-mybucket")    
    def vpcoutput(self):
            output= {"vpc_cidr_block":self.vpc.vpc_cidr_block,"vpc_id":self.vpc.vpc_id,
                        "public_subnets":self.vpc.public_subnets,"private_subnets":self.vpc.private_subnets,
                        "DBsubnets":self.vpc.isolated_subnets}
            for k, v in output.items():

                core.CfnOutput(self, k,
                            value=str(v)
                            )      

### Prerequisites

- Create 2 different users using the AWS IAM services
- Install the AWS CLI to access AWS from the device using the following steps:
	  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html (Mac)
                                    (or)
	  curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
	  sudo installer -pkg AWSCLIV2.pkg -target /
	  which aws
	  aws --version
- Install Python3
- Download the Boto3 Python SDK for AWS CLI
- To do this, download the Python packet manager, Pip
- Use the command : apt-get install Python3-pip3
- Using Pip, download Boto3
- Use the command: pip3 install boto3

### Solution Steps:

- Set up the source and destination S3 buckets
- Upload the necessary data to the source S3 bucket
- Set up the AWS profiles for the source and destination accounts
- Initialize the S3 clients with the specified profiles using the boto3.Session function
- List the objects in the source bucket using the list_objects function
- Copy each object from the source bucket to the destination bucket using the get function
- Copy the object from the source to the destination bucket using the copy_object function

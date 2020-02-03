# Installation

If you have not already done so:
- Create an [account in AWS with full admin privileges](https://docs.aws.amazon.com/translate/latest/dg/setting-up.html).
- Download and install Python 3.7 and the AWS Command Line Interface (AWS CLI). The instructions will make use of the cli command lines.

The recommended way to install Python is through [PyEnv](https://github.com/pyenv/pyenv#installation)

[See here for the AWS CLI installation - version 1](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)

## Set-Up Files

Clone the repository to a folder on your local computer. Once cloned, unzip "Web-Setup.zip" into its folder. 

Either through the AWS CLI or through the AWS S3 Console GUI create an S3 bucket that will be the repository for the default files. For example it could be called ***morfless-package***

Use the following AWS CLI command to copy the content of the local package folder to S3:

        aws s3 cp <local_package_bucket>/ s3://morfless-package/ --recursive

## Cloud Formation Set Up

The cloud formation templates can be found under [package/cloudformation](https://github.com/MickyHCorbett/MorfLess/tree/master/package/cloudformation). You can run these in the CloudFormation GUI within your AWS console or by command lines. 

Before using any CloudFormation template, create a separate folder for them and copy them from the git clone. That way you won't have to overwrite the defaults.

### MorfLess: Part1 - Create Morfless Elements

The CloudFormation file MorfLess-Part1-CreateMorflessElements.yml contains the following Parameter section:

    Parameters:
       morflessS3WebsiteBucket:
         Type: String
         Default: mydomain.com
         Description: The target bucket i.e. website. Dots can be used.
       morflessListBucket:
         Type: String
         Default: morfless-mydomain-list
         Description: The backend list bucket
       morflessSourceBucket:
         Type: String
         Default: morfless-mydomain-source
         Description: The backend source files bucket
       morflessSearchBucket:
         Type: String
         Default: morfless-mydomain-search
         Description: The backend search files bucket   
         
       morflessPackageBucket:
         Type: String
         Default: morfless-package
         Description: Bucket where source package files are held 
         
       morflessLayerName:
         Type: String
         Default: morflessLibs-mydomain
         Description: Unique layer for a MorfLess instance. Use dashes 
       morflessSearchApiName:
         Type: String
         Default: morflessMyDomainSearchApi
         Description: Morfless Search Api name
         
       morfessApiStageName:
         Type: String
         Default: prod
         
       morflessStateMachineName:
         Type: String
         Default: morflessMyDomainStateMachine
         Description: State Machine Name 
       morflessAppPreFix:
         Type: String
         Default: morfless-mydomain
         Description: The prefix for the functions associated with this instance of MorfLess. Use dashes.

Change the _mydomain_ and _MyDomain_ elements match what you want your website or web development site to be called. A bucket will be created that hosts the static website with the following address: 

        mydomain.com.s3-website.<aws-region>.amazonaws.com

The file can be run from the CloudFormation GUI or by using the following AWS CLI command:

        aws cloudformation create-stack \
                --stack-name <morfless-deployment-name> \
                --template-body file://path/to/file/MorfLess-Part1-CreateMorflessElements.yml \
                --capabilities CAPABILITY_NAMED_IAM

### MorfLess: Part2 - Copy Default to Buckets

The CloudFormation file MorfLess-Part2-CopyDefaultsToBuckets.yml contains the following Parameter section:

    Parameters:
       morflessS3WebsiteBucket:
         Type: String
         Default: mydomain.com
         Description: The target bucket i.e. website. Dots can be used.
       morflessListBucket:
         Type: String
         Default: morfless-mydomain-list
         Description: The backend list bucket
       morflessSourceBucket:
         Type: String
         Default: morfless-mydomain-source
         Description: The backend source files bucket
       morflessSearchBucket:
         Type: String
         Default: morfless-mydomain-search
         Description: The backend search files bucket 

Set these value to the same ones that you used in Part 1

The file can be run from the CloudFormation GUI or by using the following AWS CLI command:

        aws cloudformation create-stack \
                --stack-name <morfless-deployment-copyinit_name> \
                --template-body file://path/to/file/MorfLess-Part2-CopyDefaultsToBuckets.yml \
                --capabilities CAPABILITY_NAMED_IAM
                
## Updating settings.txt

At this stage all of the elements will be in place. Go to the Cloud Formation admin panel and select the CloudFormation named _morfless-deployment-name_. Go to the Outputs tab and copy the Api Invoke Url. 

In your local package folder (the copy) open settings.txt and copy the url into search_api_url={ }: section i.e.

        search_api_url={ }:
        
will become:

        search_api_url={ https://<api-ident>.execute-api.eu-west-1.amazonaws.com/prod }:
        
Ensure that the keyword format is maintained

Upload settings.txt to the Source Bucket folder in S3.

##

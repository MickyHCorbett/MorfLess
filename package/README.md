# Installation

If you have not already done so:
- Create an [account in AWS with full admin privileges](https://docs.aws.amazon.com/translate/latest/dg/setting-up.html).
- Download and install Python 3.7 and the AWS Command Line Interface (AWS CLI). The instructions will make use of the cli command lines.

The recommended way to install Python is through [PyEnv](https://github.com/pyenv/pyenv#installation)

[See here for the AWS CLI installation - version 1](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)

If you are Upgrading - see [here](https://github.com/MickyHCorbett/MorfLess/blob/master/package/upgrading.md)

## Set-Up Files

Clone the repository to a folder on your local computer. Once cloned, unzip "Web-Setup.zip" into its folder. 

Either through the AWS CLI or through the AWS S3 Console GUI create an S3 bucket that will be the repository for the default files. For example it could be called ***morfless-package***

Before copying the files from the local package folder, decide what kind of site you want. The folder in question is "source-files-setup". There are two options:
- A blog - copy all the files in this folder using the command
- Not a blog - copy only 404.page, index.page, authors.page, search.page and settings.txt. Remove the files: categories.page, archive.page and posts.page, then use the command below

Use the following AWS CLI command to copy the content of the local package folder to S3:

        aws s3 cp <local_package_bucket>/ s3://morfless-package/ --recursive
        
## Set-up Buckets 

The 4 buckets used for MorfLess are set up separately using the CloudFormation template Morfless-CreateBuckets.yml. This is done as deleting and recreating buckets can cause issues if you link your site to CloudFront. It also means you can decide to leave the content as is and just respin up the functions and apis.

The CloudFormation file MorfLess-CreateBuckets.yml contains the following Parameter section:

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
         
Change the _mydomain_ and _MyDomain_ elements to match what you want your website or web development site to be called. A bucket will be created that hosts the static website with the following address: 

        mydomain.com.s3-website.<aws-region>.amazonaws.com

## Cloud Formation Set Up Part 1

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

Change the _mydomain_ and _MyDomain_ elements to match the bucket names you set up.

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

Set these values to the same ones that you used in Part 1

The file can be run from the CloudFormation GUI or by using the following AWS CLI command:

        aws cloudformation create-stack \
                --stack-name <morfless-deployment-copyinit-name> \
                --template-body file://path/to/file/MorfLess-Part2-CopyDefaultsToBuckets.yml \
                --capabilities CAPABILITY_NAMED_IAM
                
## Updating settings.txt

At this stage all of the elements will be in place. Go to the Cloud Formation admin panel and select the CloudFormation named _morfless-deployment-name_. Go to the Outputs tab and copy the Api Invoke Url. 

In your local package folder (the copy) open settings.txt and copy the url into search_api_url={ }: section i.e.

        search_api_url={ }:
        
will become:

        search_api_url={ https://<api-ident>.execute-api.<aws-region>.amazonaws.com/prod }:
        
Ensure that the keyword format is maintained

Upload settings.txt to the Source Bucket folder in S3.

## Cloud Formation Set Up Part 2

The last part of the set-up is to add notifications for the Source Bucket to then call TriggerStates which kicks off the Step Function.

### MorfLess: Part3 - Assign Bucket Notifications

The CloudFormation file MorfLess-Part3-MorfLess-Part3-AssignBucketNotifications.yml contains the following Parameter section:

    Parameters:
       morflessSourceBucket:
         Type: String
         Default: morfless-mydomain-source
         Description: The backend source files bucket defined in MorfLess setup Part 1
       morflessAppPreFix:
         Type: String
         Default: morfless-mydomain
         Description: The function prefix defined in MorfLess setup Part 1
      
Set these values to the same ones that you used in Part 1

The file can be run from the CloudFormation GUI or by using the following AWS CLI command:

        aws cloudformation create-stack \
                --stack-name <morfless-deployment-applynotifications-name> \
                --template-body file://path/to/file/MorfLess-Part3-AssignBucketNotifications.yml \
                --capabilities CAPABILITY_NAMED_IAM
                
That completes the setup. The application is now active and will respond to files uploaded into the Source Bucket. 

[Next step: Building out the site](https://github.com/MickyHCorbett/MorfLess/blob/master/user-guide/building-the-site.md) 

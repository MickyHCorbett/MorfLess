# Upgrading

In the event that you update any of the core files in Libraries or in the lambdas, you will want to redeploy your CloudFormation stacks.

To do this you first must delete some of the stacks, copy the current data to a backup bucket, then delete the main stack formed in Part 1. 

## Removing Notifications

Remove the notifications from the Source bucket by deleting the stack. You can delete the stack in the AWS Cloud Formation GUI or use the following AWS CLI command:

    aws cloudformation delete-stack --stack-name <morfless-deployment-applynotifications-name>
    
You can also delete the Copy Defaults to Buckets formation:

    aws cloudformation delete-stack --stack-name <morfless-deployment-copyinit-name>
    
## Creating Backup

Create a backup by creating an S3 bucket e.g. ***morfless-backup***

Modify the Parameters section in the cloudformation file MorfLess-BackUpBuckets.yml:

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

      BackupBucket:
        Type: String
        Default: morfless-backup
        Description: S3 bucket containing the backups

Run the file in the GUI or by the following AWS CLI command giving the stack _morfless-deployment-reset-name_ an appropriate name::

    aws cloudformation create-stack \
        --stack-name <morfless-deployment-reset-name> \
        --template-body file://path/to/file/MorfLess-BackUpBuckets.yml \
        --capabilities CAPABILITY_NAMED_IAM
        
## Clear Buckets 

Before the main stack is deleted, the buckets must be cleared, otherwise a DELETE_FAILED message will be displayed in Cloud Formation. 

Use the file MorfLess-ClearBuckets.yml and modify the Parameters section to match your bucket names:

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

Run the file in the GUI or by the following AWS CLI command giving the stack _morfless-deployment-cleardeploy_ an appropriate name:

    aws cloudformation create-stack \
        --stack-name <morfless-deployment-cleardeploy> \
        --template-body file://path/to/file/MorfLess-BackUpBuckets.yml \
        --capabilities CAPABILITY_NAMED_IAM
        
Once the stacks run, you can delete the Backup and Clear Buckets formations either in the GUI or by the following commands:

    aws cloudformation delete-stack --stack-name <morfless-deployment-reset-name>
    
    aws cloudformation delete-stack --stack-name <morfless-deployment-cleardeploy>
    
## Delete Main stack

You can now delete the main stack i.e. _morfless-deployment-name_ from Part 1. The AWS CLI command is:

    aws cloudformation delete-stack --stack-name <morfless-deployment-name>
    
## Upgrading

Upload the new files to a package folder and modify MorfLess-Part1-CreateMorflessElements.yml to match (as in the Installation instructions). Repeat the steps of Installation but instead of using the package folder that contains defaults, use the Back up folder to restore all the content.


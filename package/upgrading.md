# Upgrading

In the event that you update any of the core files in Libraries or in the lambdas, you will want to redeploy your CloudFormation stacks.

To do this you first must delete some of the stacks, copy the current data to a backup bucket, then delete the main stack formed in Part 1. 

## Removing Notifications

Remove the notifications from the Source bucket by deleting the stack. 

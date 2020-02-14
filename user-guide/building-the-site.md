# Building The Site

Once MorfLess is installed, the task now turns to adding post and page schematics. The first thing to do is to download the Source Bucket content to a local folder

To do this, navigate to the local folder and use the following AWS CLI command substituing the _local folder_ and _morfless-source-bucket_ with the names of your folder and bucket name:

    aws s3 cp s3://morfless-source-bucket/ . --recursive
    
Alternatively you can use the Amazon S3 GUI or third-party tools such as CloudBerry. 

You can then upload the files again to trigger the creation of content i.e.:

    aws s3 cp local-folder/ s3://morfless-source-bucket/  --recursive
    
    

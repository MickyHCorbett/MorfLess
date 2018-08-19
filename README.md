# MorfLess

A Python-based serverless blog/website architecture that runs in Amazon Web Services. MorfLess uses the PoliMorf schematic approach taking meta source files and parsing them into html files with associated linked archiecture. Supporting files (css, JavaScript etc) can be linked privately or publicly. 

# Basic Architecture
MorfLess uses two AWS Lambdas: a standard Lambda linked to S3, and a Lambda@Edge (CloudFront Edge Lambda). The S3 Lambda is asynchonous while the Lambda@Edge modifies outgoing HTML document bodies to refer to private resources. 

# Dependencies
MorfLess is best used on an existing Route 53 - CloudFront - S3 architecture. 

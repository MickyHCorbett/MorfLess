# MorfLess

A Python-based serverless blog/website architecture that runs in Amazon Web Services. MorfLess uses the PoliMorf schematic approach taking meta source files and parsing them into html files with associated linked archiecture. Supporting files (css, JavaScript etc) can be linked publicly. 

The initial version will deal with public links only.

# Basic Architecture
MorfLess is structured in two parts: 
- The core elements featuring S3 buckets and an AWS Step Function - parsing html, updating json files and JavaScript constants
- Search lambda driven through API Gateway that returns data to the website

There are 4 buckets: A source bucket, a list bucket, a search bucket and the target bucket (the website)
A CloudTrail event is used to trigger the Step Function when a file is uploaded or deleted from the source bucket. 

The Step Function consists of two Lambdas:
- RenderHtml
- CreateListPages 

RenderHtml either creates a single HTML file, updates multiple files if the file uploaded is a dependent file, or deletes the target file if a file is deleted from the source bucket. In addition, lists of post/page meta properties are created along with information on displaying lists of posts and pagination. Raw content is also created and added to the search bucket.

CreateListPages takes the list information and creates JavaScript constants for post lists and pagination. 

SearchContent scans the content in the search bucket and returns a formatted list of post and page entries.

Note: If you wish to run the site through Cloudfront you can use Lambda@Edge to re-route requests (standard www to non-www etc) as a seperate microservice set-up.

# Dependencies
MorfLess is best used if you have a user with Admin privileges. 

# MorfLess

A Python-based serverless blog/website architecture that runs in Amazon Web Services (AWS). MorfLess uses the PoliMorf schematic approach taking meta source files and parsing them into html files with associated linked archiecture. Supporting files (css, JavaScript etc) can be linked publicly. 

The initial version will deal with public links only.

The website runs as a STATIC website with JS enhancements and an API search capability. MorfLess is not a web server application. It creates static content through the use of templates.


## Description
MorfLess is structured in two parts: 
- The core elements featuring S3 buckets and an AWS Step Function - parsing html, updating json files and JavaScript constants
- Search lambda driven through API Gateway that returns data to the website

There are 4 buckets: A source bucket, a list bucket, a search bucket and the target bucket (the website)
There are 4 lambdas: RenderHtml, CreateListPages, SearchContent and TriggerStates.

An S3 notification event is used to call TriggerStates which in turn calls the Step Function when a file is uploaded or deleted from the source bucket. 

The Step Function consists of two Lambdas:

- RenderHtml
  - RenderHtml either creates a single HTML file, updates multiple files if the file uploaded is a dependent file, or deletes the target file if a file is deleted from the source bucket. In addition, lists of post/page meta properties are created along with information on displaying lists of posts and pagination. Raw content is also created and added to the search bucket.
  
- CreateListPages 
  - CreateListPages takes the list information and creates JavaScript constants for post lists and pagination. 

The search lambda (SearchContent) scans the content in the search bucket and returns a formatted list of post and page entries.

## Architecture

MorfLess is arranged as a worklow where a template (schematic) file is updated or deleted from a bucket in S3 (Source Bucket). The event triggers a series of Lambdas (through the Step Function) which take the file and parse it into html, which is output into the Website Bucket. Depending on the command syntax in the file, additional information is added to meta files (stored in the List Bucket). Stripped down (raw) html files are also put into a Search Bucket that can be accessed through an API Gateway.

Once the html file is created, the next step is to update the associated files that mimic blog database entries i.e. lists of category, author and archive information. MorfLess is a static site so associations are created using links to JavaScript constant files. These files are accessed by JavaScript handler references that have been inserted into the html when a given schematic command is present.

<img src="https://github.com/MickyHCorbett/MorfLess/blob/master/MorflessArchitecture.png" width=100% align="center" />

When a search request is made, the API Gateway communicates with Lambda and searches through the raw content files. Lambda will condition the result and send back a formatted list. The formatting uses the same functions that are used to create list meta files.

## Installation 

Go to [MorfLess Installation instructions](https://github.com/MickyHCorbett/MorfLess/blob/master/package/installation.md)

## Syntax 

Go to [MorfLess Syntax](https://github.com/MickyHCorbett/MorfLess/blob/master/syntax/syntax-introduction.md)

## Dependencies
You will need an AWS account and a user with Admin privileges (recommended NOT to be the root user). 
You can use any text editor.

## Options 

By default, the target bucket will be of the form "$TARGET_BUCKET.s3-website.$AWS_REGION.amazonaws.com". You can choose to front it with CloudFront/Route53 using a domain name of your choosing - see [Hosting a static website on S3 with CloudFront/Route53](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)
  
If you wish to run the site through Cloudfront you can also use Lambda@Edge to re-route requests (standard www to non-www etc) as a seperate microservice set-up.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This application was built from many hours of experimentation and reading AWS support documentation

# Building The Site

Once MorfLess is installed, the task now turns to adding post and page schematics. The first thing to do is to download the Source Bucket content to a local folder

To do this, navigate to the local folder and use the following AWS CLI command substituing the _local folder_ and _morfless-source-bucket_ with the names of your folder and bucket name:

    aws s3 cp s3://morfless-source-bucket/ . --recursive

Alternatively you can use the Amazon S3 GUI or third-party tools such as CloudBerry.

You can then upload the files again to trigger the creation of content i.e.:

    aws s3 cp local-folder/ s3://morfless-source-bucket/  --recursive

If you upload the raw sources files back into the source bucket and don't change any more of the settings.txt file then those defaults will be applied.

# Settings

To change the site settings to something that matches what you want, there are a number of elements that you should change that will form the foundation of your site:

- Default thumbnail for posts and pages
- Default author for posts and pages
- Template and core page search information

## Default thumbnail

The default thumbnail will show on any page or post when the meta information doesn't include a thumbnail keyword and definition:

        default_thumbnail={ /images/site-background.jpg }:

## Default author

The default author will be for any post or page that hasn't any author meta information. The name and shortname are used to identify pages and posts for that author. For example, if a page or post is added with the author meta tag set to the shortname, it will be identified with the name. The name will be what appears on any meta or search information.

It is recommended that all the JSON keys are used even though only the name and shortname are mandatory.

        default_author={

          {
              "name": "Default Team",
              "shortname": "TDEF",
              "thumbnail": "/images/default_team.jpg",
              "description": "General information and content from the site"
          }

        }:

If you have already uploaded data to the site and an author list (authors.json) has been updated with the default "None" author, you need to change the list file (in the list bucket) to remove this. The next time a page or post is uploaded (or any dependent files) this author list and associated pages will be regenerated.

## Template and core page search information

These settings come up when a site search occurs. Because these files are not included in the main list of pages and posts their settings are defined here:

The keyword syntax is:

        template_search_content={ <JSON content> }:

The default JSON content within is as below. This replaces the core default settings that are defined in the python file globals.py:

        template_search_content={

        {
            "categories": {
                "name": "Categories",
                "thumbnail": "/images/Polimorf-shapes-background-orange.jpg",
                "description": "Posts listed by category"
            },
            "authors": {
                "name": "Authors",
                "thumbnail": "/images/Polimorf-shapes-background-yellow.jpg",
                "description": "Posts and pages listed by author"
            },
            "archive": {
                "name": "Archive",
                "thumbnail": "/images/Polimorf-shapes-background-black.jpg",
                "description": "Monthly archives arranged by most recent to older"
            },
            "posts": {
                "name": "Posts",
                "thumbnail": "/images/Polimorf-shapes-background-darkblue.jpg",
                "description": "Posts by various authors and in various categories"
            },
            "index": {
                "name": "Home",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": "Welcome to the site! Feel free to browse around and follow the links to other pages and posts"
            },
            "404": {
                "name": "Not Found",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": "When you can't find anything you end up here!"
            }
        }

        }:

## Author and category details

When you add an author to a page/post meta, it gets added to the list of authors (authors.json) in the list bucket if the author is not already on the list. It will add the name, shortname and the default thumbnail but have no description. In the settings file you change this detail by adding an entry to the authors meta in settings as below. The syntax is JSON.

        author={
          [
            {
                "name": "Author name 1",
                "shortname": "AUT1",
                "thumbnail": "/images/author1.jpg",
                "description": "General information for author1"
            },
            {
                "name": "Author name 2",
                "shortname": "AUT2",
                "thumbnail": "/images/author2.jpg",
                "description": "General information for author2"
            }
          ]
        }:

Similarly is you add a category to a post meta, it will be added to the category list (categories.json). The default is name and the default thumbnail. You can change this by adding detail to the categories meta in settings:

        categories={

          [
            {
                "name": "Interesting things",
                "thumbnail": "/images/int-things.jpg",
                "description": "Interesting things to write about"
            },
            {
                "name": "animals",
                "thumbnail": "/images/animals.jpg",
                "description": "Posts about animals"
            },
          ]

        }:

## Site details



## Content meta defaults

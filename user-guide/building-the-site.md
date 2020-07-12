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

The main site details that appear in the head part of the html source can be modified using the following meta:

        title={ PoliMorfic }:
        description={ Some description }:

## Content meta and list defaults

The default posts per page is 5 but can be modified. For postlists, this will be the default if no posts per page is defined by a keyword command. For category, author and search lists this will be the default.

Content meta is defined for pages and posts as shown. Date format can be set to UK or US.

        posts_per_page={ 5 }:
        post_meta_default={ title, category, author, date_created, date_modified, show_time }:
        page_meta_default={ title, author, date_created, date_modified }:
        date_format={ UK }:

## Templates and Localisation

There are 5 templates: posts, categories, authors, archive and search. Do not use these names as your source files e.g. do not call a page schematic, "categories.page" unless you want the categories page to use this format. You can however change the name of the page as it is presented on the site.

The full template meta is shown below:

        templates={
          {
            "search": "search",
            "categories": "categories",
            "authors": "authors",
            "archive": "archive",
            "posts": "posts"
          }
        }:

        template_main_header_text={
          {
            "search": "Results for: ",
            "categories": "Categories",
            "authors": "Authors",
            "archive": "Monthly Archives",
            "posts": "Posts"
          }
        }:


        template_sub_header_text={

          {
            "categories": "Posts for category: ",
            "authors": "Posts by author: ",
            "archive": "Posts for month: "
          }
        }:

        template_sub_header_back_link_text={
          {
            "categories": "Back to Categories",
            "authors": "Back to Authors",
            "archive": "Back to Archives"
          }
        }:

If you wish to have an "entries" page that shows all the post type pages (blog entries) you change the value in the JSON under the templates keyword (templates={ ... }: shown below). You also change the header text on that template page (under template_main_header_text={ ... }:). You still upload the posts.page template to your source folder but it will now have a link as https://yoursite.com/entries/.


        templates={
          {
            "search": "search",
            "categories": "categories",
            "authors": "authors",
            "archive": "archive",
            "posts": "entries"
          }
        }:

        template_main_header_text={
          {
            "search": "Results for: ",
            "categories": "Categories",
            "authors": "Authors",
            "archive": "Monthly Archives",
            "posts": "Entries"
          }
        }:

The sub header text is for sub-category and individual author pages. The backlink text is also present on each of these sub-pages.

You can also change the language of this text and template output names meaning that it is quite easy to do localisation for your site.

## Default sections

The last part of the settings file is where you define the different default elements for each section. If you set any of these to default, the default schematic (in schematics.py) will be used. It is up to you if you wish to change this in the python. An easier way is to define schematic commands within each section. Then when a DEFAULT command is used in a page or post schematic it will use this information. Also, when you update the settings.txt file it will regenerate any schematic which includes DEFAULT commands.

The bare section settings in the basic settings file are:

        ///HEADER:
        %%DEFAULT::

        ///BEFORE::
        NONE

        ///MAIN:
        %%DEFAULT::

        ///AFTER:
        NONE

        ///SIDEBAR:
        NONE:

        ///FOOTER:
        %%DEFAULT::

# Inserts

Inserts are where you use schematic commands from another file to add content to your current file. The insert command is replaced with schematic commands and then these generate html elements. Inserts can also include addition commands, where content is added to the head or the footer before the close body tag.

An example of an insert being used in the Main section is:

        ///MAIN:
        %%INSERT::
        ref={ insert1.txt }:

The file insert1.txt could be:

        %%CONTENT::
        TEXT=[
        <p>Add this content</p>
        ]:

During parsing the insert will be processed and the result added to the html where the insert was called. Effectively the insert is the same as the following:

        ///MAIN:
        %%CONTENT::
        TEXT=[
        <p>Add this content</p>
        ]:

***Note:*** It is best not to use insert commands within insert files.

For more information see [Morfless - Inserts](https://polimorfic.com/morfless/inserts/)

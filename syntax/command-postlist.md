<- [Back to Syntax Commands](syntax-commands.md)

# POSTLIST

The POSTLIST command allows you to add a manual list of posts and arrange them how you see fit, including making stickies.
There is also a unique case where you can display all the posts on the site (i.e. post type pages). This can be used anywhere but the header.

For example:

    ///MAIN:
    %%POSTLIST::
    list={ article1.page, latest_post1.post }:

or

    ///MAIN:
    %%POSTLIST::
    list={
      article1.page,
      latest_post1.post,
      that_post2.post,
      this_post3.post
    }:
    posts_per_page={ 2 }:

or

    ///MAIN:
    %%POSTLIST::
    manual_sticky={}:
    list={
      article1.page,
      !!latest_post1.post,
      that_post2.post,
      this_post3.post
    }:
    posts_per_page={ 2 }:

## Subschematic Commands

None

## Keywords

There are 4 keywords for POSTLIST:

- manual_sticky - tells MorfLess that this postlist will have manually set sticky entries
- list - this is the list of posts and pages. To allocate a sticky use '!!' before the name of the entry
- posts_per_page - sets the number of entries per visible list sub-page. Numbered sub-pages will appear below the entries.
- title - adds a title to the postlist

### POSTS list attribute

If the list keyword is set to 'posts' or 'POSTS' the postlist will show all the posts. This can be used to create a blog list.

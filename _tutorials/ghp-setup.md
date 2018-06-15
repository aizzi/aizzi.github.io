---
---
# Publishing your website on GitHub pages

1. [Activate GitHub Pages](activate-github-pages)
2. [Configuring the website](configuring-the-website)
3. [Site Layout](site-layout)
4. [Customize the Layout](customize-the-layout)
5. [Define a Collection](define-a-collection)

--
## Activate GitHub Pages

If you want to build a website, sooner or later you need a way to test it and verify that users will be presented with what you intended to. In order to do so, you need a webserver.

*Apache*, *NGINX*, *Node.js*, *Tomcat* are some examples of web servers you can choose from. These programs are powerful and complex to setup. Use one of them could be a choice if you want to build and control your own environment, but this add an extra layer of unneeded complexity if what you want is just to start learning some plain HTML.

Nowadays there are other choices other than set up your own development environment. For example, you can use resources on Cloud. *Amazon AWS*, *IBM Softlayer*, *Microsoft Azure* are all possible choices. However, they replace one complexity layer with another one: you need to understand how they work and setup the environment (aside of providing your credit card number).

Luckily, there is a choice we can leverage to get quickly up and running with a basic static webserver: [GitHub Pages](https://pages.github.com/). GitHub Pages (GHP) is a static webserver based on [Jekyll](https://jekyllrb.com/) engine, integrated with GitHub repositories. It is able to serve static HTML pages as well as transform Markdown documents into HTML pages. It can works as a blogging platform and is integrated with your GitHub repositories to provide online documentation about your project.

Overall, it is an easy and inexpensive way to start your journey into web programming. Let's see how we can set it up.

GitHub Pages can serve two types of sites: *User or organization site* or *Project site*. At this stage, you can think of a *User or organization site* as a main container for all your *Project site*: all your *Project sites* will be served as children of your *User site*.

We are not interested now in digging into the working details of GitHub Pages, so we will start with focusing on creating your *User site* in order to use it to serve static web pages.

By now you should have created your GitHub profile. For example, my public profile is available at https://github.com/aizzi.

In order to create your GitHub Pages user site, you must create a new repository called `<username>.github.com`. Pay attention, that it must exactly match your username. If you are in doubt, you can find your username on the top-left side of your profile page, under your picture.

![username location](/assets/img/ghp-setup_img01.png)

So, go on and create it.

![create aizzi.github.io](/assets/img/ghp_setup-img02.png)

Once it is created, create the index page of your site `index.html` and copy the following text in it (changing my name with your one):

```HTML
<!DOCTYPE html>
<html>

  <head>
    <title>Antonello Izzi's Web Site</title>
  </head>

  <body>
    <h1>Antonello Izzi's Web Site</h1>
    <p>My personal static web site</p>
  </body>

</html>
```

That's it: your personal website is ready for your at the address `https://<username>.github.io`. Go on and check it!

Now, clone the repository on your computer and you are ready to go.

The nice part of this setup is that publishing your site is as easy as pushing your commits to the master branch of `<username>.github.io` repository. The GitHub Jekyll backend will do the rest, processing your site and publishing it.

> Note: since your commit has to be processed by the Jekyll engine, it could take a while before you see your changes published. Be patient and allow for it to work. Later on in this course we will setup a local Jekyll environment to test your changes before to push them, but for now what we have is more than enough.

A really valuable resource about how to work with Jekyll on GitHub Pages can be found [here](http://jmcglone.com/guides/github-pages/).

[Jekyll](https://jekyllrb.com) will run through your repository, ingest all your files, transform them as needed and serve them out as a static website which can be served on the internet.

The nice part of this is that, unlike Medium, or Linkedin or Blogger your posts and articles are still yours. You can control what goes up, and take it down as you like. If GitHub should close tomorrow, you will still have your website right there on your hard disk, ready to be publish somewhere else.

[Jekyll](https://jekyllrb.com) is blogging aware, meaning that if you maintain a specific naming convention for your files, it will be easy to publish your articles and serve them as a blog.

As a bonus, it will be extremely easy to link your Git project's documentation to your *site*, making it the very centre of your internet presence. Later on, you can still migrate it to a webserver able to provide dynamic content if you need. But until then, why bother with maintaining such an environment?

This tutorial is mostly the documentation of how this very site was developed from scratch. This means that I will update it while I progress in designing my site.

I will proceed by steps, building one feature after the other, solving problems as they present themselves and documenting all the steps and the choices I make. I have some HTML and CSS knowledge, as well as some programming skills, but it has been a while since I used them and lot of things did change over time. This means that sometimes I will come back to change something because I find a better way to do it, or because I simply changed my mind. All those changes will be documented here.

--
## Configuring the website
Although [Jekyll](https://jekyllrb.com) will scan through all your repository, some directories and files have a special meaning to it. Jekyll's directory structure is described [here](https://jekyllrb.com/docs/structure/). I will not repeat what's already described in the documentation, but summarizing it in a Jekyll enabled site you will find the following:

* `_config.yml` : a configuration file for Jekyll features, accurately described [here](https://jekyllrb.com/docs/configuration/)
* `_data` : it will contains all data used throughout your site. Any files stored in this directory can be accessed via a `site.data` variable.
* `_drafts` : this directory will contain all the drafts of your articles
* `_includes` : this directory contains files that can be included in other files in your site using the liquid tag ```{% raw %}{% include file.ext %}{% endraw %}```
* `_layouts` : this directory contains the template used to render your web pages. Providing the right [YAML FrontMatter](https://jekyllrb.com/docs/frontmatter/) in a file, you can insert the content of the file in the choosen template by using the tag ```{% raw %}{{ content }}{% endraw %}```
* `_posts` : this directory contains your blog articles, using the naming convention `yyyy-mm-dd-title-of-the-article.md`
* `_sass` : this directory contains the [sass](https://sass-lang.com/) files used throughout your website
* `index.html` : the index page of your site (we already created it).

The other directories are not directly used by us and are only important if you are going to build your own Jekyll engine. Since we are not going to do it yet, we'll skip them. So, now go on and create the files and directories in your `name.github.io` repository as requested.

Now, let's open the newly created `_config.yml` file and make some general configuration.

> Note: these are the configuration I made to this website. They are reported here for documentation. You can make your own. Read the documentation and decide what you want to do with your site!

```
timezone: Europe/Prague
show_drafts: FALSE
future: FALSE
```

--
## Site Layout

At this point, we have a very simple, old style static web site. If you know CSS and HTML, you can start working on the front-end, customizing the layout as you like. But what if you don't know CSS and/or don't want to invest time in working on the site layout? Maybe you, like me, are more interested in using the site to store your notes, projects, posts and tutorials.

Luckily for you, GitHub Pages provides you with a series of Jekyll themes you can choose from in order to help you. Let's see how you can enable one of these themes for your site.

First of all, navigate to your `<username>.github.io` repository. Open the `Settings` and scroll down to the `GitHub Pages` section. There, you can find the `Theme Chooser` option. Do you see that nice button ```Chose a theme```? Well, go on and click on it!

You will be presented with a list of themes to choose from. Choose the one that suits you most and click on the `Select theme` button when done. For this site, I've chosen the [Architect Theme](https://github.com/pages-themes/architect), but you can select whatever you like.

Now, let's modify our site to use the theme.

First of all customize the `_config.yml` file to enable the new theme by adding the following line:

```
theme: jekyll-theme-architect
```

Read the documentation of the theme you choose in order to understand what to add for your one.

Then, modify the `index.html` file to use the layout:

```
---
layout: default
---
```

The snippet above is called a ```YAML FrontMatter```and it is used to specify configurations and variables.  By specifying the `layout`, Jekyll will replace the ```{% raw %}{{ content }}{% endraw %}``` tag in the `_layouts\default.html` file provided by the theme with the actual content of the file (which is empty, for now).

Commit and push your updates and refresh the page. If everything is fine, you should get an empty page with the new graphics.

Now, let's do another step. We don't want to specify the layout for every single page in our site, so let's move it into the `_config.yml` file as a default choice. Add the following line at the end of your `_config.yml` file:

```
# Setting defaults configurations
defaults:
  -
    scope:
      path: "" # apply this default to all files in the project
      type: ["pages", "posts"] # apply only to pages and posts
    values:
      layout: "default"
```

Now:
* rename `index.html` to `index.md`
* remove the FrontMatter in `index.md`, since it was defined into the `_config.yml`
* add some text to see the changes.
* Commit and push your updates to see if it works.

Finally, as the last step of this phase, let's customize the Title and the description of the site. The chosen theme supports two general configuration variables for that: `title` and `description`. Let's add those into the `_config.yaml` file to set the corresponding values in the page header.

```
title: "Tetriminos"
description: "Filling (my) life with pieces of knowledge"
```

--
## Customize the Layout

At this point, you should have a working page you can reach at the url '<username>.github.io', that will show you the content of the `index.md` file in your root directory.

In order to have a website, you need to add contents, such as pages, and blog posts. Let's start with pages, like this tutorial for example. In order to do so, you must decide upfront the directory structure of your website.

For example, I want to use the right column of the theme I choose as a navigation column, allowing visitors of my site to reach out for the different sections of the sites.

Unfortunately, the standard layout provided does not allow for this out-of-the-box, so I'll have to modify it a little bit. This will require some knowledge of HTML and CSS.

Create a `_layouts/default.html` file in your site, and copy in it the content of the `_layouts/default.html` file of the chosen theme. Now, the local copy will be used by Jekyll instead on the standard one, and you can modify it to suit your needs.

--
## Define a Collection

I decided that I'd like to have a specific type of content that I will call *tutorials*. Tutorials are one-page articles, containing a step-by-step guide about a specific issue. These files will be stored in a specific directory called `_tutorials`, and will be defined as a specific [Collection](https://jekyllrb.com/docs/collections/).

Start by creating the `_tutorials/index.md` file. This will be the starting page when someone reaches the `<username>.github.io/tutorials` url.

Now we need to define the collection into the `_config.yml` file:

```
# collections
collections:
  tutorials:
    output: true
```

Then, edit the `_tutorials/index.md` and insert the following:

```
{% raw %}
# Tutorials

{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
{% endraw %}
```

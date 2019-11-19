#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'alex.gonzalez'
SITENAME = 'deeprivers'
SITEURL = ''
THEME = 'attila'
LOAD_CONTENT_CACHE = False

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Blog setup

STATIC_PATHS = ['images']
# HEADER_IMAGE = "/content/images/great-wave-off-kinosawa.jpg"
HOME_COVER = 'images/great-wave-off-kinosawa.jpg'
# HOME_COLOR = 'black'
# COLOR_SCHEME_CSS = 'monokai.css'

AUTHORS_BIO = {
  "alexgonzalez": {
    "name": "Alex Gonzalez",
    "cover": "images/last-night.jpg",
    "image": "images/last-night.jpg",
    "website": "http://alexgonzalez.dev",
    "location": "Terra",
    "bio": "This is my 200 character biography. Hello!"
  }
}

ARTICLE_PATHS = ['posts',]
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'alex.gonzalez'
SITENAME = 'deeprivers'
SITESUBTITLE = 'Sorry for the mess and welcome to my blog!'
SITEURL = 'https://alexgonzalez.dev'
THEME = 'theme' # or attila
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
LINKS = (('Github', 'http://github.com/alexgonzalez'),
        #  ('Python.org', 'http://python.org/'),
        #  ('Jinja2', 'http://jinja.pocoo.org/'),
        #  ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/alexgonzalez'),
          ('Twitter', 'http://twitter.com/gonz4lex_'),)

DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Blog setup

STATIC_PATHS = ['images', 'extra']
HEADER_IMAGE = "images/last_night.jpg"
HOME_COVER = 'images/last-night.jpg'
# HOME_COLOR = 'black'
# COLOR_SCHEME_CSS = 'monokai.css'

AUTHORS_BIO = {
  "alexgonzalez": {
    "name": "Alex Gonzalez",
    "cover": "images/great-wave-off-kinosawa.jpg",
    "image": "images/last-night.jpg",
    "website": "http://alexgonzalez.dev",
    "location": "Terra",
    "bio": "This is my 200 character biography. Hello!"
  }
}

ARTICLE_PATHS = ['posts',]
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
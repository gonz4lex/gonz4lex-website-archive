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
LINKS = (('Github', 'http://github.com/gonz4lex'),
        #  ('Python.org', 'http://python.org/'),
        #  ('Jinja2', 'http://jinja.pocoo.org/'),
        #  ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/gonz4lex'),
          ('Twitter', 'http://twitter.com/gonz4lex_'),)
TYPOGRIFY = True
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

# COLOR_SCHEME_CSS = 'monokai.css'

# AUTHORS_BIO = {
#   "Alex Gonzalez": {
#     "name": "Alex Gonzalez",
#     "cover": "images/great-wave-off-kinosawa.jpg",
#     "image": "images/last-night.jpg",
#     "website": "http://alexgonzalez.dev",
#     "location": "Terra",
#     "bio": "This is my 200 character biography. Hello!"
#   }
# }
AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

ARTICLE_PATHS = ['posts',]
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

AUTHOR_PATHS = ['author',]
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%m'
NEWEST_FIRST_ARCHIVES = True
GITHUB_URL = 'http://github.com/gonz4lex'
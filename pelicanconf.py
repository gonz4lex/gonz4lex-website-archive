#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Gonzalez'
SITENAME = 'Alex Gonzalez'
TAGLINE = "Hey! I'm Alex, a developer specialising on machine learning, data science, engineering, visualization and analytics."
# SITEURL = 'https://alexgonzalezc.dev'
SITEURL = 'http://127.0.0.1:8000'
THEME = 'svbhack'
LOAD_CONTENT_CACHE = True

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Github', 'http://github.com/gonz4lex'),
#          ('Python.org', 'http://python.org/'),
#          )

# Social widget
SOCIAL = (
    ('Github', 'http://github.com/gonz4lex'),
    # ('Twitter', 'http://twitter.com/gonz4lex_'),
)


TYPOGRIFY = True
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Blog setup
USER_LOGO_URL = SITEURL + 'static/images/logo.png'

STATIC_PATHS = ['images', 'extra', 'assets']
HEADER_COVER = "images/last-night.jpg"


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
EMAIL = "hello@alexgonzalezc.dev"
LINKEDIN_URL = "https://www.linkedin.com/in/alejandro-gonzalez-a05636127/"

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
DISPLAY_PAGES_ON_MENU = True
GOOGLE_ANALYTICS = "UA-155317378-1"

import logging
LOG_FILTER = [(logging.WARN, 'Cannot get modification stamp')]
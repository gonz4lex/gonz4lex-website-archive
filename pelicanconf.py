#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import time
import os


AUTHOR = 'Alex Gonzalez'
SITENAME = 'Alex Gonzalez'
TAGLINE = "Hey! I'm Alex, a developer specialising on machine learning, data science, engineering, visualization and analytics."
SITEURL = 'alexgonzalezc.dev'

PATH = 'content'
THEME = './themes/svbhack'
LOAD_CONTENT_CACHE = False
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}
TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'http://github.com/gonz4lex'
EMAIL = "hello@alexgonzalezc.dev"
LINKEDIN_URL = "https://www.linkedin.com/in/alejandro-gonzalez-a05636127/"

# # Blogroll
# LINKS = (('Github', 'http://github.com/gonz4lex'),
#          )

# Social widget
SOCIAL = (
    ('Github', GITHUB_URL),
    ('LinkedIn', LINKEDIN_URL),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USER_LOGO_URL = SITEURL + '/images/avatar.png'

STATIC_PATHS = ['images', 'extra', 'assets']

ARTICLE_PATHS = ['posts',]
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%m'
NEWEST_FIRST_ARCHIVES = False

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
DISPLAY_PAGES_ON_MENU = True

GOOGLE_ANALYTICS = "UA-155317378-1"

import logging
LOG_FILTER = [(logging.WARN, 'Cannot get modification stamp')]

MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.admonition'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight','guess_lang': 'False', 'linenums': 'True'},
    },
    'output_format': 'html5',
}

GISCUS_ENABLED = True
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'qDot'
SITENAME = 'buttplug.io'
SITEURL = 'https://buttplug.io'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

THEME = "themes/buttplug"

# Feed generation is usually not desired when developing
# FEED_ATOM = ('atom.xml')
# FEED_RSS = ('index.xml')
# CATEGORY_FEED_ATOM = None
# FEED_ALL_ATOM = None
# FEED_DOMAIN = SITEURL
# TRANSLATION_FEED = None
# FEED_MAX_ITEMS = 10

# Relative to content dir
PAGE_PATHS = ['hardware/', 'pages/']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_PATHS = ['posts']
# ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
# CATEGORY_URL = 'blog/category/{slug}/index.html'
# TAG_URL = 'blog/tag/{slug}/index.html'
# TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
# AUTHOR_SAVE_AS = False
# INDEX_SAVE_AS = 'blog/index.html'
DIRECT_TEMPLATES = ['index']

# DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
# YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['summary', 'neighbors', ]

# SUMMARY_END_MARKER = "<!--more-->"
# SUMMARY_MAX_LENGTH = None

STATIC_PATHS = ['extras/htaccess',
                'extras/robots.txt',
                'images']

EXTRA_PATH_METADATA = {
    'extras/htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

EXTRA_TEMPLATES_PATHS = ['content/templates']

TEMPLATE_PAGES = {'templates/index.html': "index.html",
                  'templates/github.html': "github.html",
                  'templates/404.html': "404/index.html"}

# MENUITEMS = (('bio', '/about'),
#              ('blog', '/'),
#              ('portfolio', '/portfolio'))
# #             ('config', '/config'))

SITELOGO = "theme/images/buttplug.logo.png"
SITELOGOSVG = "theme/images/buttplug.logo.svg"
SITELOGO_SIZE = "35px"
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
SHOW_ARTICLE_CATEGORY = False

PIWIK_URL = "apps.nonpolynomial.com/piwik"
PIWIK_SITE_ID = "5"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'video': {},
    },
    'output_format': 'html5',
}

TWITTER_CARDS = True
USE_OPEN_GRAPH = True
TWITTER_USERNAME = "buttplugio"
OPEN_GRAPH_IMAGE = "images/header-opengraph.jpg"

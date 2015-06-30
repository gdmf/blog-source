#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Grant Miller-Francisco'
SITENAME = u'Grant Miller-Francisco'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Github', 'http://github.com/gdmf'),
#         ('email', 'mailto:g.millfran@gmail.com'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/gdmf'),
          ('email', 'mailto:g.millfran@gmail.com'),)

DEFAULT_PAGINATION = 10
THEME = 'pelican-themes/pelican-svbhack'
SITEURL = 'http://gdmf.github.io'

USER_LOGO_URL = SITEURL + '/images/gdmf.png'
TAGLINE = 'spatial | python | javascript'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#DELETE_OUTPUT_DIRECTORY = FALSE

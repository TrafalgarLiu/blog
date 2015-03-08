#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'luffyliu'
SITENAME = u"Luffyliu's blog"
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
iDEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

DEFAULT_LANG = u'zh_cn'
#Theme
JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]
THEME = '/home/luffy/project/blog/pelican-theme/niu-x2-sidebar'

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

#disqus comment
DISQUS_SITENAME = 'luffyliu'
SITEURL = "http://blog.luffyliu.com"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False 

#other conf copy ohter
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

#NIUX2-THEME-SETTING
NIUX2_PYGMENTS_THEME = 'borland'

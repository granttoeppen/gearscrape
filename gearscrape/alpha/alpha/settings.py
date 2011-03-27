# Scrapy settings for alpha project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'alpha'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['alpha.spiders']
NEWSPIDER_MODULE = 'alpha.spiders'
DEFAULT_ITEM_CLASS = 'alpha.items.AlphaItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


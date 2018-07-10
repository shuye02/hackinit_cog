# -*- coding: utf-8 -*-
import os

### App config ###

## These variables must be set as env variables ##

# Postgres SQL Connection String.
# Note: This is the default env variable name
# used for Heroku postgres deploys.
DB_URI = os.environ['DATABASE_URL'] 

# URL of Quill instance (for auth integration)
QUILL_URL = os.environ['QUILL'] 

# Random Secret for JWTs - must match Quill secret
SECRET = os.environ['SECRET']


### The following variables may all be set using environment
### variables of the same name. The environment variable will
### take precedence over the value shown here. This is to allow
### for deploy configuration without modifying the codebase at all.

## Deploy settings ##

# Enable/disable Flask debug mode. Should be set to
# False on production deploys of Cog.
DEBUG = True

# Ensure that all attempts to visit an insecure version
# of the page redirect to  https, and makes sure all
# Cog-derived redirects use https. Recommended to set
# this to True if using an SSL-protected deploy.
# Only works when DEBUG=False.
FORCE_SSL = False

## Metadata ##

HACKATHON_NAME = "Hack.init()"

## Event logistical settings ##

# If true, lets users to make requests even if
# item is out of stock
ENABLE_WAITLIST = True

# If True, requires hackers to submit a proposal
# for lotteried items
LOTTERY_REQUIRES_PROPOSAL = True

# If True, item type is set to CHECKOUT after an
# item's lottery is run
CLOSE_LOTTERY_WHEN_RUN = False

# If True, deny lottery requests that don't win
# item
DENY_LOTTERY_LOSERS = True

# Character limit for lottery proposals
# Set to 0 to disable char limit
LOTTERY_CHAR_LIMIT = 140

# If True, display current lottery item stock to user
DISPLAY_LOTTERY_QUANTITY = True

# If True, display current checkout item stock to user
DISPLAY_CHECKOUT_QUANTITY = True

# If False, prevent users from submitting multiple
# requests for same lottery item
LOTTERY_MULTIPLE_SUBMISSIONS = False

# The info text underneath the 'Lottery Required' section
LOTTERY_TEXT = u"""由于这些物品数量有限，需要通过抽签获取。请填写一份简要的计划，描述你在项目中使用这些物品的想法，我们将在Hackathon开始30分钟后随机通过尽可能多的请求。"""

# The info text underneath the 'Checkout Required' section
CHECKOUT_TEXT = u"""点击以请求这些物品。你的请求将在物品可用时被通过。在物品被归还之前，我们将要求通过某种ID来记录物品状态。"""

# The info text underneath the 'No Checkout Required' section
FREE_TEXT = u"""你可以直接到Hardware Desk请求以下物品！"""

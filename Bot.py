import praw
import logging
from datetime import datetime
import pytz
from requests import Session
import time

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


r1 = reddit.redditor('str1kebeam')
r2 = reddit.redditor('sidewind864')

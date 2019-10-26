from auth import Authorization
import praw
import logging
from datetime import datetime
import pytz
from requests import Session
import json
import time

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


reddit = praw.Reddit(client_id='acrtj7jRqKQlSw',
                     client_secret='3dOyTX5ijxMYhgca02T32Ptt-y0',
                     user_agent='<console:new_bot:0.0.1 (by /u/str1kebeam)>',
                     username='str1kebeam',
                     password='stg90shredder')
r1 = reddit.redditor('str1kebeam')
r2 = reddit.redditor('sidewind864')

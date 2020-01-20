from auth import Authorization
import praw
import logging
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pytz
import math
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

r1 = reddit.redditor('mrcatisgod')
r2 = reddit.redditor('str1kebeam')

r1_karma = r1.link_karma + r1.comment_karma
r2_karma = r2.link_karma + r2.comment_karma

r1_link = r1.link_karma
r1_comment = r1.comment_karma
r2_link = r2.link_karma
r2_comment = r2.comment_karma

r1_submission_breakdown = {}
r1_comment_counts = {}
r1_post_counts = {}
r1_submission_subs = []
r1_comment_subs = []
r1_comment_breakdown = {}
#karma_values = []
'''
for s in r1.submissions.new(limit=None):
    if s.subreddit.display_name in r1_submission_breakdown.keys():
        r1_submission_breakdown[s.subreddit.display_name] += s.score
        r1_post_counts[s.subreddit.display_name] += 1
    else:
        r1_submission_breakdown[s.subreddit.display_name] = s.score
        r1_post_counts[s.subreddit.display_name] = 1
        r1_submission_subs.append(s.subreddit.display_name)



for c in r1.comments.new(limit=None):
    if c.subreddit.display_name in r1_comment_breakdown.keys():
        r1_comment_breakdown[c.subreddit.display_name] += c.score
        r1_comment_counts[c.subreddit.display_name] += 1
    else:
       r1_comment_breakdown[c.subreddit.display_name] = c.score
       r1_comment_counts[c.subreddit.display_name] = 1
       r1_comment_subs.append(c.subreddit.display_name)
    #karma_values.append(c.score)



r1_top_comment = [c for c in r1.comments.top(limit=1)][0]
r1_top_submission = [c for c in r1.submissions.top(limit=1)][0]

r2_submission_breakdown = {}
r2_comment_counts = {}
r2_post_counts = {}
r2_submission_subs = []
r2_comment_subs = []
r2_comment_breakdown = {}
#karma_values = []

for s in r2.submissions.new(limit=None):
    if s.subreddit.display_name in r2_submission_breakdown.keys():
        r2_submission_breakdown[s.subreddit.display_name] += s.score
        r2_post_counts[s.subreddit.display_name] += 1
    else:
        r2_submission_breakdown[s.subreddit.display_name] = s.score
        r2_post_counts[s.subreddit.display_name] = 1
        r2_submission_subs.append(s.subreddit.display_name)



for c in r2.comments.new(limit=None):
    if c.subreddit.display_name in r2_comment_breakdown.keys():
        r2_comment_breakdown[c.subreddit.display_name] += c.score
        r2_comment_counts[c.subreddit.display_name] += 1
    else:
       r2_comment_breakdown[c.subreddit.display_name] = c.score
       r2_comment_counts[c.subreddit.display_name] = 1
       r2_comment_subs.append(c.subreddit.display_name)
    #karma_values.append(c.score)



r2_top_comment = [c for c in r2.comments.top(limit=1)][0]
r2_top_submission = [c for c in r2.submissions.top(limit=1)][0]



def toEST(utc):
    utc_dt = datetime.strptime(utc, '%Y%m%d %H:%M:%S.%f')
    nyt_dt = utc_dt.replace(tzinfo=pytz.timezone('utc')).astimezone(tz = pytz.timezone('America/New_York'))
    return datetime.strftime(nyt_dt, '%H:%M:%S %m/%d/%Y')

print(toEST(datetime.fromtimestamp(int(r1.created_utc)).strftime('%Y%m%d %H:%M:%S.%f')))
print(toEST(datetime.fromtimestamp(int(r2.created_utc)).strftime('%Y%m%d %H:%M:%S.%f')))
'''

#Originally supposed show a histogram of comment karma for user, but
#I didn't realize that most redditors have an inconsistent comment
#history with most comments under 20 karma, along with outliers
#giving a heavily skewed histogram. Oh well.

'''
data = np.array(karma_values)
bins = np.linspace(math.ceil(min(data)),
                   math.floor(max(data)),
                   30)
plt.xlim([min(data)-5, max(data)+5])
plt.hist(data, bins=bins, alpha=0.5)
plt.show()
'''

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


class RedditStatistics:

    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def karma_1(self):
        r1_karma = {"total_karma": self.r1.link_karma + self.r1.comment_karma, "r1_link": self.r1.link_karma,
                    "r1_comment": self.r1.comment_karma}
        return r1_karma

    def karma_2(self):
        r2_karma = {"total_karma": self.r2.link_karma + self.r2.comment_karma, "r1_link": self.r2.link_karma,
                    "r1_comment": self.r2.comment_karma}
        return r2_karma

    def r1_submission_karma(self):
        r1_submission_breakdown = {}
        r1_post_counts = {}
        r1_submission_subs = []
        for s in self.r1.submissions.new(limit=None):
            if s.subreddit.display_name in r1_submission_breakdown.keys():
                r1_submission_breakdown[s.subreddit.display_name] += s.score
                r1_post_counts[s.subreddit.display_name] += 1
            else:
                r1_submission_breakdown[s.subreddit.display_name] = s.score
                r1_post_counts[s.subreddit.display_name] = 1
                r1_submission_subs.append(s.subreddit.display_name)
        return r1_submission_breakdown

    def r1_comment_karma(self):
        r1_comment_counts = {}
        r1_comment_subs = []
        r1_comment_breakdown = {}
        for c in self.r1.comments.new(limit=None):
            if c.subreddit.display_name in r1_comment_breakdown.keys():
                r1_comment_breakdown[c.subreddit.display_name] += c.score
                r1_comment_counts[c.subreddit.display_name] += 1
            else:
                r1_comment_breakdown[c.subreddit.display_name] = c.score
                r1_comment_counts[c.subreddit.display_name] = 1
                r1_comment_subs.append(c.subreddit.display_name)

    def r2_submission_karma(self):
        r2_submission_breakdown = {}
        r2_post_counts = {}
        r2_submission_subs = []
        for s in self.r2.submissions.new(limit=None):
            if s.subreddit.display_name in r2_submission_breakdown.keys():
                r2_submission_breakdown[s.subreddit.display_name] += s.score
                r2_post_counts[s.subreddit.display_name] += 1
            else:
                r2_submission_breakdown[s.subreddit.display_name] = s.score
                r2_post_counts[s.subreddit.display_name] = 1
                r2_submission_subs.append(s.subreddit.display_name)
        return r2_submission_breakdown

    def r2_comment_karma(self):
        r2_comment_counts = {}
        r2_comment_subs = []
        r2_comment_breakdown = {}
        for c in self.r2.comments.new(limit=None):
            if c.subreddit.display_name in r2_comment_breakdown.keys():
                r2_comment_breakdown[c.subreddit.display_name] += c.score
                r2_comment_counts[c.subreddit.display_name] += 1
            else:
                r2_comment_breakdown[c.subreddit.display_name] = c.score
                r2_comment_counts[c.subreddit.display_name] = 1
                r2_comment_subs.append(c.subreddit.display_name)

r2_top_comment = [c for c in r2.comments.top(limit=1)][0]
r2_top_submission = [c for c in r2.submissions.top(limit=1)][0]
def toEST(utc):
    utc_dt = datetime.strptime(utc, '%Y%m%d %H:%M:%S.%f')
    nyt_dt = utc_dt.replace(tzinfo=pytz.timezone('utc')).astimezone(tz = pytz.timezone('America/New_York'))
    return datetime.strftime(nyt_dt, '%H:%M:%S %m/%d/%Y')
print(toEST(datetime.fromtimestamp(int(r1.created_utc)).strftime('%Y%m%d %H:%M:%S.%f')))
print(toEST(datetime.fromtimestamp(int(r2.created_utc)).strftime('%Y%m%d %H:%M:%S.%f')))
'''

# Originally supposed show a histogram of comment karma for user, but
# I didn't realize that most redditors have an inconsistent comment
# history with most comments under 20 karma, along with outliers
# giving a heavily skewed histogram. Oh well.

'''
'''
data = np.array(karma_values)
bins = np.linspace(math.ceil(min(data)),
                   math.floor(max(data)),
                   30)
plt.xlim([min(data)-5, max(data)+5])
plt.hist(data, bins=bins, alpha=0.5)
plt.show()
'''


import praw
import logging
from datetime import datetime

import pytz
import math
from requests import Session
import json
import time

def toEST(utc):
    utc_dt = datetime.strptime(utc, '%Y%m%d %H:%M:%S.%f')
    nyt_dt = utc_dt.replace(tzinfo=pytz.timezone('utc')).astimezone(tz = pytz.timezone('America/New_York'))
    return datetime.strftime(nyt_dt, '%m/%d/%Y %H:%M:%S')

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
        self.r1 = reddit.redditor(r1)
        self.r2 = reddit.redditor(r2)

    def karma_1(self):
        r1_karma = {"total_karma": self.r1.link_karma + self.r1.comment_karma, "r1_link": self.r1.link_karma,
                    "r1_comment": self.r1.comment_karma}
        return r1_karma

    def karma_2(self):
        r2_karma = {"total_karma": self.r2.link_karma + self.r2.comment_karma, "r2_link": self.r2.link_karma,
                    "r2_comment": self.r2.comment_karma}
        return r2_karma

    def submission_karma(self):
        submission_breakdown = {}
        post_counts = {}
        for s in self.r1.submissions.new(limit=None):
            if s.subreddit.display_name in submission_breakdown.keys():
                submission_breakdown[s.subreddit.display_name][0] += s.score
                post_counts[s.subreddit.display_name][0] += 1
            else:
                submission_breakdown[s.subreddit.display_name] = [0,0]
                submission_breakdown[s.subreddit.display_name][0] = s.score
                post_counts[s.subreddit.display_name] = [0, 0]
                post_counts[s.subreddit.display_name][0] = 1
        for s in self.r2.submissions.new(limit=None):
            if s.subreddit.display_name in submission_breakdown.keys():
                submission_breakdown[s.subreddit.display_name][1] += s.score
                post_counts[s.subreddit.display_name][1] += 1
            else:
                submission_breakdown[s.subreddit.display_name] = [0,0]
                submission_breakdown[s.subreddit.display_name][1] = s.score
                post_counts[s.subreddit.display_name] = [0,0]
                post_counts[s.subreddit.display_name][1] = 1
        return [submission_breakdown, post_counts]

    def comment_karma(self):
        comment_breakdown = {}
        comment_counts = {}
        for s in self.r1.comments.new(limit=None):
            if s.subreddit.display_name in comment_breakdown.keys():
                comment_breakdown[s.subreddit.display_name][0] += s.score
                comment_counts[s.subreddit.display_name][0] += 1
            else:
                comment_breakdown[s.subreddit.display_name] = [0, 0]
                comment_breakdown[s.subreddit.display_name][0] = s.score
                comment_counts[s.subreddit.display_name] = [0, 0]
                comment_counts[s.subreddit.display_name][0] = 1
        for s in self.r2.comments.new(limit=None):
            if s.subreddit.display_name in comment_breakdown.keys():
                comment_breakdown[s.subreddit.display_name][1] += s.score
                comment_counts[s.subreddit.display_name][1] += 1
            else:
                comment_breakdown[s.subreddit.display_name] = [0, 0]
                comment_breakdown[s.subreddit.display_name][1] = s.score
                comment_counts[s.subreddit.display_name] = [0, 0]
                comment_counts[s.subreddit.display_name][1] = 1
        return [comment_breakdown, comment_counts]
    def top_reddit(self):
        r1_top_comment = [c for c in self.r1.comments.top(limit=1)][0]
        r1_top_submission = [s for s in self.r1.submissions.top(limit=1)][0]
        r2_top_comment = [c for c in self.r2.comments.top(limit=1)][0]
        r2_top_submission = [s for s in self.r2.submissions.top(limit=1)][0]
        return {"r1_comment": r1_top_comment, "r1_sub": r1_top_submission, "r2_comment": r2_top_comment, "r2_submission": r2_top_submission}
    def time_stamps(self):
        r1_cake = toEST(datetime.fromtimestamp(int(self.r1.created_utc)).strftime('%Y%m%d %H:%M:%S.%f'))
        r2_cake = toEST(datetime.fromtimestamp(int(self.r2.created_utc)).strftime('%Y%m%d %H:%M:%S.%f'))
        delta_1 = datetime.now() - datetime.fromtimestamp(int(self.r1.created_utc))
        print(delta_1.days)
        delta_2 = datetime.now() - datetime.fromtimestamp(int(self.r2.created_utc))
        print(delta_2.days)
        print(r1_cake)
        print(r2_cake)



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


import praw
import logging
from datetime import datetime

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

    def __init__(self, r1, r2, tz):
        self.tz = tz;
        self.r1 = reddit.redditor(r1)
        self.r2 = reddit.redditor(r2)

    def karma(self):
        return {"total": {"total_karma": [self.r1.link_karma + self.r1.comment_karma, self.r2.link_karma + self.r2.comment_karma]},
                "link": {"link_karma": [self.r1.link_karma, self.r2.link_karma]},
                "comment": {"comment_karma": [self.r1.comment_karma, self.r2.comment_karma]}}

    def submission_karma(self):
        submission_breakdown = {}
        submission_counts = {}
        for s in self.r1.submissions.new(limit=None):
            if s.subreddit.display_name in submission_breakdown.keys():
                submission_breakdown[s.subreddit.display_name][0] += s.score
                submission_counts[s.subreddit.display_name][0] += 1
            else:
                submission_breakdown[s.subreddit.display_name] = [0,0]
                submission_breakdown[s.subreddit.display_name][0] = s.score
                submission_counts[s.subreddit.display_name] = [0, 0]
                submission_counts[s.subreddit.display_name][0] = 1
        for s in self.r2.submissions.new(limit=None):
            if s.subreddit.display_name in submission_breakdown.keys():
                submission_breakdown[s.subreddit.display_name][1] += s.score
                submission_counts[s.subreddit.display_name][1] += 1
            else:
                submission_breakdown[s.subreddit.display_name] = [0,0]
                submission_breakdown[s.subreddit.display_name][1] = s.score
                submission_counts[s.subreddit.display_name] = [0,0]
                submission_counts[s.subreddit.display_name][1] = 1
        return {"submission_breakdown": submission_breakdown, "submission_counts": submission_counts}

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
        return {"comment_breakdown": comment_breakdown, "comment_counts": comment_counts}

    def top_reddit(self):
        link_start = "www.reddit.com"
        r1_top_comment = link_start + str([c for c in self.r1.comments.top(limit=1)][0].permalink)
        r1_top_submission = link_start + str([s for s in self.r1.submissions.top(limit=1)][0].permalink)
        r2_top_comment = link_start + str([c for c in self.r2.comments.top(limit=1)][0].permalink)
        r2_top_submission = link_start + str([s for s in self.r2.submissions.top(limit=1)][0].permalink)
        return {"comment": {"top_comment": [r1_top_comment, r2_top_comment]},
                "submission": {"top_submission": [r1_top_submission, r2_top_submission]}}

    def changeTZ(self, utc):
        new_dt = utc.replace(tzinfo=pytz.timezone('utc')).astimezone(tz=pytz.timezone(self.tz))
        return datetime.strftime(new_dt, '%m/%d/%Y %H:%M:%S')

    def time_stamps(self):
        r1_cake = self.changeTZ(datetime.fromtimestamp(int(self.r1.created_utc)))
        r2_cake = self.changeTZ(datetime.fromtimestamp(int(self.r2.created_utc)))
        delta_r1 = str((datetime.utcnow() - datetime.fromtimestamp(int(self.r1.created_utc))).days)
        delta_r2 = str((datetime.utcnow() - datetime.fromtimestamp(int(self.r2.created_utc))).days)
        return {"cake": {"cake_day": [r1_cake, r2_cake]},
                "delta": {"uptime": [delta_r1, delta_r2]}}

    def reddit_merge(self):
        return {**{"user_1": self.r1.name, "user_2": self.r2.name},**self.karma(), **self.submission_karma(), **self.comment_karma(), **self.top_reddit(), **self.time_stamps()}

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

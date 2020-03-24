import praw
import json
import pandas as pd
reddit = praw.Reddit(user_agent='risi',
                     client_id='****', client_secret="****",
                     username='risi1001', password='****')

subreddit = reddit.subreddit('coronavirus')
# top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=10)
# for submission in subreddit.top(limit=1):
#     print(submission.title, submission.id)
topics_dict = { "title":[],"score":[], "id":[], "url":[],"comms_num": [],"created": [],"body":[]}
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

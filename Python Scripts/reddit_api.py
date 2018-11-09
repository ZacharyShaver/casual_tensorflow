import praw
import random

random.seed()
reddit = praw.Reddit(
    client_id = 'YYMdlwpb-5JHBg',
    client_secret = 'CJQmIaS3eA16qBe6JguS0HBLv9I',
    username = 'nicki_bot',         #trash account for testing take it if you want it
    password = 'nickiistweet',
    user_agent = 'ainthetweet'
)
subreddit = reddit.subreddit('aww')
niki = ['https://imgur.com/a/8NOy3TK', 'https://imgur.com/a/WCJhNZJ', 'https://imgur.com/a/VX11gy7', 'https://imgur.com/a/sGUimwm', 'https://imgur.com/a/zXIkDHJ', 'https://imgur.com/a/84JLrWX']
new_posts = subreddit.new(limit=10)

for comment in subreddit.stream.comments():
    if 'nicki' in comment.body and '---->' not in comment.body:
        print('we got a live one')
        comment.reply(str('You know who else is named nicki? ----> ' + random.choice(niki) + ' aint he tweet!'))
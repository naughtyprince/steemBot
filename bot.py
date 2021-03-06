from piston import Steem
import os
import json

steemPostingKey = os.environ.get('steemPostingKey')
steemAccountName = os.environ.get('steemAccountName')

steem = Steem(wif=steemPostingKey)
authors = ["krish3732","pikachuu"]
for post in steem.stream_comments():
   if  post["author"] in authors:
       post.upvote(voter="steemAccountName")





'''
"""
This bot randomly upvotes posts
It upvotes a random post from the most recent [numPostsToConsider]
"""
import sys
import datetime
import os
import subprocess
from piston.steem import Steem
from random import randint
# extra
import time
from piston.post import Post
import os
import json



# grab config vars
percentChanceToPost = int(os.environ.get('percentChanceToPost'))
numPostsToConsider = int(os.environ.get('numPostsToConsider'))
voteWeight = int(os.environ.get('voteWeight'))
steemPostingKey = os.environ.get('steemPostingKey')
steemAccountName = os.environ.get('steemAccountName')

print ("steem Posting Key " + steemPostingKey)


steem = Steem(wif=steemPostingKey)
tags = ["postoftheday", "introduceyourself", "introducemyself"]
past_authors = []

for p in steem.stream_comments():
    for x in tags:
        try:
            if x in p["tags"] and p.is_opening_post() and p["author"] not in past_authors:
                print(p.get_comments())
                print(p["author"])
                post = p.reply(body = "I am Groot!", author = steemAccountName)
                p.upvote(weight=+0.01, voter = steemAccountName)
                print(post)
                past_authors.append(post['operations'][0][1]['parent_author'])
                time.sleep(25)
                print(past_authors)

        except:
            print("Failed to comment on post.")



# [percentChanceToPost] chance to proceed past this block
i = randint(1, 100)
if i > percentChanceToPost:
    print('[{:%Y-%m-%d, %H:%M:%S}] No action (failed random roll {}>{})\n'.format(datetime.datetime.now(), i, percentChanceToPost))
    sys.exit(1)

# initialize steem object
steem = Steem(wif=steemPostingKey)

# use piston to set default voter and author
subprocess.call(['piston', 'set', 'default_voter', steemAccountName])
subprocess.call(['piston', 'set', 'default_author', steemAccountName])

# upvote random post from the most recent [numPostsToConsider]
posts = steem.get_posts(limit=numPostsToConsider, sort='created')
postId = randint(0, numPostsToConsider-1)

try:
    steem.vote(posts[postId]["identifier"], voteWeight)
except:
    print('[{:%Y-%m-%d, %H:%M:%S}] Vote failed: {}\n'.format(datetime.datetime.now(), sys.exc_info()[0]))
else:
    print('[{:%Y-%m-%d, %H:%M:%S}] Vote succeeded: {}\n'.format(datetime.datetime.now(), posts[postId]["identifier"]))   
'''

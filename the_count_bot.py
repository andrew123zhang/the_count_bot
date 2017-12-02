import praw
import os
import time

#FUCKCKCKCKCKCKCKCKCCKCKCKCCKCKCKCK
#FUCKFUCKFUCKFUKCFUCKFUCKFUKUFCUFKCUFUC

bot = praw.Reddit(user_agent="The Count Bot",
                  client_id="R2Cow3Sq7SvGXA",
                  client_secret="B9zd_3-30EX4mloVEoQAKOf43ZI",
                  username="thecountbot",
                  password=input("Type the password for thecountbot: "))

subreddit = bot.subreddit("testingground4bots")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
while True:
    for submission in subreddit.hot(limit=6):
        if submission.id not in posts_replied_to:
            text = submission.selftext
            thes = text.lower().split(" ").count("the")
            submission.reply("Hi. I am a bot. (Zaz) You wrote the word \"the\" {0} times version4".format(thes))
            with open("posts_replied_to.txt", "a") as f:
                f.write("\n{0}".format(submission.id))
            posts_replied_to.append(submission.id)
    time.sleep(1)

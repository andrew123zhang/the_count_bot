import praw
import os
import time

password = input("Type the password:")

bot = praw.Reddit(
	user_agent="The Count Bot",
	client_id="R2Cow3Sq7SvGXA",
	client_secret="B9zd_3-30EX4mloVEoQAKOf43ZI",
	username="thecountbot",
	password=password
)

subreddit = bot.subreddit("testingground4bots")

if not os.path.isfile("replies.txt"):
	replies = []
else:
	with open("replies.txt", "r") as f:
		replies = list(filter(None, f.read().split("\n")))

while True:
	for submission in subreddit.hot(limit=10):
		if submission.id not in replies:
			text = submission.selftext
			thes = text.lower().split(" ").count("the")
			submission.reply("Hi. I am a bot (J). You wrote the word \"the\" {0} times".format(thes))
			with open("replies.txt", "a") as f:
				f.write("\n{0}".format(submission.id))
			replies.append(submission.id)
		time.sleep(1)
	time.sleep(1)



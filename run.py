from main import reddit_bot
import praw

r = praw.Reddit(user_agent="test_bot_xena",
                    username="test_bot_xena",
                    password="Quailk777!!!",
                    client_id="whlMP0C9rsqDsg",
                    client_secret="UXgHQPC4fUYPcaHCz3MgkByt0G4lvg",
                    )

while True:
    reddit_bot.run_bot(r)
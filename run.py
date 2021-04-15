import praw
from main import reddit_bot


r = praw.Reddit(user_agent="test_bot_xena",
                username="test_bot_xena",
                password="Quailk777!!!",
                client_id="whlMP0C9rsqDsg",
                client_secret="UXgHQPC4fUYPcaHCz3MgkByt0G4lvg",
                )

while True:
    # reddit_bot.babble(r)
    # reddit_bot.delete_comments(r)
    # reddit_bot.pokemon_link(r)
    # reddit_bot.summon_bot(r)
    reddit_bot.parse_subreddit(r)
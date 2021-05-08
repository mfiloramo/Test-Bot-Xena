import praw
from main import reddit_bot
from main import config


r = praw.Reddit(user_agent=config.user_agent,
                username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                )

while True:
    # reddit_bot.babble(r)
    # reddit_bot.delete_comments(r)
    # reddit_bot.pokemon_link(r)
    # reddit_bot.summon_bot(r)
    reddit_bot.scrape_subreddit(r)

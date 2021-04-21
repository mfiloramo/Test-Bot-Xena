import praw
import config


class RedditBot:
    """An instance of a Reddit bot."""

    def __init__(self):
        """Initialize an instance of a Reddit bot and log in with agent/user credentials."""
        self.login = \
            praw.Reddit(user_agent=config.user_agent,
                        username=config.username,
                        password=config.password,
                        client_id=config.client_id,
                        client_secret=config.client_secret,
                        )
        print('Logged in.')

    def scrape_subreddit(self):
        """Scrapes and prints all comments and comment replies in all posts within a subreddit."""
        subreddit = self.login.subreddit('learnpython')
        print('Running...')
        while True:
            for submission in subreddit.new(limit=10):
                print(f"{submission.title}\n\n")
                for comment in submission.comments:
                    print(f"{comment.body}\n")
                    for reply in comment.replies:
                        print(f"\t{reply.body}\n")



if __name__ == '__main__':
    RedditBot().scrape_subreddit()

import praw
import config


class RedditBot:
    """An instance of a Reddit bot."""

    def __init__(self, user_agent, username, password, client_id, client_secret):
        """Initialize an instance of a Reddit bot with correct login credentials."""
        self.user_agent = user_agent
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

    def login(self):
        """Logs into Reddit via PRAW."""
        reddit = praw.Reddit(user_agent=self.user_agent,
                             username=self.username,
                             password=self.password,
                             client_id=self.client_id,
                             client_secret=self.client_secret,
                             )
        print("Logged in.")
        return reddit

    def scrape_subreddit(self):
        """Scrapes and prints all comments and comment replies in all posts within a subreddit."""
        subreddit = self.login().subreddit('learnpython')
        print('Running...')
        while True:
            for submission in subreddit.new(limit=10):
                print(f"{submission.title}\n\n")
                for comment in submission.comments:
                    print(f"{comment.body}\n")
                    for reply in comment.replies:
                        print(f"\t{reply.body}\n")


run_bot = RedditBot(config.user_agent, config.username, config.password,
                    config.client_id, config.client_secret)

if __name__ == '__main__':
    run_bot.scrape_subreddit()

import praw
from main import config


def login():
    r = praw.Reddit(user_agent=config.user_agent,
                    username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    )
    print("Logged in.")
    return r


def run_bot(r):
    """Looks at comments within own submission and automatically responds to user."""
    submission = r.submission(url="https://www.reddit.com/user/test_bot_xena/comments/mm4oqz/im_a_bot_testing/")
    all_comments = submission.comments.list()
    logged_posts = []
    # with open('log.txt', 'r+') as log_file:
    #     opened_file = log_file.readlines()
    #     for line in opened_file:
    #         logged_posts.append(line.rstrip())
    for comment in all_comments:
        # if comment.author == "Calif0rnia_Soul" and comment not in logged_posts:
        if "!summon" in comment.body and comment not in logged_posts:
            # log_file.write(f"{comment}\n")
            logged_posts.append(f"{comment}\n")
            print("New comment detected. Responding...")
            comment.reply("Beep boop. I'm a bot in the making!\n\n"
                          "*This action was performed automatically.*")


def delete_comments(r):
    """Deletes all the bot's comments from itself."""
    submission = r.submission(id="mm4oqz")
    all_comments = submission.comments.list()
    for comment in all_comments:
        if comment.author == "test_bot_xena":
            print("Deleting comments...")
            comment.delete()


reddit = login()

print("Running...")

while True:
    run_bot(reddit)
    # delete_comments(reddit)



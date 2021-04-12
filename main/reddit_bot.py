import praw
from main import config
from modules import random_sentences_gen
from modules import rand_items
import random


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
    # with open('log.txt', 'r+') as log_file:
    #     opened_file = log_file.readlines()
    #     for line in opened_file:
    #         logged_posts.append(line.rstrip())
    for comment in all_comments:
        word_count = 0
        word_limit = random.randint(4, 12)
        sentence = ""

        while word_count < word_limit:
            sentence += random.choice([random.choice(rand_items.conjunctions).lower(),
                                       random.choice(rand_items.words)]).lower() + str(" ")
            word_count += 1

        if word_count == word_limit:
            sentence += random.choice([random.choice(rand_items.conjunctions).lower(),
                                       random.choice(rand_items.words)]).lower()

        # random_sentence = f"{random_sentences_gen.sentence.rstrip(' ').capitalize()}"
        #                    f"{random.choice(rand_items.punctuation)}"
        # if comment.author == "Calif0rnia_Soul" and comment not in logged_posts:
        if "!summon" in comment.body and comment not in cache:
            # log_file.write(f"{comment}\n")
            cache.append(f"{comment}")
            print("New comment detected. Responding...")
            comment.reply(f"{sentence.capitalize()}\n\n"
                          "*Beep boop. I'm a bot in the making!*\n"
                          "*This action was performed automatically.*")


def delete_comments(r):
    """Deletes all the bot's comments from itself."""
    submission = r.submission(id="mm4oqz")
    all_comments = submission.comments.list()
    for comment in all_comments:
        if comment.author == "test_bot_xena":
            print("Deleting comments...")
            comment.delete()


cache = []

reddit = login()

print("Running...")

while True:
    run_bot(reddit)
    # delete_comments(reddit)



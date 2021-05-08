import praw
import config
import time
import random
import re
from modules import rand_items


class RedditBot:
    """A model of a Reddit bot."""

    def __init__(self):
        """Initializes an instance of a Reddit bot and logs in with agent/user credentials."""
        self.login = praw.Reddit(user_agent=config.user_agent,
                                 username=config.username,
                                 password=config.password,
                                 client_id=config.client_id,
                                 client_secret=config.client_secret,
                                 )
        print('Logged in.')

    def scrape_subreddit(self):
        """Scrapes and prints all comments and comment replies in all posts within a subreddit."""
        subreddit = self.login.subreddit('learnpython')
        for submission in subreddit.new(limit=10):
            print(f"{submission.title}\n\n")
            for comment in submission.comments:
                print(f"{comment.body}\n")
                for reply in comment.replies:
                    print(f"\t{reply.body}\n")

    def summon_bot(self):
        """Looks at comments within own submission and automatically responds to user."""
        # Points the bot at a particular submission.
        submission = self.login.submission(id="mpk3s5")
        all_comments = submission.comments.list()
        detect_words = ('!Summon', '!summon', 'Xena', 'xena')

        # Waits to be summoned upon command and replies to the comment.
        for comment in all_comments:
            for word in detect_words:
                if word in comment.body and comment.author not in \
                 (None, 'test_bot_xena') and comment not in cache:
                    print("New comment detected. Responding...")
                    cache.append(comment)
                    comment.reply(f"I have been summoned.\n\n"
                                  "*Beep boop. I'm a prototype bot in the making!*\n"
                                  "*This action was performed automatically.*")

                    # Regulate the speed of the bot's activity.
                    # time.sleep(1)

    def log_track(self):
        """
        Keeps track of posts in a separate text file when run from a local machine.
        Currently cannot be actively managed/used on a cloud server.
        """
        # Points the bot at a particular submission.
        submission = self.login.submission(id="mpk3s5")
        all_comments = submission.comments.list()

        for comment in all_comments:
            if comment.author not in [None, 'test_bot_xena'] and comment not in log_file:
                with open('log.txt', 'r+') as log_file:
                    opened_file = log_file.readlines()
                    for line in opened_file:
                        log_file.write(line.rstrip())

    def babble(self):
        """Generate random sentences for each unlogged comment once bot is summoned."""
        # Points the bot at a particular submission.
        submission = self.login.submission(id="mpk3s5")
        all_comments = submission.comments.list()

        key_words = ['babble', 'blabber', 'gibberish', 'jargon', 'rant', 'ranting', 'ranted', 'random',
                     'drone', 'arbitrary', 'aimless', 'weird', 'unusual']

        def _make_sentence():
            sentence = ''
            word_count = 0
            word_limit = random.randint(3, 12)
            punctuation = random.choice(rand_items.punctuation)
            while word_count < word_limit:
                conjunction = random.choice(rand_items.conjunctions).lower()
                word = random.choice(rand_items.words).lower()
                sentence += f"{random.choice([conjunction, word])} "
                word_count += 1
            sentence = f"{sentence.capitalize().strip()}{punctuation}"
            return sentence

        # while True:
        for comment in all_comments:
            sentence = _make_sentence()
            if comment.author not in (None, 'test_bot_xena') and comment not in cache\
                    and comment.author == 'Calif0rnia_Soul':
                for word in comment.body.split():
                    if (word.lower() or word.capitalize()) in key_words:
                        print("New comment detected. Responding...")
                        comment.reply(f"Hello. I see that you mentioned '{word.lower()}.' I can do that "
                                      f"in sentence form!\n\n"
                                      f"{sentence}\n\n"
                                      "*Beep boop. I'm a prototype bot in the making!*\n"
                                      "*This action was performed automatically.*")
                        cache.append(comment)

    def pokemon_link(self):
        """Generates a link to a Pokemon if any are mentioned."""
        # Points the bot at a particular submission.
        submission = self.login.submission(id="mpk3s5")
        all_comments = submission.comments.list()

        # You can use Regex to compile this list into a Match object and ues re.IGNORECASE to make it so any
        # case spelling will be detected by the bot.

        pokemon_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle',
                        'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill',
                        'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans',
                        'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran♀', 'Nidorina', 'Nidoqueen',
                        'Nidoran♂', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff',
                        'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat',
                        'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey',
                        'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra',
                        'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel',
                        'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro',
                        'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk',
                        'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby',
                        'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee',
                        'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela',
                        'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime',
                        'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras',
                        'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto',
                        'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno,' 'Zapdos', 'Moltres', 'Dratini', 'Dragonair',
                        'Dragonite', 'Mewtwo', 'Mew', 'Tentacool',
                        ]
        try:
            for comment in all_comments:
                if comment not in cache and comment.author is not None and comment.author != "test_bot_xena":
                    for word in comment.body.split():
                        if word.lower() in pokemon_list or word.capitalize() in pokemon_list:
                            pokemon = word.capitalize()
                            cache.append(comment)
                            print("New comment detected. Responding...")
                            comment.reply(f"I see that you mentioned {pokemon}. You can learn more about "
                                          f"{pokemon} [here](https://www.pokemon.com/us/pokedex/{word.lower()}).\n\n"
                                          "*Beep boop. I'm a prototype bot in the making!*\n"
                                          "*This action was performed automatically.*")

                            # Regulate the speed of the bot's activity.
                            time.sleep(120)
                            continue
        except AttributeError:
            pass

    def auto_respond(self):
        """Continually scrapes a subreddit and replies to specified user."""
        subreddit = self.login.subreddit("mpk3s5")
        while True:
            for submission in subreddit.new(limit=10):
                for comment in submission.comments:
                    if comment.author == 'Calif0rnia_Soul' and comment not in cache:
                        print("New comment detected. Responding...")
                        comment.reply(f'Hi there, {comment.author}. I am your bot.\n\n'
                                      '*Beep boop. I\'m a prototype bot in the making!*\n'
                                      '*This action was performed automatically.*')
                        cache.append(comment)

                        # Regulate the speed of the bot's activity.
                        time.sleep(10)

    def delete_comments(self):
        """Deletes all the bot's comments from itself."""
        # Points the bot at a particular submission.
        submission = self.login.submission(id="mpk3s5")
        all_comments = submission.comments.list()

        # Identifies and removes own comments.
        while True:
            for comment in all_comments:
                if comment.author == "test_bot_xena" and comment.author is not None:
                    print("Deleting comment...")
                    comment.delete()


# Set up empty cache for bot usage (typically for tracking posts).
cache = []

# Create an instance of the bot.
run_bot = RedditBot()

# Run the bot.
if __name__ == '__main__':
    print('Running...')
    while True:
        run_bot.scrape_subreddit()

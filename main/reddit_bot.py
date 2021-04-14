import time

import praw
from main import config
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


def summon_bot(r):
    """Looks at comments within own submission and automatically responds to user."""
    # Points the bot at a particular submission.
    submission = r.submission(id="mpk3s5")
    all_comments = submission.comments.list()

    # Waits to be summoned upon command and replies to the comment.
    for comment in all_comments:
        if "!summon" in comment.body or "xena" in comment.body and comment.author is not None and comment not in cache:
                print("New comment detected. Responding...")
                comment.reply("I have been summoned.")
                cache.append(comment)


def log_track(r):
    """
    Keeps track of posts in a separate text file when run from a local machine.
    # Currently cannot be actively managed/used on a cloud server.
    """
    # Points the bot at a particular submission.
    submission = r.submission(id="mpk3s5")
    all_comments = submission.comments.list()

    for comment in all_comments:
        # Currently has no particular condition for responses.
        if comment.author is not None and comment not in log_file:
            with open('log.txt', 'r+') as log_file:
                opened_file = log_file.readlines()
                for line in opened_file:
                    log_file.write(line.rstrip())


def babble(r):
    """Generate random sentences for each unlogged comment once bot is summoned."""
    # Points the bot at a particular submission.
    submission = r.submission(id="mpk3s5")
    all_comments = submission.comments.list()

    key_words = ['babble', 'blabber', 'gibberish', 'jargon', 'rant', 'ranting', 'ranted', 'random',
                 'drone', 'arbitrary', 'aimless', 'weird', 'unusual']

    # Forms the babble sentences each time per comment.
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

        try:
            for comment in all_comments:
                if comment not in cache and comment.author is not None and comment.author != "test_bot_xena":
                    for word in comment.body.split():
                        if word.lower() in key_words or word.capitalize() in key_words:

                            cache.append(f"{comment}")
                            print("New comment detected. Responding...")
                            comment.reply(f"Hello. I see that you mentioned '{word.lower()}.' I can do that "
                                          f"in sentence form!\n\n"
                                          f"{sentence.capitalize()}{random.choice(rand_items.punctuation)}\n\n"
                                          "*Beep boop. I'm a prototype bot in the making!*\n"
                                          "*This action was performed automatically.*")
                            time.sleep(10)
        except AttributeError:
            pass


def pokemon_link(r):
    """Generates a link to a Pokemon if any are mentioned."""
    # Points the bot at a particular submission.
    submission = r.submission(id="mpk4qo")
    all_comments = submission.comments.list()

    pokemon_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle',
                    'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill',
                    'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans',
                    'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran♀', 'Nidorina', 'Nidoqueen',
                    'Nidoran♂', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff',
                    'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat',
                    'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape',
                    'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam',
                    'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool',
                    'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro',
                    'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk',
                    'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby',
                    'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee',
                    'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela',
                    'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime',
                    'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras',
                    'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto',
                    'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno,' 'Zapdos', 'Moltres', 'Dratini', 'Dragonair',
                    'Dragonite', 'Mewtwo', 'Mew']
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
                        time.sleep(120)
                        continue
    except AttributeError:
        pass


def delete_comments(r):
    """Deletes all the bot's comments from itself."""
    # Points the bot at a particular submission.
    submission = r.submission(id="mpk3s5")
    all_comments = submission.comments.list()

    # Identifies and removes own comments.
    try:
        for comment in all_comments:
            if comment.author == "test_bot_xena" and comment.author is not None:
                print("Deleting comments...")
                comment.delete()
    except AttributeError:
        pass


# Log into the Reddit using the user agent.
reddit = login()

# Set up empty cache for bot usage (typically for tracking posts).
cache = []

# Notify user that bot is running.
print("Running...")




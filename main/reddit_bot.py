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


def run_bot(r):
    """Looks at comments within own submission and automatically responds to user."""
    submission = r.submission(url="https://www.reddit.com/user/test_bot_xena/comments/mpk3s5/test_post_2/")
    all_comments = submission.comments.list()
    pokemon_list = ['bulbasaur', 'ivysaur']

    # with open('log.txt', 'r+') as log_file:
    #     opened_file = log_file.readlines()
    #     for line in opened_file:
    #         logged_posts.append(line.rstrip())


def babble(r):
    """Generate random sentences for each unlogged comment once bot is summoned."""
    submission = r.submission(url="https://www.reddit.com/user/test_bot_xena/comments/mpk3s5/test_post_2/")
    all_comments = submission.comments.list()
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

        # Reply to a comment once the bot is summoned and the comment ID is unlogged.
        if "!summon" in comment.body and comment not in cache:
            # log_file.write(f"{comment}\n")
            cache.append(f"{comment}")
            print("New comment detected. Responding...")
            comment.reply(f"{sentence.capitalize()}{random.choice(rand_items.punctuation)}\n"
                          "*Beep boop. I'm a bot in the making!*\n"
                          "*This action was performed automatically.*")


def pokemon_link(r):
    """Generates a link to a Pokemon if any are mentioned."""
    submission = r.submission(id="mpk3s5")
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
                                      "*Beep boop. I'm a bot in the making!*\n"
                                      "*This action was performed automatically.*")
    except AttributeError:
        pass


def delete_comments(r):
    """Deletes all the bot's comments from itself."""
    # Directs bot to own test submission.
    submission = r.submission(id="mpk3s5")

    # Identifies and removes own comments.
    all_comments = submission.comments.list()
    # try:
    for comment in all_comments:
        if comment.author == "test_bot_xena":
            print("Deleting comments...")
            comment.delete()
    # except AttributeError:
    #     pass

# Set up empty cache for run_bot usage.
cache = []

# Log into the Reddit using the user agent.
reddit = login()

# Notify user that bot is running.
print("Running...")




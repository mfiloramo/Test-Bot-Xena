import random
from modules import rand_items

word_count = 0
word_limit = random.randint(4, 12)
sentence = ""

while word_count <= word_limit:
    sentence += random.choice([random.choice(rand_items.conjunctions).lower(),
                               random.choice(rand_items.words)]).lower() + str(" ")
    word_count += 1


#  Here, I use multiple methods at once for the first time! I stripped the space
#  that came at the end (because the last word choice would also add a space),
#  and also capitalized the first letter of the string. Then, I added a random
#  punctuation mark from the rand_items module I created.

rand_sentence = f"{sentence.rstrip(' ').capitalize()}{random.choice(rand_items.punctuation)}"
#  This module can be used to generate various random values.

import random

conjunctions = ['A minute later', 'Accordingly', 'Actually', 'After',
                'After a short time', 'Afterwards', 'Also', 'And', 'Another',
                'As an example', 'As a consequence', 'As a result', 'As soon as',
                'At last', 'At length', 'Because', 'Because of this', 'Before',
                'Besides', 'Briefly', 'But', 'Consequently', 'Conversely', 'Equally important',
                'Finally', 'First', 'For example', 'For instance', 'For this purpose',
                'For this reason', 'Fourth', 'From here on', 'Further', 'Furthermore',
                'Gradually', 'Hence', 'However', 'In addition', 'In conclusion', 'In contrast',
                'In fact', 'In short', 'In spite of', 'In spite of this', 'In summary',
                'In the end', 'In the meanwhile', 'In the meantime', 'In the same manner',
                'In the same way', 'Just as important', 'Least', 'Last', 'Last of all',
                'Lastly', 'Later', 'Meanwhile', 'Moreover', 'Nevertheless', 'Next',
                'Nonetheless', 'Now', 'Nor', 'Of equal importance', 'On the contrary',
                'On the following day', 'On the other hand', 'Other hand', 'Or', 'Presently',
                'Second', 'Similarly', 'Since', 'So', 'Soon', 'Still', 'Subsequently',
                'Such as', 'The next week', 'Then', 'Thereafter', 'Therefore', 'Third',
                'Thus', 'To be specific', 'To begin with', 'To illustrate', 'To repeat',
                'To sum up', 'Too', 'Ultimately', 'What', 'Whatever', 'Whoever', 'Whereas',
                'Whomever', 'When', 'While', 'With this in mind', 'Yet']

words = ['cellar', 'bike', 'race', 'unlikely', 'guess',
         'repeat', 'inflation', 'monstrous', 'formulate',
         'talk', 'aunt', 'mistreat', 'cause', 'urine',
         'belong', 'fate', 'kid', 'wreck', 'carrot', 'inhabitant',
         'warning', 'concede', 'reduce', 'quality', 'patrol',
         'bible', 'bacon', 'item', 'black', 'miner', 'step']

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+=-"
punctuation = [".", "!", "?", "...", "!?"]

ran_character = random.choice(str([letters, numbers, symbols]))
ran_conjunct = random.choice(conjunctions)
ran_noun = random.choice(words)

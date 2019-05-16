import random

def generate_next_word(prev):
    if prev == 'A':
        return random.choice(['B','B','B','B','C'])
    elif prev == 'B':
        return random.choice(['C','C','C','C','D'])
    elif prev == 'C':
        return random.choice(['D','D','D','D','E'])
    elif prev == 'D':
        return random.choice(['A','A','A','E','E'])

def generate_sent():
    words = ['A']
    while words[-1] != 'E':
        words.append(generate_next_word(words[-1]))
    return ' '.join(words)
    
with open('abcd/ptb.test.txt', 'w') as outhandle:
    for i in range(1000):
        outhandle.write(generate_sent())
        outhandle.write('\n')
    
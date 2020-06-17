import json
import os
import re

FOLDER = 'data/full'


def load_reuters():
    json_files = sorted([j for j in os.listdir(FOLDER) if j[-5:] == '.json'])

    docs = []
    for j in json_files:
        with open(FOLDER + '/' + j, 'r') as f:
            docs += json.load(f)

    return docs


def update(dct, update):
    dct.update(update)
    return dct


def count_words(text):
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
    return len(text.split(' '))


def count_paragraphs(text):
    text = re.sub(' +', ' ', text)
    text = re.sub('(\n )+', '\n', text)
    text = re.sub('(\n)+', '\n', text)
    return len(text.split('\n'))


def load_enhance_reuters():
    docs = load_reuters()
    docs = [d for d in docs if 'body' in d.keys()]
    docs = [update(d, {'characters_count': len(d['body'])}) for d in docs]
    docs = [update(d, {'words_count': count_words(d['body'])}) for d in docs]
    docs = [update(d, {'paragraphs_count': count_paragraphs(d['body'])}) for d
            in docs]
    return docs


x = [d for d in load_enhance_reuters() if d['paragraphs_count'] > 10]

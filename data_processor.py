from imdb import imdb
import shelve
import random 
import os

actors = list()

def create_entry(actor, date, title, role):
    # create a dictionary for each row in imdb file
    entry = {'actor': actor,'title': title,'data': date,'role': role}
    # append this dictionary to our list
    actors.append(entry)

# call create_entry for every row in imdb file
imdb.process_file('data/actors.list.gz', create_entry)

# remove the database if already exists
try:
    os.remove('data/actors.db')
except OSError:
    pass

# create a new shelve database
s = shelve.open('data/actors.db')

# pick only n random entries from the imdb data
n = 15
indexes_to_save = random.sample(range(0,len(actors)-1), n)

# save these picked entries to the database
try:
    for i in indexes_to_save:
        s[str(i)] = actors[i]
finally:
    s.close()
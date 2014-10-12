#!/usr/bin/python

import argparse
import sqlite3

############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('dbPath', help = 'Path to Firefox places.sqlite file.', metavar = 'places-sqlite-path')

opt = parser.parse_args()

conn = sqlite3.connect(opt.dbPath)
conn.row_factory = sqlite3.Row
curs = conn.cursor()

curs.execute("select id from moz_bookmarks")

# Record the built-in root folder with ID 0
ids = [ 0 ]

for row in curs:
    ids.append(row['id'])

curs.execute("select id, parent, title from moz_bookmarks")

entriesWithoutValidParent = []

for row in curs:
    if row['parent'] not in ids:
        entriesWithoutValidParent.append(row)
        
conn.close()    

print "Database %s contains:" % opt.dbPath        
print "Entries: %s" % (len(ids) - 1)
print "Entries without valid parent: %s" % len(entriesWithoutValidParent)
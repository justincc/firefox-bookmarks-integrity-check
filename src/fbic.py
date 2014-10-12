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

ids = []

for row in curs:
    ids.append(row["id"])
    
print "Database %s contains %s items" % (opt.dbPath, len(ids))
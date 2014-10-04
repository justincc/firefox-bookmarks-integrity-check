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
curs = conn.cursor()

curs.execute("select id from moz_bookmarks")

rows = curs.fetchall()

ids = []

for row in rows:
    ids.append(row[0])
    
print "Database %s contains %s items" % (opt.dbPath, len(ids))
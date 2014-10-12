#!/usr/bin/python

import argparse
import sqlite3

def check(dbPath):
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    
    curs.execute("select id from moz_bookmarks")
    
    # Record the built-in root folder with ID 0
    ids = [ 0 ]
    
    for row in curs:
        ids.append(row['id'])
    
    curs.execute("select id, parent, title from moz_bookmarks")
    
    invalidParentEntries = []
    
    for row in curs:
        if row['parent'] not in ids:
            invalidParentEntries.append(row)
            
    conn.close()
    
    return { 'entries' : len(ids) - 1, 'invalidParentEntries' : len(invalidParentEntries) }
    
############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('dbPath', help = 'Path to Firefox places.sqlite file.', metavar = 'places-sqlite-path')

opt = parser.parse_args()

results = check(opt.dbPath)
    
print "Database %s contains:" % opt.dbPath        
print "Entries: %s" % results['entries']
print "Entries without valid parent: %s" % results['invalidParentEntries']
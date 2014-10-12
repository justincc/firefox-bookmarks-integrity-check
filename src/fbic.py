#!/usr/bin/python

import argparse
import fbic.checker
import sqlite3
    
############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('dbPath', help = 'Path to Firefox places.sqlite file.', metavar = 'places-sqlite-path')

opt = parser.parse_args()

conn = sqlite3.connect(opt.dbPath)
conn.row_factory = sqlite3.Row

results = fbic.checker.check(conn)
    
print "Database %s contains:" % opt.dbPath        
print "Entries: %s" % (results.entries - 1)
print "Entries without valid parent: %s" % results.invalidParentEntries
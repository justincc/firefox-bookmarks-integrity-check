#!/usr/bin/python

import argparse
import fbic.checker
    
def yeck():
    print "YEK"
    
############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('dbPath', help = 'Path to Firefox places.sqlite file.', metavar = 'places-sqlite-path')

opt = parser.parse_args()

results = fbic.checker.check(opt.dbPath)
    
print "Database %s contains:" % opt.dbPath        
print "Entries: %s" % results['entries']
print "Entries without valid parent: %s" % results['invalidParentEntries']
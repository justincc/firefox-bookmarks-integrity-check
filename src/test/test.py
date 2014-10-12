#!/usr/bin/python
import os.path
import sqlite3
import sys
import unittest

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import fbic.checker as checker

class FbicTests(unittest.TestCase):
    def testGoodAndBadParents(self):
        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row
        conn.execute('create table moz_bookmarks (id value, parent value, title text)')
        conn.execute('insert into moz_bookmarks values ("1", "0", "bookmark1")')
        conn.execute('insert into moz_bookmarks values ("2", "1", "bookmark2")')
        conn.execute('insert into moz_bookmarks values ("3", "999", "bookmark3")')
        conn.commit()
        
        res = checker.check(conn)
        self.assertEqual(res.entries, 3)
        self.assertEqual(res.invalidParentEntries, 1)
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
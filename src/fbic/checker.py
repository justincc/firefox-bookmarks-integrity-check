def check(conn):    
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
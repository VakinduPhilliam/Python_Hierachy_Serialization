# Python object serialization
# The 'pickle' module implements binary protocols for serializing and de-serializing 
# a Python object structure. 
# �Pickling� is the process whereby a Python object hierarchy is converted into a byte stream, 
# and �unpickling� is the inverse operation, whereby a byte stream (from a binary file or bytes-like 
# object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as �serialization�, �marshalling,� or �flattening�; 
# however, to avoid confusion, the terms used here are �pickling� and �unpickling�.
# sqlite3 � DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn�t require a separate 
# server process and allows accessing the database using a nonstandard variant of the SQL query language. 
# Some applications can use SQLite for internal data storage. 
# It�s also possible to prototype an application using SQLite and then port the code to a larger database 
# such as PostgreSQL or Oracle.
# iterdump() 
# Returns an iterator to dump the database in an SQL text format. Useful when saving an in-memory 
# database for later restoration. 
# This function provides the same capabilities as the .dump command in the sqlite3 shell.
# Convert file existing_db.db to SQL dump file dump.sql

import sqlite3

con = sqlite3.connect('existing_db.db')

with open('dump.sql', 'w') as f:

    for line in con.iterdump():
        f.write('%s\n' % line)

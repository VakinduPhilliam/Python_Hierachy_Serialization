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
# Registering an adapter callable.
# The other possibility is to create a function that converts the type to the string representation and 
# register the function with register_adapter().
 
import sqlite3

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return "%f;%f" % (point.x, point.y)

sqlite3.register_adapter(Point, adapt_point)

con = sqlite3.connect(":memory:")
cur = con.cursor()

p = Point(4.0, -3.2)
cur.execute("select ?", (p,))

print(cur.fetchone()[0])

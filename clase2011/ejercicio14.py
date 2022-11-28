import sqlite3


con=sqlite3.connect("test.db")

statement=con.cursor()


statement.execute("CREATE TABLE PERSONA(nombre,dni)")
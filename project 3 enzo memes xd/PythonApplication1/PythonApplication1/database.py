import psycopg2

database = psycopg2.connect("dbname=Jaar 1 Project 3 user=VUL MIJ IN")
cursor = database.cursor()
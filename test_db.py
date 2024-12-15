import pandas as pd
import psycopg2


connection = psycopg2.connect(database='pc-repair',
                              user='user',
                              password='1234',
                              host='localhost',
                              port='5432')

cursor = connection.cursor()
print(connection.get_dsn_parameters(), '\n')
cursor.execute("SELECT version();")
version_ps = cursor.fetchone()
print("Вы подключены - ", version_ps, "\n")
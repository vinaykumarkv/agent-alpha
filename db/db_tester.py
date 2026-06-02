import sqlite3

# 1. Connect to an in-memory database for testing
connection = sqlite3.connect('audit.db')
cursor = connection.cursor()

# 2. Create a test table and insert data
cursor.execute('''
    SELECT * FROM events ORDER BY timestamp DESC
''')

results = cursor.fetchall()

# 4. Print the results
print("Events in the database:")
for row in results:
    print(row)

# 5. Clean up and close the connection
cursor.close()
connection.close()

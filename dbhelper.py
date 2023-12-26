import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="my_project")
            self.mycursor = self.conn.cursor()
            print("Connected to the database.")
        except Exception as e:
            print("Some error occurred while connecting to the database:", e)

    def register(self, name, email, password):
        try:
            query = "INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, %s, %s, %s)"
            values = (name, email, password)
            self.mycursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print("Error during registration:", e)
            return -1  # Registration failed
        else:
            return 1   # Registration successful

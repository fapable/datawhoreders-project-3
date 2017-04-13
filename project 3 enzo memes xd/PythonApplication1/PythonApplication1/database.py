import psycopg2

class Database:  
     def interact_with_database(command):
        connection = psycopg2.connect(host = "localhost", dbname = "Project 3", user = "postgres", password = "61hhsjmercedes")
        cursor = connection.cursor()

        # Execute the command
        cursor.execute(command)
        connection.commit()

        # Save results
        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            # Nothing to fetch
            pass

        # Close connection
        cursor.close()
        connection.close()

        return results

def get_data(result, tabel, jaar, wijk):
   return Database.interact_with_database("SELECT " + str(result) + " FROM " + str(tabel) + " WHERE jaar = " + str(jaar) + " AND wijk = " + str(wijk))[0][0]
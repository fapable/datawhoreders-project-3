import psycopg2

class Database:  
    def interact_with_database(command):
        connection = psycopg2.connect(host = "localhost", dbname = "Jaar 1 Project 3", user = "postgres", password = "breadcrumb1")
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

    def get_crime_data(result, jaar, wijk):
        return Database.interact_with_database("SELECT " + str(result) + " FROM criminaliteit WHERE jaar = " + str(jaar) + " AND wijk = " + str(wijk))[0][0]

    def politie_coordinaten():
        return Database.interact_with_database("SELECT X, Y FROM politiebureaus")
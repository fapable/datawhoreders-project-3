import psycopg2
  
def interact_with_database(command):
    connection = psycopg2.connect(host = "localhost", dbname = "Jaar 1 Project 3", user = "postgres", password = "DatThaBeast3636")

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

def get_data(tabel, jaar, wijk, result):
    return interact_with_database("SELECT " + str(result) + " FROM " + str(tabel) + "\nWHERE jaar = " + str(jaar) + "AND wijk = " + str(wijk))[0][0]
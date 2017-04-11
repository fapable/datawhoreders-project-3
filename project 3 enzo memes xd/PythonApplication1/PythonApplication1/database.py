import psycopg2

def interact_with_database(command):
    connection = psycopg2.connect(" host = localhost dbname= Project 3 user= postgres password = 61hhsjmercedes")

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

def C_prins_alexander_2009():
    return interact_with_database("SELECT * FROM c_prins_alexander_2009")

def C_prins_alexander_2011():
    return interact_with_database("SELECT * FROM c_prins_alexander_2011")

def C_delfshaven_2009():
    return interact_with_database("SELECT * FROM c_delfshaven_2009")

def C_delfshaven_2011():
    return interact_with_database("SELECT * FROM c_delfshaven_2011")

def C_feijenoord_2009():
    return interact_with_database("SELECT * FROM c_feijenoord_2009")

def C_feijenoord_2011():
    return interact_with_database("SELECT * FROM c_feijenoord_2011")

def C_charlois_2009():
    return interact_with_database("SELECT * FROM c_charlois_2009")

def C_charlois_2011():
    return interact_with_database("SELECT * FROM c_charlois_2011")

def C_hillegersberg_schiebroek_2009():
    return interact_with_database("SELECT * FROM c_hillegersberg_schiebroek_2009")

def C_hillegersberg_schiebroek_2011():
    return interact_with_database("SELECT * FROM c_hillegersberg_schiebroek_2011")

def C_ijsselmonde_2009():
    return interact_with_database("SELECT * FROM c_ijsselmonde_2009")

def C_ijsselmonde_2011():
    return interact_with_database("SELECT * FROM c_ijsselmonde_2011")

def C_kralingen_crooswijk_2009():
    return interact_with_database("SELECT * FROM c_kralingen_crooswijk_2009")

def C_kralingen_crooswijk_2011():
    return interact_with_database("SELECT * FROM c_kralingen_crooswijk_2011")

def C_noord_2009():
    return interact_with_database("SELECT * FROM c_noord_2009")

def C_noord_2011():
    return interact_with_database("SELECT * FROM c_noord_2011")

def C_overschie_2009():
    return interact_with_database("SELECT * FROM c_overschie_2009")

def C_overschie_2011():
    return interact_with_database("SELECT * FROM c_overschie_2011")

D_overschie_2009 = C_overschie_2009()

if D_overschie_2009 >= 10:
    result = polygon("blue",(904,194,947,183,955,205,1106,109,1176,199,1222,163,1242,185,1237,355,1109,432,1138,471,1057,479,1017,403,1059,350,1050,345,1003,366,964,322,949,342))
    print(result)
else:
    pass

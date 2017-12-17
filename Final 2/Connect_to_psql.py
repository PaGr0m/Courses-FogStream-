import psycopg2 as db


def connect_to_database():
    """
    Establishing a connection to the database
    :return: connect -> connection
             cur -> cursor
    """

    DBNAME = "GitHub"
    USER = "postgres"
    HOST = "localhost"
    PASSWORD = "postgres"

    try:
        connect = db.connect("dbname={} user={} host={} password={}"
                             .format(DBNAME, USER, HOST, PASSWORD))
    except db.Error:
        print("I am unable to connect to the database")
        exit()

    cur = connect.cursor()

    return connect, cur
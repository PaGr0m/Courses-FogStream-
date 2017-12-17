import psycopg2 as db


def connect_to_database():
    """
    Устанавливается соединение с БД
    :return: connect -> соединение
             cur -> курсор
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
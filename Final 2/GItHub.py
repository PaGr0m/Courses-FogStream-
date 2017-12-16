import psycopg2 as db
import urllib.request
import json
import datetime


def connect_to_database():
    DBNAME = "GitHub"
    USER = "postgres"
    HOST = "localhost"
    PASSWORD = "postgres"

    global connect
    global cur

    try:
        connect = db.connect("dbname={} user={} host={} password={}"
                             .format(DBNAME, USER, HOST, PASSWORD))
    except: #прописать исключение
        print("I am unable to connect to the database")

    cur = connect.cursor()


def insert_to_users(cur, connect, object):
    cur.execute("""
        INSERT INTO Users
        (Login, URL, Repositories)
        VALUES ('{}', '{}', '{}')""".format(object["login"],
                                            object["url"],
                                            object["repos_url"]))
    connect.commit()


def insert_to_repositories(cur, connect, object):
    cur.execute("""
        INSERT INTO Repositories
        (Full_name, Name, Tag, Star, Update_time, Login_user, Tags_url)
        VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}')
        """.format(object["full_name"],
                   object["name"],
                   object["language"],
                   object["stargazers_count"],
                   object["updated_at"],
                   object["owner"]["login"],
                   object["languages_url"]))
    connect.commit()


def update_to_users(cur, connect, object, count):
    cur.execute("""UPDATE Users SET Count_of_repositories = {} 
                   WHERE Login = '{}'""".format(count, object["login"]))
    connect.commit()



def create_query(url):
    user_object = get_json_object(url)

    for user in user_object:
        count_repositories = 0
        insert_to_users(cur, connect, user)
        repos_object = get_json_object(user["repos_url"])

        for repository in repos_object:
            count_repositories += 1
            insert_to_repositories(cur, connect, repository)

        update_to_users(cur, connect, user, count_repositories)


def get_json_object(url):
    # прописать исключения"""urllib.request.RequestError:"""

    try:
        response = urllib.request.urlopen(url)
    except:
        print("Нет интернета!")
        exit()
    json_obj = json.loads(response.read().decode())

    return json_obj


def show_task_1(tag):
    cur.execute("""
        SELECT Full_name, Name, Tag
        FROM Repositories
        WHERE Tag = '{}'
        """.format(tag))

    connect.commit()
    show_data()


def show_task_3():
    cur.execute("""
        SELECT Tag, count(Full_name) 
        FROM Repositories
        GROUP BY Tag
        ORDER BY count(Full_name) DESC
        LIMIT 10
        """)
    connect.commit()
    show_data()


def show_task_4():
    cur.execute("""
        SELECT Login, Count_of_repositories 
        FROM Users
        ORDER BY Count_of_repositories DESC
    """)
    connect.commit()
    show_data()


def show_data():
    rows = cur.fetchall()

    print("\nShow me the databases:\n")
    for row in rows:
        print(row)


def main():
    URL_USERS = "https://api.github.com/users"
    connect_to_database()

    # case = input("Check number ")

    # if (case == "0"):
    #     create_query(URL_USERS)
    # elif (case == "1"):
    #     tag = input("Enter the tag ")
    #     show_task_1(tag)
    # elif (case == "3"):
    #     show_task_3()
    # elif(case == "4"):
    #     show_task_4()

    current_date = datetime.datetime.today()
    week_ago = current_date.replace(day=current_date.day-7)

    print(current_date)
    print(week_ago)


if __name__ == "__main__":
    main()

"""
исклчения psycopg2.IntegrityError: duplicate key value violates unique constraint "users_pkey"


"""
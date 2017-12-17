import psycopg2 as db
import urllib
# import urllib.request
import json
import datetime
import argparse


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
    except db.Error:
        print("I am unable to connect to the database")
        exit()

    cur = connect.cursor()


def insert_to_users(cur, connect, object):
    try:
        cur.execute("""
            INSERT INTO Users
            (Login, URL, Repositories)
            VALUES ('{}', '{}', '{}')""".format(object["login"],
                                                object["url"],
                                                object["repos_url"]))
        connect.commit()
    except db.Error:
        print("Database Users already exists")


def insert_to_repositories(cur, connect, object):
    try:
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
    except db.Error:
        print("Database Repositories already exists")


def update_to_users(cur, connect, object, count):
    try:
        cur.execute("""UPDATE Users SET Count_of_repositories = {} 
                       WHERE Login = '{}'""".format(count, object["login"]))
        connect.commit()
    except db.Error:
        print("Current transaction is aborted")


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
    try:
        response = urllib.request.urlopen(url)
    except urllib.request.URLError:
        print("Query limitted")
        exit()
    json_obj = json.loads(response.read().decode())

    return json_obj


def show_task_1(tag, time_1, time_2):
    cur.execute("""
        SELECT Full_name, Name, Tag
        FROM Repositories
        WHERE Tag = '{}' AND Update_time 
        BETWEEN '{}' AND '{}'
        """.format(tag, time_1, time_2))
    connect.commit()
    show_data()


def show_task_2(first_date, second_date):
    cur.execute("""
        SELECT Full_name, Star, Update_time 
        FROM Repositories
        WHERE update_time
        BETWEEN '{}' AND '{}'
        ORDER BY Star DESC
        """.format(first_date, second_date))
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
    print("Query result")
    for row in rows:
        print(row)


def create_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task")
    parser.add_argument("--tag")
    parser.add_argument("--add")
    parser.add_argument("--time1")
    parser.add_argument("--time2")

    return parser


def main():
    URL_USERS = "https://api.github.com/users"
    URL_USERS_2 = "https://api.github.com/users?page=2&per_page=70"
    connect_to_database()

    # case = input("Check number ")
    # if (case == "0"):
    #     create_query("https://api.github.com/users?since=200")


    parser = create_argparse()
    namespace = parser.parse_args()

    if namespace.task == "1":
        show_task_1(namespace.tag, namespace.time1, namespace.time2)

    elif namespace.task == "2":
        current_date = datetime.datetime.today()
        week_ago = current_date.replace(day=current_date.day - 7)
        show_task_2(week_ago, current_date)

    elif namespace.task == "3":
        show_task_3()

    elif namespace.task == "4":
        show_task_4()

    elif namespace.add == "add":
        create_query("https://api.github.com/users?since=135")



if __name__ == "__main__":
    main()

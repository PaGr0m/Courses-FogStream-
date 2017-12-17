from Connect_to_psql import connect_to_database
import psycopg2 as db
import urllib.request
import json


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
        print("Data was added")


def get_json_object(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.request.URLError:
        print("Query limitted")
        exit()
    json_obj = json.loads(response.read().decode())

    return json_obj


def main():
    global connect
    global cur

    connect, cur = connect_to_database()

    answer = input("Do you want add data ? (Y/N) ")

    if (answer == "Y" or answer == "y"):
        URL = "https://api.github.com/users?since=500"
        create_query(URL)


if __name__ == "__main__":
    main()
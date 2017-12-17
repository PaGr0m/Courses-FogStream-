from Connect_to_psql import connect_to_database
import psycopg2 as db
import urllib.request
import json


def insert_to_users(object):
    """
    Добавление данных в таблицу Users

    :param object: json объект, хранящий данные о пользователях
    :return: данные передаются в БД Postgresql
    """

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


def insert_to_repositories(object):
    """
    Добавление данных в таблицу Repositories

    :param object: json объект, хранящий данные о пользователях
    :return: данные передаются в БД Postgresql
    """

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


def update_to_users(object, count):
    """
    Обновление даных в таблице Users для поля Count_of_repositories

    :param object: json объект, хранящий данные о пользователях
    :param count: количество репозиториев
    :return: данные передаются в БД Postgresql
    """

    try:
        cur.execute("""UPDATE Users SET Count_of_repositories = {} 
                       WHERE Login = '{}'""".format(count, object["login"]))
        connect.commit()
    except db.Error:
        print("Current transaction is aborted")


def create_query(url):
    """
    Получение json объекта, создание запросов SQL

    :param url: url ссылка
    :return: данные передаются в БД Postgresql
    """

    user_object = get_json_object(url)

    for user in user_object:
        count_repositories = 0
        insert_to_users(user)
        repos_object = get_json_object(user["repos_url"])

        for repository in repos_object:
            count_repositories += 1
            insert_to_repositories(repository)

        update_to_users(user, count_repositories)
        print("Data was added")


def get_json_object(url):
    """
    Создание json оъекта по url ссылке
    :param url: url ссылка
    :return: объект формата json
    """

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
        URL = "https://api.github.com/users?since=800"
        create_query(URL)


if __name__ == "__main__":
    main()
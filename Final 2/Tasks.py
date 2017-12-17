import datetime
import argparse
from Connect_to_psql import connect_to_database


def task_1(tag, time_1, time_2):
    """
    Получаем список репозиториев по заданному хэш-тэгу
    в заданный период времени

    :param tag: хэш-тэг по которому происходит поиск
    :param time_1: левая граница временного диапазона
    :param time_2: правая граница временного диапазона
    :return: таблица с полями: полное имя, имя, хэш-тэг, время/дата
    """

    cur.execute("""
        SELECT Full_name, Name, Tag, Update_time
        FROM Repositories
        WHERE Tag = '{}' AND Update_time 
        BETWEEN '{}' AND '{}'
        """.format(tag, time_1, time_2))
    connect.commit()
    show_task_1()


def task_2(first_date, second_date):
    """
    Получаем список популярных репозиториев за неделю

    :param first_date: дата и время неделю назад
    :param second_date: текущая дата и время
    :return: таблица с полями: полное имя, количество звезд, время/дата
    """

    cur.execute("""
        SELECT Full_name, Star, Update_time 
        FROM Repositories
        WHERE update_time
        BETWEEN '{}' AND '{}'
        ORDER BY Star DESC
        """.format(first_date, second_date))
    connect.commit()
    show_task_2()


def task_3():
    """
    Получаем топ 10 популярных хэш-тэгов, т.е.
    те у которых больше всего репозиториев

    :return: таблица с полями: хэш-тэг, количество репозиториев
    """

    cur.execute("""
        SELECT Tag, count(Full_name) 
        FROM Repositories
        GROUP BY Tag
        ORDER BY count(Full_name) DESC
        LIMIT 10
        """)
    connect.commit()
    show_task_3()


def task_4():
    """
    Получаем список самых активных пользователей,
    те у которых больше всего репозиториев
    :return:
    """

    cur.execute("""
        SELECT Login, Count_of_repositories 
        FROM Users
        ORDER BY Count_of_repositories DESC
    """)
    connect.commit()
    show_task_4()


def show_task_1():
    """
    Вывод в таблицу результатов 1 задания
    :return: таблица
    """

    print("+" + "-"*40 + "+" + "-"*30 + "+" + "-"*15 + "+" + "-"*19 + "+")
    print("|{:>40}|{:>30}|{:>15}|{:>19}|".format("Full_name", "Name", "Tag", "Update_time"))
    print("+" + "-"*40 + "+" + "-"*30 + "+" + "-"*15 + "+" + "-"*19 + "+")

    rows = cur.fetchall()
    for full_name, name, tag, time in rows:
        print("|{:>40}|{:>30}|{:>15}|{}|".format(full_name, name, tag, time))

    print("+" + "-" * 40 + "+" + "-" * 30 + "+" + "-" * 15 + "+" + "-" * 19 + "+")


def show_task_2():
    """
    Вывод в таблицу результатов 2 задания
    :return: таблица
    """

    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")
    print("|{:>35}|{:>15}|{:>19}|".format("Full_name", "Star", "Update_time"))
    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")

    rows = cur.fetchall()
    for name, star, time in rows:
        print("|{:>35}|{:>15}|{}|".format(name, star, time))

    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")


def show_task_3():
    """
    Вывод в таблицу результатов 3 задания
    :return: таблица
    """

    print("+" + "-"*15 + "+" + "-"*15 + "+")
    print("|{:>15}|{:>15}|".format("Tag", "Count"))
    print("+" + "-" * 15 + "+" + "-" * 15 + "+")

    rows = cur.fetchall()
    for tag, count in rows:
        print("|{:>15}|{:>15}|".format(tag, count))

    print("+" + "-"*15 + "+" + "-"*15 + "+")


def show_task_4():
    """
    Вывод в таблицу результатов 4 задания
    :return: таблица
    """

    print("+" + "-"*35 + "+" + "-"*25 + "+")
    print("|{:>35}|{:>25}|".format("Login", "Count_of_repositories"))
    print("+" + "-"*35 + "+" + "-"*25 + "+")

    rows = cur.fetchall()
    for login, count in rows:
        print("|{:>35}|{:>25}|".format(login, count))

    print("+" + "-" * 35 + "+" + "-" * 25 + "+")


def create_argparse():
    """
    Создание парсера, добавление аргументов для скрипта
    :return: parser -> парсер аргументов (объект класса argparse)
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--task")
    parser.add_argument("--tag")
    parser.add_argument("--time1")
    parser.add_argument("--time2")

    return parser


def main():
    global connect
    global cur

    connect, cur = connect_to_database()
    parser = create_argparse()
    namespace = parser.parse_args()

    if namespace.task == "1":
        task_1(namespace.tag, namespace.time1, namespace.time2)
    elif namespace.task == "2":
        current_date = datetime.datetime.today()
        week_ago = current_date.replace(day=current_date.day - 7)
        task_2(week_ago, current_date)
    elif namespace.task == "3":
        task_3()
    elif namespace.task == "4":
        task_4()


if __name__ == "__main__":
    main()
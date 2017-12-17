import datetime
import argparse
from Connect_to_psql import connect_to_database


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



def show_data_3():
    rows = cur.fetchall()
    print("|{:>10}|{:>10}|".format("Tag", "Count"))
    for row in rows:
        # print(row)
        # print(type(row))
        for tag, count in row:
            print(tag)
            print(count)
            print("|{:>10}|{:>10}|".format(tag, count))
        # print(row)

def show_task_3():
    cur.execute("""
        SELECT Tag, count(Full_name) 
        FROM Repositories
        GROUP BY Tag
        ORDER BY count(Full_name) DESC
        LIMIT 10
        """)
    connect.commit()
    # show_data()
    show_data_3()

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
    global connect
    global cur

    connect, cur = connect_to_database()
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


if __name__ == "__main__":
    main()
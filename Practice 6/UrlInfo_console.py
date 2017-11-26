""" URL
http://www.recipepuppy.com/about/api/
задача: передаем список продуктов, получаем рецепты для этого списка продуктов

http://open-notify.org/Open-Notify-API/ISS-Location-Now/
задача: показать в какой точке мира находится МКС сейчас

https://api.football-data.org/index
задача: предоставить информацию о ТОП 5 популярных чемпионатов.
    Вывести по каждому чемпионату пять команд с наибольшим числом забитых голов

https://pokeapi.co/
задача: необходимо получить номер покемона и выдать краткую информацию о нем

Pavel Gromov
"""


import urllib3
import urllib3.request
import json


def get_json_object(url):
    """
    Запрос полного объекта типа json
    :param url: url ссылка
    :return: объект формата json, взятый с ссылки
    """

    http = urllib3.PoolManager()
    response = http.request("GET", url)
    json_obj = json.loads(bytes.decode(response.data))

    return json_obj


def get_recipe(url, ingredients):
    """
    Запрос рецепта по списку ингредиентов
    :param url: url ссылка
    :param ingredients: список ингредиентов
    :return: Название, ингредиенты и ссылки
    """

    json_obj = get_json_object("{}{}".format(url, ingredients))

    for recipe in json_obj["results"]:
        print("Title: {}\n"
              "href: {}\n"
              "ingredients: {}\n"
              "thumbnail: {}\n\n".format(recipe["title"], recipe["href"], recipe["ingredients"], recipe["thumbnail"]))


def get_station_coordinations(url):
    """
    Запрос координат МКС
    :param url: url ссылка
    :return: долгота и широта МКС
    """

    json_obj = get_json_object(url)
    latitude = json_obj["iss_position"]["latitude"]
    longitude = json_obj["iss_position"]["longitude"]

    print("At the moment the international space station is at:\n"
          "    latitude = {},\n"
          "    longitude = {}".format(latitude, longitude))


def get_football_team(url):
    """
    Запрос топ 5 команд по голам из следующих чемпионатов
    PL - Чемпионат Англии
    BL1 - Чемпионат Германии
    PD - Чемпионат Испании
    SA - Чемпионат Италии
    FL1 - Чемпионат Франции

    :param url: url ссылка
    :return: вывод информации о чемпионате и список команд
    """

    LEAGUE_LIST = ("PL", "BL1", "PD", "SA", "FL1")
    json_obj = get_json_object(url)

    for obj in json_obj:
        if obj["league"] in LEAGUE_LIST:
            print("Information about {0} league:\n"
                  "    ID: {1}\n"
                  "    Title: {2}\n"
                  "    Year: {3}\n"
                  "    Current tour: {4}\n"
                  "    Number of tours: {5}\n"
                  "    Number of teams: {6}\n"
                  "    Number of games: {7}\n".format(obj["league"],
                                                      obj["id"],
                                                      obj["caption"],
                                                      obj["year"],
                                                      obj["currentMatchday"],
                                                      obj["numberOfMatchdays"],
                                                      obj["numberOfTeams"],
                                                      obj["numberOfGames"]))
            json_table = get_json_object("{}/{}/leagueTable".format(url, obj["id"]))
            all_teams = {team["teamName"] : team["goals"] for team in json_table["standing"]}
            top_teams = sorted(all_teams.items(), key=lambda item: item[1], reverse=True)[:5]

            print("    Top 5 team:")
            count = 1
            for team, goals in top_teams:
                print("        {}. {} (goals: {})".format(count, team, goals))
                count += 1
            print("\n")


def get_pokemons(url):
    """
    Запрос на получение всех покемонов и вывод информации о них
    :param url: url ссылка
    :return:
    """

    json_obj = get_json_object(url)

    for pokemon in json_obj["results"]:
        json_pokemon = get_json_object(pokemon["url"])
        print("{}. {}\n"
              "    Weight: {}\n"
              "    Height: {}\n"
              "    Order: {}\n"
              "    Base experience: {}\n".format(json_pokemon["id"],
                                                 pokemon["name"],
                                                 json_pokemon["weight"],
                                                 json_pokemon["height"],
                                                 json_pokemon["order"],
                                                 json_pokemon["base_experience"]))

def output_menu():
    print("Menu:\n"
          "  1. Get recipes from the list of products.\n"
          "  2. Request the coordinates of the ISS.\n"
          "  3. Output the top 5 popular championships and five teams of each championship.\n"
          "  4. Output pokemon data.\n"
          "  0. Exit.\n")


def main():
    URL_ISS = "http://api.open-notify.org/iss-now.json"
    URL_RECIPE = "http://www.recipepuppy.com/api/?i="
    URL_FOOTBALL_TEAM = "http://api.football-data.org/v1/competitions"
    URL_POKEMONS = "https://pokeapi.co/api/v2/pokemon/"

    while True:
        output_menu()
        case = input("Choice a number: ")

        if case == "1":
            ingredients = input("Enter the list of products (please enter a space): ").split()
            ingredients = ",".join(ingredients)
            get_recipe(URL_RECIPE, ingredients)
        elif case == "2":
            get_station_coordinations(URL_ISS)
        elif case == "3":
            get_football_team(URL_FOOTBALL_TEAM)
        elif case == "4":
            get_pokemons(URL_POKEMONS)
        elif case == "0":
            exit()
        else:
            print("Incorrectly input. Repeat again.")


if __name__ == "__main__":
    main()

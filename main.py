import turtle
import pandas

screen = turtle.Screen()
screen.title("Państwa Europy")
screen.bgpic("europa3.gif")

data = pandas.read_csv("europa2.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 46:
    answer_country = screen.textinput(title=f"{len(guessed_countries)} z 46 państw Europy",
                                      prompt="Podaj nazwę państwa").title()
    print(answer_country)

    if answer_country == "Koniec":
        missing_countries = []
        for country in all_countries:
            if country not in guessed_countries:
                missing_countries.append(country)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("kraje_do_powtórzenia.csv")
        break
    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer_country)

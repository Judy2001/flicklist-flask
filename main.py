from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    todays_movie = get_random_movie()
    tomorrows_movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + todays_movie + "</li>"
    content += "</ul>"

    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrows_movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    return random.choice(["The Boondock Saints", "The Matrix", "M*A*S*H", "The Big Lebowski", "The Replacements"]
)


app.run()

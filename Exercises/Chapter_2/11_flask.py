from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <p>
    Hello from Bob Smith's comp.
    Click <a href="/space">here</a> to view a page about space.
    Click <a href="/coolform">here</a> to go to the form page.
    Click <a href="/dogs">here</a> to view a page about dogs.
    <br><img src="https://i.imgur.com/H3E1gAY.png" alt="Dog" /></br>
    </p>
    """

@app.route("/space")
def space():
    return """
    <p>
    In space, there are things.
    You can view those things on websites like
    <a href="https://nasa.gov">NASA!</a>
    Click <a href="/dogs">here</a> to view a page about dogs.
    Click <a href="/">here</a> to go back to the home page.
    </p>
    """

@app.route("/dogs")
def dogs():
    return """
    <p>
    This is the page about dogs.
    Click <a href="/space">here</a> to view a page about space.
    Click <a href="/">here</a> to go back to the home page.
    </p>
    """

@app.route("/coolform")
def coolform():
    return """
    <form action="/submit" method="post">
      Name: 
      <input type="text" id="user_name" name="user_name" />
      Animal you would pick as a pet:
      <input type="text" id="animal" name="animal" />
      <input type="submit" value="submit" />
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    user_name = request.form["user_name"]
    animal = request.form["animal"]
    safe_user_name = escape(user_name)
    safe_animal = escape(animal)
    f = open("my_submit_record.txt", "a")
    f.write(f"{safe_user_name} {safe_animal}\n")
    f.close()
    return f"""
    You submitted the form with this data: {safe_user_name} {safe_animal}
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
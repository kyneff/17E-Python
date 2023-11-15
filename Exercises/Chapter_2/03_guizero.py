## 1
# from guizero import App

# app = App(title="My first GUIZERO app")

# app.display()

  
## 2
# from guizero import App, Text

# app = App(title="Favorite Animal App")

# # create widgets here
# Text(app, text="Welcome to the favorite animal app!")

# app.display()

  
## 3
# from guizero import App, Text, TextBox

# app = App(title="Favorite Animal App")

# # create widgets here
# Text(app, text="Welcome to the favorite animal app!")
# Text(app, text="Enter your favorite animal:")
# name = TextBox(app)

# app.display()


## 4
# from guizero import App, Text, TextBox

# app = App(title="Favorite Animal App")
# app.text_size = 18
# app.text_color = "maroon"
# app.height = 800
# app.width = 1000
# app.bg = "dodger blue"

# Text(app, text="Welcome to the favorite animal app!")
# Text(app, text="Enter your favorite animal:")
# name = TextBox(app)
# name.text_color = "green"

# app.display()


## 5
from guizero import App, Text, TextBox, PushButton

def change_bg():
    app.bg = "orange"
    app.text_color = "blue"
    Text(app, text="Congratulations you changed the background color and text color when you pushed me.")

app = App(title="Favorite Animal App")
app.text_size = 18
app.text_color = "maroon"
app.height = 800
app.width = 1000
app.bg = "dodger blue"

# create widgets here
Text(app, text="Welcome to the favorite animal app!")
sometext = Text(app, text="Enter your favorite animal:")
name = TextBox(app)
name.text_color = "red"
button = PushButton(app, text="Press Here", command=change_bg)

app.display()
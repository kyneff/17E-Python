## 1
# from prompt_toolkit.shortcuts import input_dialog
# from prompt_toolkit.styles import Style


# style=Style.from_dict({
#     'dialog':             'bg:#88ff88',
#     'dialog frame.label': 'bg:#ffffff #000000',
#     'dialog.body':        'bg:#000000 #00ff00',
#     'dialog shadow':      'bg:#00aa00',
#     })

# name = input_dialog(
#     title='Username',
#     text='Please type your name:', style=style).run()

## 2
# from prompt_toolkit.shortcuts import input_dialog
# from prompt_toolkit.styles import Style


# style=Style.from_dict({
#     'dialog':             'bg:#33a2ff',
#     'dialog frame.label': 'bg:#7d33ff #3364ff',
#     'dialog.body':        'bg:#ffca33 #00ff00',
#     'dialog shadow':      'bg:#00aa00',
#     })

# name = input_dialog(
#     title='Animal',
#     text='Please type your favorite animal:', style=style).run()

## 3
## Use the example below and make changes to add a second dialog box to your previous code to tell the user
## the purpose of your program.
## Hint: place it above the `input_dialog` if you want it to run first and don't forget to update your import.
from prompt_toolkit.shortcuts import button_dialog, input_dialog, message_dialog, yes_no_dialog
from prompt_toolkit.styles import Style


style=Style.from_dict({
    'dialog':             'bg:#33a2ff',
    'dialog frame.label': 'bg:#7d33ff #3364ff',
    'dialog.body':        'bg:#ffca33 #00ff00',
    'dialog shadow':      'bg:#00aa00',
    })

message_dialog(
    title=f"Calculator!!",
    text=f"This is a basic calculator that adds, subtracts, multiplies, and divides.",
    style=style).run()

name = input_dialog(
    title='Name',
    text='Please type your name:', style=style).run()

dontstop = True

while dontstop == True:  
    firstnum = float(input_dialog(
        title=f"{name}'s input",
        text='Please type a number:', style=style).run())
    secondnum = float(input_dialog(
        title=f"{name}'s  second input",
        text='Please type another number:', style=style).run())
    operation = button_dialog(
        title='Operation',
        text=f'Choose an operation {name}?',
        buttons=[
            ('Add', 'sum'),
            ('Subtract', 'difference'),
            ('Multiply', 'product'),
            ('Divide', 'quotient')
        ], style=style
    ).run()
    if operation == 'sum':
        result = firstnum + secondnum
    elif operation == 'difference':
        result = firstnum - secondnum
    elif operation == 'product':
        result = firstnum * secondnum
    elif operation == 'quotient':
        result = firstnum / secondnum
    message_dialog(
            title=f"{name}'s Result",
            text=f"The {operation} is {result}", style=style).run()
    result = yes_no_dialog(
        title='Confirmation',
        text=f'Would you like to perform another calculation {name}?', style=style).run()
    if result == False:
        message_dialog(
            title='Exiting',
            text=f'Thank you for playing {name}, Goodbye', style=style).run()
        dontstop = False
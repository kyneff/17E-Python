# Delay Printing
# import time

# def delay_print(s):
#     for c in s:
#         print(c, end="", flush=True)
#         time.sleep(0.25)

# delay_print("hello world")

## The code below delays everything.
# import time

# real_print = print
# real_input = input
 
# def print(s):
#     for c in s:
#         real_print(c, end="", flush=True)
#         time.sleep(0.02)
#     real_print("\n")
 
# def input(s):
#     for c in s:
#         real_print(c, end="", flush=True)
#         time.sleep(0.02)
#     return real_input()

# print("Notice that the normal print function has now been overridden.")
# x = input("You can use input too.")

## Color Output
# from termcolor import cprint

# cprint("Hello, World!", "green", "on_white")

## Colors Using Rich
# from rich.console import Console
# from rich.table import Table

# table = Table(title="Star Wars Movies")

# table.add_column("Released", justify="right", style="cyan", no_wrap=True)
# table.add_column("Title", style="magenta")
# table.add_column("Box Office", justify="right", style="green")

# table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# console = Console()
# console.print(table)

## Dialog Boxes in the Terminal
# from prompt_toolkit.shortcuts import input_dialog

# text = input_dialog(
#     title='Input dialog example',
#     text='Please type your name:').run()

# print(f"You said {text}.")

## Sounds (Must provide an MP3 file.)
# from playsound import playsound

# playsound("You_must_pick_a_filename.mp3")
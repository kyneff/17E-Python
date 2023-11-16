  
from guizero import App, Text, PushButton, TextBox, Combo, Box
import ipaddress


def calculate():
    global boxContents   
    net4 = ipaddress.ip_network(f'{Ip_Address.value}/{cidr.value}', strict=False)
    boxContents = [
        Text(box, f"Your Network ID is {net4[0]}"),
        Text(box, f"Your Broadcast ID is {net4[-1]}"),
        Text(box, f"Your Subnet Mask is {net4.netmask}"),
        Text(box, f"You have {net4.num_addresses - 2} available IP addresses"),
        Text(box, f"Your available host range is:"),
        Text(box, f"{net4[1]} to"),
        Text(box, f"{net4[-2]}"),
    ]

def reset():
    global boxContents
    for item in boxContents:
        item.destroy()

app = App(title="Subnet Calculator")
app.height = 400
app.width = 600
Box(app, align="top", height=20, width="fill")
welcome = Text(app, text="Welcome to the IP Subnet Calculator")
welcome.text_size = 24
Box(app, height=10, width="fill")
Text(app, text="Please enter a valid IPv4 Network ID in the box below.")
Ip_Address = TextBox(app, width=14)
Box(app, height=10, width="fill")
Text(app, text="Please choose a CIDR value from the dropdown menu for your subnet.")
cidr = Combo(app, options= list(range(8, 30+1)))
Box(app, height=10, width="fill")
box = Box(app, width=550, height=175, border=True)
button1 = PushButton(box, text="Calculate", command=calculate)
button1.align = "left"
button2 = PushButton(box,  text="  Reset  ", command=reset)
button2.align = "right"

app.display()
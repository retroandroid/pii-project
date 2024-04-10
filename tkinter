import tkinter as ttk
from PIL import Image, ImageTk
import sqlite3
import ttkbootstrap as tb
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import tempsdb
tempsdb.c.execute(f"SELECT * FROM stats")
data = tempsdb.c.fetchall()

image_label = None
text_label = []
last_button = None
def on_button_click(button):
    # Destroy the old frame
    global image_label,text_label,last_button
    if image_label is not None and (button == last_button or button!=last_button):
        image_label.destroy()
        image_label = None
        for label in text_label:
            label.destroy()
        text_label = []
    if button == last_button:
        last_button = None
        return
    last_button = button
    

    # Load and resize the image
    image = Image.open("box1.png")
    image = image.resize((500, 500), Image.LANCZOS)  # Resize to 200x200
    photo_image = ImageTk.PhotoImage(image)

    # Create a label for the image and place it in the frame
    image_label = ttk.Label(root, image=photo_image)
    image_label.image = photo_image  # Keep a reference to the image
    image_label.place(x=50, y =50)

     #Connect to the database



    # Fetch data
    

    # Display data in labels in the frame
    for index, item in enumerate(data):
        label = ttk.Label(root, text=item)
        label.config(font=("Courier", 14), fg="blue", bg="#dce3f3", padx=10, pady=10, anchor="w")
        label.place(x = 100, y = 100+30*index)
        text_label.append(label)

root = tb.Window(themename="morph")
root.iconphoto(False, ttk.PhotoImage(file='weather-2019-02-07.png'))
root.title("Root Window")
# Create the button

# Load and resize the image
image = Image.open("Lebanon_adm_location_map.svg.png")
image = image.resize((900, 1000), Image.LANCZOS)  # Resize to 700x1000
image = ImageTk.PhotoImage(image)

# Create a label for the image and place it at the top right
label = tb.Label(root, image=image)
label.pack(anchor='ne')

# Define the coordinates for the buttons
coordinates = [(1530, 170), (1420, 270), (1600, 350), (1370, 480), (1450, 600), (1280, 740), (1210, 760)]
buttons_text = ['akkar','Tripoli','Baalbak','Matn','bekaa','Nabatiye','Saida']

# Create a list to store the label variables
labels = []
# Create a style
style = tb.Style()
style.configure("Red.TLabel", foreground="red", background="#85a3cd")
style.configure("Black.TLabel", foreground="black", background="#85a3cd")

def update_color(event, label):
    for lbl in labels:
        if lbl != label:
            lbl.config(style="Black.TLabel")  # Reset other labels
    if style.lookup(label.cget('style'), 'foreground') == 'black':
        label.config(style="Red.TLabel")  # Change to your desired color
    else:
        label.config(style="Black.TLabel")  # Change to default color'''

for i, ((x, y), text) in enumerate(zip(coordinates, buttons_text)):
    # Create the label with the "Black.TLabel" style
    label = tb.Label(root, text=text, style="Black.TLabel", font=("Times New Roman", 16))

    # Bind the update_color function to the label click event
    label.bind("<Button-1>", lambda event,lbl = label: (update_color(event,lbl),on_button_click(lbl)))
    label.place(x=x, y=y)

    # Add the label to the list
    labels.append(label)
style.configure("Label1.TLabel", foreground="black", background="black")
label1 = tb.Label(root, text='beirut', style="Label1.TLabel", font=("Times New Roman", 16))
label1.bind("<Button-1>", lambda event,lbl1 = label1:(update_color(event,lbl1),on_button_click(lbl1)))
label1.place(x=1250, y=470)
label1.config(background="#D9E3F1")
labels.append(label1)

def on_close():
    tempsdb.connection.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

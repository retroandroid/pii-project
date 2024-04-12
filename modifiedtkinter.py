from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb

# Create the root window
# Create the root window
root = tb.Window(themename="morph")
root.geometry('1920x1080')
image_label = None
text_label = []
last_button = None
def resize_image(event=None):
    global prev_width, prev_height

    # Get the new size of the window
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Only resize the image if the window size has changed by more than 10 pixels
    if abs(window_width - prev_width) > 10 or abs(window_height - prev_height) > 10:
        # Calculate the new size of the image
        if prev_width>prev_height:
            image_width = int(window_height * 0.75)
            image_height = int(window_height * 0.75)
        else:
            image_width = int(window_width * 0.75)
            image_height = int(window_width * 0.75)
        if window_height>800:
            window_height=800
        if window_width>1100:
            window_width=1100
        # Resize the image
        resized_image = image.resize((image_width, image_height), Image.BILINEAR)
        # Update the image in the label
        label.image = ImageTk.PhotoImage(resized_image)
        label['image'] = label.image

        # Update the previous size of the window
        prev_width = window_width
        prev_height = window_height
def update_color(event, label):
    for lbl in labels:
        if lbl != label:
            lbl.config(style="Black.TLabel")  # Reset other labels
    if style.lookup(label.cget('style'), 'foreground') == 'black':
        label.config(style="Red.TLabel")  # Change to your desired color
    else:
        label.config(style="Black.TLabel")  # Change to default color'''
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
    image2 = Image.open("Rectangle 2.png")  # Resize to 200x200
    photo_image1 = ImageTk.PhotoImage(image2)
    image_label = ttk.Label(root, image=photo_image1)
    # Create a label for the image and place it in the frame
    image_label.image = photo_image1  # Keep a reference to the image
    image_label.place(relx=0.25, rely =0.2, anchor='center')

# Initialize the previous size of the window
prev_width = root.winfo_width()
prev_height = root.winfo_height()
'''for index, item in enumerate(data):
        label = ttk.Label(root, text=item)
        label.config(font=("Courier", 14), fg="blue", bg="#dce3f3", padx=10, pady=10, anchor="w")
        label.place(x = 100, y = 100+30*index)
        text_label.append(label)'''


# Load the image
image = Image.open("pngtree-grey-lebanon-map-district-province-city-vector-picture-image_9437234.png")

# Create a label for the image and place it at the top right
label = tb.Label(root)
label.place(relx=0.75, rely=0.5, anchor='center')

# Bind the resize_image function to the <Configure> event of the window

coordinates = [(0.81, 0.18), (0.75, 0.27), (0.82, 0.4), (0.68, 0.5), (0.73, 0.61), (0.65, 0.745), (0.59, 0.75)]
buttons_text = ['akkar','Tripoli','Baalbak','Matn','bekaa','Nabatiye','Saida']

# Create a list to store the label variables
labels = []
# Create a style
style = tb.Style()
style.configure("Red.TLabel", foreground="red", background="#d0d4d5")
style.configure("Black.TLabel", foreground="black", background="#d0d4d5")
for i, ((x, y), text) in enumerate(zip(coordinates, buttons_text)):
    # Create the label with the "Black.TLabel" style
    label1 = tb.Label(root, text=text, style="Black.TLabel", font=("Times New Roman", 16))

    # Bind the update_color function to the label click event
    label1.bind("<Button-1>", lambda event,lbl = label1: (update_color(event,lbl),on_button_click(lbl)))
    label1.place(relx=x, rely=y)

    # Add the label to the list
    labels.append(label1)
label2 = tb.Label(root, text='beirut', style="Label1.TLabel", font=("Times New Roman", 16))
label2.bind("<Button-1>", lambda event,lbl2 = label2:(update_color(event,lbl2),on_button_click(lbl2)))
label2.place(relx=0.6, rely=0.5)
label2.config(background="#d9e3f1")
labels.append(label2)
root.bind('<Configure>', resize_image)

# Call the resize_image function manually to resize the image to fit the window
resize_image()
root.mainloop()
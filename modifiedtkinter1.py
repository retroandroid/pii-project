from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb
#import tempsdb
#import io
#import sys

# Create the root window
# Create the root window
root = tb.Window(themename="morph")
root.geometry('1920x1080')
root.configure(bg='#F6FAFE')
root.resizable(False,False)
image_label = None
text_labels = []
last_button = None
output_label = None
root.iconphoto(False, tb.PhotoImage(file='weather-2019-02-07.png'))
root.title("weather")
style = tb.Style()
style.configure("Red.TLabel", foreground="#FFFFFF", background="#d0d4d5")
style.configure("Black.TLabel", foreground="black", background="#d0d4d5")
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

    global image_label,text_labels,last_button,output_label,info_label
    if image_label is not None and (button == last_button or button!=last_button):
        image_label.destroy()
        image_label = None
        for label in text_labels:
            label.destroy()
        text_labels = []
    if output_label is not None:
        output_label.destroy()
        output_label = None
    if button == last_button:
        last_button = None
        return
    
    last_button = button
    image2 = Image.open("Rectangle 2.png")  # Resize to 200x200
    photo_image = image2.resize((800,500))
    photo_image1 = ImageTk.PhotoImage(photo_image)
    
    image_label = ttk.Label(root, image=photo_image1)
    image_label.configure(background="#F6FAFE")
    # Create a label for the image and place it in the frame
    image_label.image = photo_image1  # Keep a reference to the image
    image_label.place(relx=0.25, rely =0.4, anchor='center')
        # Redirect stdout to a string buffer
    #old_stdout = sys.stdout
    #sys.stdout = buffer = io.StringIO()

    # Call the function that prints the data
    #tempsdb.load_data(button.cget('text'))

    # Get the printed data
    #data = buffer.getvalue()

    # Restore stdout
    #sys.stdout = old_stdout

    # Display the data
    #output_label = ttk.Label(root, text=data,background="#E5F1FC",font=("Quincy",16))
    #output_label.place(relx=0.2, rely=0.4, anchor='center')  # Adjust the position as needed
    info_label = ttk.Label(root)
    
    labels1.append(info_label)

# Initialize the previous size of the window
prev_width = root.winfo_width()
prev_height = root.winfo_height()

image = Image.open("pngtree-grey-lebanon-map-district-province-city-vector-picture-image_9437234.png")
image=image.resize((800, 800), Image.BILINEAR)
photo_image1 = ImageTk.PhotoImage(image)
image_label1 = ttk.Label(root, image=photo_image1)
image_label1.configure(background="#F6FAFE")
image_label1.place(relx=0.75, rely=0.5, anchor='center') 
# Create a label for the image and place it at the top right
label = tb.Label(root)
label.configure(background="#F6FAFE")
label.place(relx=0.75, rely=0.5, anchor='center')
upbar=Image.open("Rectangle 1.png")
uplabel=tb.Label(root)
uplabel.configure(background="#F6FAFE")
uplabel.place(relx=0.5, rely=0.5, anchor='center')
# Bind the resize_image function to the <Configure> event of the window

coordinates = [(0.81, 0.18), (0.75, 0.27), (0.82, 0.4), (0.64, 0.55), (0.73, 0.61), (0.65, 0.745), (0.58, 0.76)]
buttons_text = ['akaar','tripoli','baalbak','Mount Lebanon','bqaa','nabatieh','South\nLebanon']

# Create a list to store the label variables
labels = []
# Create a style

for i, ((x, y), text) in enumerate(zip(coordinates, buttons_text)):
    # Create the label with the "Black.TLabel" style
    label1 = tb.Label(root, text=text, style="Black.TLabel", font=("Quincy", 16))

    # Bind the update_color function to the label click event
    label1.bind("<Button-1>", lambda event,lbl = label1: (update_color(event,lbl),on_button_click(lbl)))
    label1.place(relx=x, rely=y)

    # Add the label to the list
    labels.append(label1)
label2 = tb.Label(root, text='beirut', style="Black.TLabel", font=("Quincy", 16))
label2.bind("<Button-1>", lambda event,lbl2 = label2:(update_color(event,lbl2),on_button_click(lbl2)))
label2.place(relx=0.6, rely=0.5)
label2.config(background="#F6FAFE")
labels.append(label2)


# Call the resize_image function manually to resize the image to fit the window
task_bar = Image.open("Rectangle 1.png")  # Resize to 200x200
task_bar1 = task_bar.resize((3200,200))
photo_task = ImageTk.PhotoImage(task_bar1)
    
image_label2 = ttk.Label(root, image=photo_task)
image_label2.configure(background="#F6FAFE")
    # Create a label for the image and place it in the frame
image_label2.image = photo_task  # Keep a reference to the image
image_label2.place(relx=0.2, rely =0.01, anchor='center')
        # Redirect stdout to a string buffer

filter_button = Image.open("Group 1.png")
filter_button1 = filter_button.resize((60,60))
photo_filter = ImageTk.PhotoImage(filter_button1)

image_label3 = ttk.Label(root, image=photo_filter)
image_label3.configure(background="#F6FAFE")

image_label3.image = photo_filter  # Keep a reference to the image
image_label3.place(relx=0.96, rely =0.01, anchor='ne')
        # Redirect stdout to a string buffer

image_paths = ["3953532.png","humidity.png","multiple-users-silhouette.png","rainy.png","temperature.png"]
image_labels = []
images_displayed = False

info_label = ttk.Label(root)
info_label.place(relx=0.5, rely=0.5, anchor='center') 
labels1 =[]
def on_image_click(event, image_path):
    # Fetch specific information from the database based on the image_path
    # This is just a placeholder. Replace it with your actual database query.
    global info_label
    for i in labels1:
        i.destroy()
    labels1.clear()
    
    info = f"Information for {image_path}"
    
    info_label = ttk.Label(root)

    info_label.configure(text = info)
    info_label.place(relx=0.5, rely=0.5, anchor='center') 
    # Display the information
    labels1.append(info_label)

def change_image(event):
    global images_displayed,output_label,info_label,image_label,last_button
    if output_label is not None:
        output_label.destroy()
        output_label = None
    if info_label is not None:
        info_label.destroy()
        info_label = None
    if image_label is not None:
        image_label.destroy()
        image_label = None
    for i in labels:
        i.configure(style = "Black.TLabel")
        last_button = None
    if images_displayed:
        # Hide the images
        for label in image_labels:
            label.destroy()
        for i in labels1:
            i.destroy()
        labels1.clear()  
        images_displayed = False
        
        images_displayed = False
    else:
        # Show the images
        for i, path in enumerate(image_paths):
            image4 = Image.open(path)
            image_resized = image4.resize((60,60))
            photo_imagess = ImageTk.PhotoImage(image_resized)

            label_image = ttk.Label(root, image=photo_imagess)
            label_image.image = photo_imagess  # Keep a reference to the image
            label_image.place(relx=0.5 - 0.1 * i, rely=0.01, anchor='ne')  # Adjust the position as needed
            label_image.bind("<Button-1>", lambda event, path=path: (on_image_click(event, path)))
            image_labels.append(label_image)
        images_displayed = True
image_label3.bind("<Button-1>",change_image)
root.mainloop()

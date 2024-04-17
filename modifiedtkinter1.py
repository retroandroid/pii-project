from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb
import tempsdb
import io
import contextlib
from tkinter import font
# Create the root window
# Create the root window
root = tb.Window(themename="morph")
root.geometry('1920x1080')
root.configure(bg='#F6FAFE')
root.resizable(False,False)
image_label = None
text_labels = []
dark=False
images_displayed = False
filter_image_label = None
last_button = None
output_label = None
info_label=None
root.iconphoto(False, tb.PhotoImage(file='weather-2019-02-07.png'))
root.title("weather")
rectangle_images=[]
style = tb.Style()
prev_width = root.winfo_width()
prev_height = root.winfo_height()
previous_path=None
style.configure("Redbeirut.TLabel", background="#F6FAFE", foreground="#76ABAE")
style.configure("Blackbeirut.TLabel", background='#F6FAFE',foreground='#222831')
style.configure("Red.TLabel", background="#222831", foreground="#76ABAE")
style.configure("Black.TLabel", background='#222831',foreground='#F6FAFE')
heat_label = None
humid_label = None
pop_label = None
rain_label = None
temp_label = None

# Initialize the previous size of the window

image = Image.open(r"images\light\pngtree-grey-lebanon-map-district-province-city-vector-picture-image_9437234light.png")
image=image.resize((800, 800), Image.BILINEAR)
photo_image1 = ImageTk.PhotoImage(image)
image_label1 = ttk.Label(root, image=photo_image1)
image_label1.configure(background="#F6FAFE")
image_label1.place(relx=0.75, rely=0.5, anchor='center') 
# Create a label for the image and place it at the top right
label = tb.Label(root)
label.configure(background="#F6FAFE")
label.place(relx=0.75, rely=0.5, anchor='center')
# Bind the resize_image function to the <Configure> event of the window
lightimage=Image.open(r"images\light\group 8light.png")
light_image = ImageTk.PhotoImage(lightimage)
lightlabel=tb.Label(root,image=light_image)
lightlabel.bind("<Button-1>",lambda event:darkmode())
lightlabel.place(relx=0.9, rely=0.9, anchor='center')
lightlabel.configure(background="#F6FAFE")
coordinates = [(0.81, 0.18), (0.75, 0.27), (0.82, 0.4), (0.64, 0.55), (0.73, 0.61), (0.65, 0.745), (0.58, 0.76)]
buttons_text = ['akaar','tripoli','baalbak','Mount Lebanon','bqaa','nabatieh','South Lebanon']

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


label2 = tb.Label(root, text='beirut', style="Blackbeirut.TLabel", font=("Quincy", 16))
label2.bind("<Button-1>", lambda event,lbl2 = label2:(update_color_beirut(event,lbl2),on_button_click(lbl2)))
label2.place(relx=0.6, rely=0.5)
labels.append(label2)


# Call the resize_image function manually to resize the image to fit the window
task_bar = Image.open(r"images\light\Rectangle 1.png")  # Resize to 200x200
task_bar1 = task_bar.resize((3200,200))
photo_task = ImageTk.PhotoImage(task_bar1)
    
image_label2 = ttk.Label(root, image=photo_task)
image_label2.configure(background="#F6FAFE")
    # Create a label for the image and place it in the frame
image_label2.image = photo_task  # Keep a reference to the image
image_label2.place(relx=0.2, rely =0.01, anchor='center')
        # Redirect stdout to a string buffer

filter_button = Image.open(r"images\light\group1light.png")
photo_filter = ImageTk.PhotoImage(filter_button)

image_label3 = ttk.Label(root, image=photo_filter)
image_label3.configure(background="#222831")

image_label3.image = photo_filter  # Keep a reference to the image
image_label3.place(relx=0.96, rely =0.01, anchor='ne')
        # Redirect stdout to a string buffer

#image_paths = ["3953532.png","humidity.png,""multiple-users-silhouette.png","rainy.png","temperature.png"]


image_labels = []


info_label = ttk.Label(root)
info_label.place(relx=0.5, rely=0.5, anchor='center') 
labels1 =[]
def increase_size(event):
    # Get the label from the event
    labels = event.widget

    # Increase the font size
    current_font = font.Font(font=labels['font'])
    current_size = current_font.actual()['size']
    font_size = min(int(current_size) + 2, 30)  # Increase the font size by 2, but don't go above 30
    labels.configure(font=('Quincy', font_size))
def decrease_size(event):
     # Get the label from the event
    labels = event.widget
    # Increase the font size
    current_font = font.Font(font=labels['font'])
    current_size = current_font.actual()['size']
    font_size = min(int(current_size) - 2, 30)  # Increase the font size by 2, but don't go above 30
    labels.configure(font=('Quincy', font_size))
def update_color(event, label):
    global label2
    for lbl in labels:
        if lbl != label:
            lbl.config(style="Black.TLabel")
    label2.config(style="Blackbeirut.TLabel")
    if label.cget('style') == 'Black.TLabel':
        label.config(style="Red.TLabel")
    else:
        label.config(style="Black.TLabel")
def update_color_beirut (event, label):
    global labels
    for lbl in labels:
        if lbl != label:
            lbl.config(style="Black.TLabel")
    if label.cget('style') == 'Blackbeirut.TLabel':
        label.config(style="Redbeirut.TLabel")
    else:
        label.config(style="Blackbeirut.TLabel")  # Change to default color'''
def on_button_click(button):
    # Destroy the old frame
    global image_label,text_labels,last_button,output_label,info_label,image_labels,images_displayed,rectangle_images,labels1
    images_displayed = False
    for image in image_labels:
        image.destroy()
        image = None
    if info_label is not None:
        info_label.destroy()
        info_label = None
    for image in rectangle_images:
        image.destroy()
        image = None
    
    if image_label is not None and (button == last_button or button!=last_button):
        image_label.destroy()
        image_label = None
        for label in text_labels:
            label.destroy()
            label = None
        text_labels = []
    if output_label is not None:
        output_label.destroy()
        output_label = None
    if button == last_button:
        last_button = None
        return
    
    last_button = button
    if dark:
        recimage = Image.open(r"images\dark\Rectangle 2dark.png")  # Resize to 200x200
        photo_image = ImageTk.PhotoImage(recimage)
        image_label = ttk.Label(root, image=photo_image)
        image_label.image = photo_image  # Keep a reference to the image
        image_label.configure(background="#222831")
    else:
        recimage = Image.open(r"images\light\Rectangle 2.png")  # Resize to 200x200
        photo_image = ImageTk.PhotoImage(recimage)
        image_label = ttk.Label(root, image=photo_image)
        image_label.image = photo_image  # Keep a reference to the image
        image_label.configure(background="#F6FAFE")
    image_label.place(relx=0.25, rely =0.4, anchor='center')

    rectangle_images.append(image_label)
        # Redirect stdout to a string buffer
    def get_data(button_text):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tempsdb.load_data(button_text)
        return buffer.getvalue()
    data = get_data(button.cget('text'))
    # Display the data
    output_label = ttk.Label(root, text=data,font=("Quincy",16))
    if dark:
        output_label.configure(background="#76ABAE",foreground="#222831")
    else:  
        output_label.configure(background="#222831",foreground="#F6FAFE")
    output_label.place(relx=0.2, rely=0.4, anchor='center')  # Adjust the position as needed
    
    labels1.append(output_label)

def on_image_click(event, image_path,button):
    # Fetch specific information from the database based on the image_path
  # Fetch specific information from the database based on the image_path
    # This is just a placeholder. Replace it with your actual database query.
    global info_label,filter_image_label,rectangle_images,last_button,previous_path
    info_label = ttk.Label(root)
    
    if filter_image_label is None :
        if not dark:
            image2 = Image.open(r"images\light\Rectangle 2.png")
            photo_image1 = ImageTk.PhotoImage(image2)
        
            filter_image_label = ttk.Label(root, image=photo_image1)
            filter_image_label.configure(background="#F6FAFE")
        else:
            image2 = Image.open(r"images\dark\Rectangle 2dark.png")
            photo_image1 = ImageTk.PhotoImage(image2)
        
            filter_image_label = ttk.Label(root, image=photo_image1)
            filter_image_label.configure(background="#222831")
        
        
        # Create a label for the image and place it in the frame
        filter_image_label.image = photo_image1  # Keep a reference to the image
        filter_image_label.place(relx=0.245, rely =0.45, anchor='center')
        rectangle_images.append(filter_image_label)
    elif filter_image_label is not None and previous_path == image_path:
        for i in labels1:
            i.destroy()
        filter_image_label.destroy()
        filter_image_label = None

    
    def filter_data(button_image):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tempsdb.filter(button_image)
        return buffer.getvalue()
    info = filter_data(image_path)
    if info_label is not None and previous_path == image_path:
        for i in labels1:
            i.destroy()
            i=None
    else:
        for i in labels1:
            i.destroy()
            i=None
        info_label = ttk.Label(root,font=("Quincy",16))
        if dark:
           info_label.configure(background="#76ABAE",foreground="#222831")
        else:
            info_label.configure(background="#222831",foreground="#F6FAFE")
        info_label.configure(text = info)
        info_label.place(relx=0.25, rely=0.45, anchor='center') 
        # Display the information
        labels1.append(info_label)
    if previous_path==image_path:
        previous_path=None
    else:
        previous_path=image_path
def change_image(event):
    global images_displayed,output_label,info_label,image_label,last_button,image,filter_image_label,previous_path,heat_label,humid_label,pop_label,rain_label,temp_label       

    if filter_image_label is not None:
        filter_image_label.destroy()
        filter_image_label = None
        previous_path = None
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
        label2.configure(style = "Blackbeirut.TLabel")
        last_button = None
    
    if images_displayed:
        # Hide the images
        for label in image_labels:
            label.destroy()
            label = None
        for i in labels1:
            i.destroy()
            i = None
        labels1.clear()  
        images_displayed = False
        
    
    else:
        # Show the images
             # Show the images
        if not dark:
            image4 = Image.open(r"images\light\3953532light.png")
            image5 = Image.open(r"images\light\humiditylight.png")
            image6 = Image.open(r"images\light\multiple-users-silhouettelight.png")
            image7 = Image.open(r"images\light\rainylight.png")
            image8 = Image.open(r"images\light\temperaturelight.png")
        else:  
            image4 = Image.open(r"images\dark\3953532.png")
            image5 = Image.open(r"images\dark\humidity.png")
            image6 = Image.open(r"images\dark\multiple-users-silhouette.png")
            image7 = Image.open(r"images\dark\rainy.png")
            image8 = Image.open(r"images\dark\temperature.png")
            
        image_resized = image4.resize((60,60))
        photo_imagess = ImageTk.PhotoImage(image_resized)

        heat_label = tb.Label(root, image=photo_imagess)
        
        heat_label.image = photo_imagess  # Keep a reference to the image
        heat_label.place(relx=0.5, rely=0.01, anchor='ne')  # Adjust the position as needed
        heat_label.bind("<Button-1>", lambda event,lbl1=heat_label, path="Heat Index": (on_image_click(event, path,lbl1)))
        image_labels.append(heat_label)
        images_displayed = True
        
        
        image_resized = image5.resize((60,60))
        photo_imagess = ImageTk.PhotoImage(image_resized)

        humid_label = tb.Label(root, image=photo_imagess)
        
        humid_label.image = photo_imagess  # Keep a reference to the image
        humid_label.place(relx=0.4, rely=0.01, anchor='ne')  # Adjust the position as needed
        humid_label.bind("<Button-1>", lambda event,lbl2=humid_label ,path="Humidity": (on_image_click(event, path,lbl2)))
        image_labels.append(humid_label)
        images_displayed = True
      

        
        image_resized = image6.resize((60,60))
        photo_imagess = ImageTk.PhotoImage(image_resized)

        pop_label = tb.Label(root, image=photo_imagess)
        
        pop_label.image = photo_imagess  # Keep a reference to the image
        pop_label.place(relx=0.3, rely=0.01, anchor='ne')  # Adjust the position as needed
        pop_label.bind("<Button-1>", lambda event,lbl3=pop_label, path="Population": (on_image_click(event, path,lbl3)))
        image_labels.append(pop_label)
        images_displayed = True

        
        image_resized = image7.resize((60,60))
        photo_imagess = ImageTk.PhotoImage(image_resized)

        rain_label = tb.Label(root, image=photo_imagess)
        
        rain_label.image = photo_imagess  # Keep a reference to the image
        rain_label.place(relx=0.2, rely=0.01, anchor='ne')  # Adjust the position as needed
        rain_label.bind("<Button-1>", lambda event,lbl4=rain_label ,path="Chance of Precipitation": (on_image_click(event, path,lbl4)))
        image_labels.append(rain_label)
        images_displayed = True



        image_resized = image8.resize((60,60))
        photo_imagess = ImageTk.PhotoImage(image_resized)

        temp_label = tb.Label(root, image=photo_imagess)
        
        temp_label.image = photo_imagess  # Keep a reference to the image
        temp_label.place(relx=0.1, rely=0.01, anchor='ne')  # Adjust the position as needed
        temp_label.bind("<Button-1>", lambda event,lbl5=temp_label ,path="Temperature": (on_image_click(event, path,lbl5)))
        image_labels.append(temp_label)
        images_displayed = True
        if not dark:
            humid_label.configure(background="#222831")
            heat_label.configure(background="#222831")
            temp_label.configure(background="#222831")
            rain_label.configure(background="#222831")
            pop_label.configure(background="#222831")
        else:
            humid_label.configure(background="#76ABAE")
            heat_label.configure(background="#76ABAE")
            temp_label.configure(background="#76ABAE")
            rain_label.configure(background="#76ABAE")
            pop_label.configure(background="#76ABAE")
def darkmode():
    global lightlabel ,image_label,dark,heat_label,humid_label,pop_label,rain_label,temp_label,image_label2,image_label3,info_label,filter_image_label,output_label
    
    if root.cget('bg')=='#F6FAFE':
        style.configure("Red.TLabel", background="#EEEEEE", foreground="#76ABAE")
        style.configure("Black.TLabel", background='#EEEEEE',foreground='#222831')
        style.configure("Redbeirut.TLabel", background="#222831",foreground='#76ABAE')
        style.configure("Blackbeirut.TLabel",background="#222831", foreground="#F6FAFE")
        dark=True
        if image_label is not None:
            if image_label.winfo_exists():
                recimage = Image.open(r"images\dark\Rectangle 2dark.png")  # Resize to 200x200
                recimage = recimage.resize((600, 500), Image.BILINEAR)
                photo_image = ImageTk.PhotoImage(recimage)
                image_label.configure(image= photo_image,background='#222831')
                image_label.image = photo_image  # Keep a reference to the image
        if filter_image_label is not None: 
            if filter_image_label.winfo_exists():
                recimage = Image.open(r"images\dark\Rectangle 2dark.png")  # Resize to 200x200
                photo_image = ImageTk.PhotoImage(recimage)
                filter_image_label.configure(image= photo_image,background='#222831')
                filter_image_label.image = photo_image  # Keep a reference to the image
        root.configure(bg='#222831')
        mapimage=Image.open(r"images\dark\pngtree-grey-lebanon-map-district-province-city-vector-picture-image_9437234.png")
        mapimage=mapimage.resize((800, 800), Image.BILINEAR)
        mapper=ImageTk.PhotoImage(mapimage)
        image_label1.configure(image=mapper,background='#222831')
        image_label1.image=mapper
        lightlabel.configure(background='#222831')
        lightimage=Image.open(r"images\dark\Group 8.png")
        light_image = ImageTk.PhotoImage(lightimage)
        lightlabel.configure(image=light_image,background='#222831')  # Change the image
        lightlabel.image = light_image  # Keep a reference to the image
        task_bar=Image.open(r"images\dark\Path 4.png")
        task_bar1 = task_bar.resize((3200,200))
        photo_task = ImageTk.PhotoImage(task_bar1)
        image_label2.configure(image=photo_task,background='#222831')
        image_label2.image=photo_task
        filterimage=Image.open(r"images\dark\Group 1.png")
        filterimage=ImageTk.PhotoImage(filterimage)
        image_label3.configure(background="#76ABAE",image=filterimage)
        image_label3.image = filterimage  # Keep a reference to the image
        image_label3.place(relx=0.96, rely =0.01, anchor='ne')
        for i in labels1:
            if i is not None:
                if i.winfo_exists():
                    i.configure(background="#76ABAE",foreground="#222831")
        if heat_label is not None:
            image4 = Image.open(r"images\dark\3953532.png")
            image4=image4.resize((60,60))
            image4=ImageTk.PhotoImage(image4)
            heat_label.configure(image=image4,background='#76ABAE')
            heat_label.image = image4
            heat_label.place(relx=0.5, rely=0.01, anchor='ne')
        if humid_label is not None:
            image5 = Image.open(r"images\dark\humidity.png")
            image5=image5.resize((60,60))   
            image5=ImageTk.PhotoImage(image5)
            humid_label.configure(image=image5,background='#76ABAE')
            humid_label.image = image5
            humid_label.place(relx=0.4, rely=0.01, anchor='ne')
            image6 = Image.open(r"images\dark\multiple-users-silhouette.png")
        if pop_label is not None:
            image6=image6.resize((60,60))
            image6=ImageTk.PhotoImage(image6)
            pop_label.configure(image=image6,background='#76ABAE')
            pop_label.image = image6
            pop_label.place(relx=0.3, rely=0.01, anchor='ne')
        if rain_label is not None:
            image7 = Image.open(r"images\dark\rainy.png")
            image7=image7.resize((60,60))
            image7=ImageTk.PhotoImage(image7)
            rain_label.configure(image=image7,background='#76ABAE')
            rain_label.image = image7
            rain_label.place(relx=0.2, rely=0.01, anchor='ne')
            if temp_label is not None:
                image8 = Image.open(r"images\dark\temperature.png")
                
                image8=image8.resize((60,60))
                image8=ImageTk.PhotoImage(image8)
                temp_label.configure(image=image8,background='#76ABAE')
                temp_label.image = image8
                temp_label.place(relx=0.1, rely=0.01, anchor='ne')
        
    elif root.cget('bg')=='#222831':
        style.configure("Red.TLabel", background="#222831", foreground="#76ABAE")
        style.configure("Black.TLabel", background='#222831',foreground='#F6FAFE')
        
        style.configure("Redbeirut.TLabel", background="#F6FAFE", foreground="#76ABAE")
        style.configure("Blackbeirut.TLabel", background='#F6FAFE',foreground='#222831')
        dark=False
        if image_label is not None:
            if image_label.winfo_exists():
                recimage = Image.open(r"images\light\Rectangle 2.png")  # Resize to 200x200
                recimage = recimage.resize((600, 500), Image.BILINEAR)
                photo_image = ImageTk.PhotoImage(recimage)
                image_label.configure(image= photo_image,background='#F6FAFE')
                image_label.image = photo_image  # Keep a reference to the image
        if filter_image_label is not None:
            if filter_image_label.winfo_exists():
                recimage = Image.open(r"images\light\Rectangle 2.png")  # Resize to 200x200
                photo_image = ImageTk.PhotoImage(recimage)
                filter_image_label.configure(image= photo_image,background='#F6FAFE')
                filter_image_label.image = photo_image  # Keep a reference to the image
        mapimage=Image.open(r"images\light\pngtree-grey-lebanon-map-district-province-city-vector-picture-image_9437234light.png")
        mapimage=mapimage.resize((800, 800), Image.BILINEAR)
        mapper=ImageTk.PhotoImage(mapimage)
        image_label1.configure(image=mapper,background='#222831')
        image_label1.image=mapper
        root.configure(bg='#F6FAFE')
        image_label1.configure(background='#F6FAFE')   
        lightimage=Image.open(r"images\light\Group 8light.png")
        light_image = ImageTk.PhotoImage(lightimage)
        lightlabel.configure(image=light_image,background='#F6FAFE')  # Change the image
        lightlabel.image = light_image # Keep a reference to the image
        task_bar=Image.open(r"images\light\Rectangle 1.png")
        task_bar1 = task_bar.resize((3200,200))
        photo_task = ImageTk.PhotoImage(task_bar1)
        image_label2.configure(image=photo_task,background='#F6FAFE')
        image_label2.image=photo_task
        filterimage=Image.open(r"images\light\group1light.png")
        filterimage=ImageTk.PhotoImage(filterimage)
        image_label3.configure(background="#222831",image=filterimage)
        image_label3.image = filterimage  # Keep a reference to the image
        image_label3.place(relx=0.96, rely =0.01, anchor='ne')
        for i in labels1:
            if i is not None:
                if i.winfo_exists():
                    i.configure(background="#222831",foreground="#F6FAFE")
        if heat_label is not None:
            image4 = Image.open(r"images\light\3953532light.png")
            image4=image4.resize((60,60))
            image4=ImageTk.PhotoImage(image4)
            heat_label.configure(image=image4,background='#222831')
            heat_label.image = image4
            heat_label.place(relx=0.5, rely=0.01, anchor='ne')
        if humid_label is not None:
            image5 = Image.open(r"images\light\humiditylight.png")
            image5=image5.resize((60,60))
            image5=ImageTk.PhotoImage(image5)
            humid_label.configure(image=image5,background='#222831')
            humid_label.image = image5
            humid_label.place(relx=0.4, rely=0.01, anchor='ne')
        if pop_label is not None:
            image6 = Image.open(r"images\light\multiple-users-silhouettelight.png")
            image6=image6.resize((60,60))
            image6=ImageTk.PhotoImage(image6)
            pop_label.configure(image=image6,background='#222831')
            pop_label.image = image6
            pop_label.place(relx=0.3, rely=0.01, anchor='ne')
        if rain_label is not None:
            image7 = Image.open(r"images\light\rainylight.png")
            image7=image7.resize((60,60))
            image7=ImageTk.PhotoImage(image7)   
            rain_label.configure(image=image7,background='#222831')
            rain_label.image = image7
            rain_label.place(relx=0.2, rely=0.01, anchor='ne')
        if temp_label is not None:
            image8 = Image.open(r"images\light\temperaturelight.png")
            image8=image8.resize((60,60))
            image8=ImageTk.PhotoImage(image8)
            temp_label.configure(image=image8,background='#222831')
            temp_label.image =image8
            temp_label.place(relx=0.1, rely=0.01, anchor='ne')
        
image_label3.bind("<Button-1>",change_image)
for label in labels:
    label.bind("<Enter>", increase_size)
    label.bind("<Leave>", decrease_size)


root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")
root.geometry("500x700")
root.configure(background="gray22")

heading = Label(root, text="Image Viewer")
heading.place(relx=0.5, rely=0.1, anchor=CENTER)

display = Label(root)
display.place(relx=0.5, rely=0.5, anchor=CENTER)

img_label = None

def openImage():
    global img_label
    global img_path
    global img
    img_path = filedialog.askopenfilename(title="Open an Image", filetypes=[("Image Files", "*.jpg *.png *.gif")])
    print(img_path)
    img = Image.open(img_path)
    img_label = ImageTk.PhotoImage(img)
    display["image"] = img_label

openButton = Button(root, text="Open Image", command=openImage)
openButton.place(relx=0.5, rely=0.8, anchor=CENTER)

def rotateImage():
    global img_label
    img_rotate = img.rotate(180)
    img_label = ImageTk.PhotoImage(img_rotate)
    display["image"] = img_label

rotateButton = Button(root, text="Rotate", command=rotateImage)
rotateButton.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.fileName = askopenfilename(filetypes = (("PNG Files","*.png"),("JPG Files", "*.jpg"),("JPEG Files", "*.jpeg"),("GIF Files", "*.gif")))
print(root.fileName)

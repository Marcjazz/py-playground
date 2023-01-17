from pytube import YouTube;
from tkinter import *

root = Tk();
root.geometry("350x100")
root.title("KD-MARK Downloader")

#input
linkEntry = Entry(root, width=50)
linkEntry.pack()

def func():
    link = linkEntry.get()
    youtube = YouTube(link)
    video = youtube.streams.get_highest_resolution()
    video.download("downloads")

    alert = Label(root, text="Downloaded successfully !", fg="red")
    alert.pack()

#button
button = Button(root, text="Download", command=func)
button.pack()

root.mainloop()
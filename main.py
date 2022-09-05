from tkinter import *
import tkvideo
root = Tk()
root.state('zoom')
# root.call(__command=karuna_sir())
my_label = Label(root)
my_label.pack()
player = tkvideo.tkvideo("Teachers Day Video Presentation Download-(BestStatusVideo.com).mp4", my_label, loop = 1, size = (1280,720))
player.play()
root.mainloop()






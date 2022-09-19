from tkinter import *
import tkvideo
from pygame import mixer
mixer.init()
#loading the song
mixer.music.load("Teachers_Day__Flute__Bgm__Theme.mp3")
#playing the audio
mixer.music.play(-1)
root = Tk()
root.state('zoom')
my_label = Label(root)
my_label.pack()

player = tkvideo.tkvideo("Teachers Day Video Presentation Download-(BestStatusVideo.com).mp4", my_label, loop = 1, size = (1280,720))
player.play()
root.mainloop()





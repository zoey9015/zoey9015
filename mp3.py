mp3 WIP

import tkinter.font as font
from tkinter import filedialog

#layout

def addsongs():
    t_song=filedialog.askopenfilenames(initialdir="Music/",title="Pick a song, hoe!!(●'◡'●)", filetypes=(("mp3 Files","*.mp3")))
for s in t_song:
    s.replace("C:/Users/Windows/Desktop/zoey9/Notepad/Music/","")
    songs_list.insert(END,s)

def deletesong():
    curr_song=songs_list.curseselection()
    songs_list.delete(curr_song[0])  

def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/Windows/Desktop/zoey9/Notepad/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Previous():
    previous_one=songs_list.curselection()
    previous_one=previous_one[0]-1
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/lenovo/Desktop/DataFlair/Notepad/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)
def Next():
    next_one=songs_list.curselection()
    next_one=next_one[0]+1
    temp=songs_list.get(next_one)
    temp=f'C:/Users/lenovo/Desktop/DataFlair/Notepad/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)     

# music player functions 

root=Tk()
root.title('(☆Jojo\'s Music Player☆)')
mixer.init()

songs_list=Listbox(rootselectmode="SINGLE",bg="black", fg="pink",font='JuliaMono', height=12,width=47,selectbackground="black",selectforeground="black")
songs_list.grid(columnspan=9)

defined_font = font.Font(family='Helvetica')
play_button=Button(root,text="🦋Play🦋)",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

pause_button=Button(root,text="✪Pause✪",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)
#stop button
stop_button=Button(root,text="(ʘᴥʘ)Stop(ʘᴥʘ)",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)
#resume button
Resume_button=Button(root,text="🐚Resume🐚",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)
#previous button
previous_button=Button(root,text="(. ❛ ᴗ ❛.)Prev(. ❛ ᴗ ❛.)",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)
#nextbutton
next_button=Button(root,text="🍰Next🍰",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)
#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="🦄Menu🦄",menu=add_song_menu)
add_song_menu.add_command(label="💗Add songs💗",command=addsongs)
add_song_menu.add_command(label="🩷Delete song🩷",command=deletesong)

mainloop()

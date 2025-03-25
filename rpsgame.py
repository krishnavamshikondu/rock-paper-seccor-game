from tkinter import *
import random
from PIL import ImageTk,Image

root=Tk()
root.title('rock paper sc game')
root.geometry('1000x500')

#FOR TITLE
for i in range(4):
    if i==3:
        l=Label(root,text='lets start the game',bg='yellow',font=30)
        l.grid(row=1,column=2)
    else:
        l=Label(root)
        l.grid(row=1,column=i)
l1=Label(root,text='computer',bg='yellow',font=30)
l2=Label(root,text='v/s',bg='yellow',font=30)
l3=Label(root,text='   human  ',bg='yellow',font=30)
l1.grid(row=2,columnspan=3)
l2.grid(row=2,columnspan=5)
l3.grid(row=2,column=3)

# FOR STARTING IMAGE
i=0
img1=(Image.open('C:/Users/prana/OneDrive/Desktop/pythonproject/rock,paper,seccor game/start.jpg'))
img2=(Image.open('C:/Users/prana/OneDrive/Desktop/pythonproject/rock,paper,seccor game/start.jpg'))
imgg1=img1.resize((200,200),Image.Resampling.LANCZOS)
imgg2=img2.resize((200,200),Image.Resampling.LANCZOS)
imggg1=ImageTk.PhotoImage(imgg1)
imggg2=ImageTk.PhotoImage(imgg2)
m=Label(root,image=imggg1)
m1=Label(root,image=imggg2)
m.grid(row=3,column=0)
m1.grid(row=3,column=4)

l4=Label(root,text=i,bg='red',font=30,padx=10)
l5=Label(root,text=i,bg='red',font=30,padx=10)
l4.grid(row=3,column=1)
l5.grid(row=3,column=3)


img4=(Image.open('C:/Users/prana/OneDrive/Desktop/pythonproject/rock,paper,seccor game/rock.png'))
img5=(Image.open('paper.png'))
img6=(Image.open('seccor.png'))
imgg4=img4.resize((200,200),Image.Resampling.LANCZOS)
imgg5=img5.resize((200,200),Image.Resampling.LANCZOS)
imgg6=img6.resize((200,200),Image.Resampling.LANCZOS)
rock=ImageTk.PhotoImage(imgg4)
paper=ImageTk.PhotoImage(imgg5)
seccor=ImageTk.PhotoImage(imgg6)

co=0
hu=0

def game(x):
    global co
    global hu
    global rock
    global paper
    global seccor
    
    #print(type(x))
    #print(x)
    

    #img=[imgg1,imgg2,imgg3]
    imgs=[rock,paper,seccor]
    
    num=random.randint(0,2)
    #print(num)
    m1=Label(root,image=imgs[num])
    m1.grid(row=3,column=0)
    #com=img[num]

    nums=int(x)
    m2=Label(root,image=imgs[nums])
    m2.grid(row=3,column=4)
    #coms=img[nums]

    #co=0
    #hu=0
    
    if nums == num:
        l2=Label(root,text='draw ',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('draw no one will get the point')

    elif num==0 and nums==1:
        
        hu=hu+1
        #print(hu)
        l6=Label(root,text=hu,bg='red',font=30)
        l6.grid(row=3,column=3)
        
        l2=Label(root,text='Human won',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('human win')

    elif num==0 and nums==2:
        co=co+1
        #print(co)
        l6=Label(root,text=co,bg='red',font=30)
        l6.grid(row=3,column=1)
        
        l2=Label(root,text=' computer win',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('computer win')

    elif num==1 and nums==0:

        co=co+1
        #print(co)
        l6=Label(root,text=co,bg='red',font=30)
        l6.grid(row=3,column=1)
        
        l2=Label(root,text=' computer win',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('computer win')

    elif num==1 and nums==2:
        hu=hu+1
        #print(hu)
        l6=Label(root,text=hu,bg='red',font=30)
        l6.grid(row=3,column=3)
        
        l2=Label(root,text=' Human won',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('human win')

    elif num==2 and nums==0:
        hu=hu+1
        #print(hu)
        l6=Label(root,text=hu,bg='red',font=30)
        l6.grid(row=3,column=3)
        
        l2=Label(root,text=' Human won',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('human win')

    elif num==2 and nums==1:

        co=co+1
        #print(co)
        l6=Label(root,text=co,bg='red',font=30)
        l6.grid(row=3,column=1)
        
        l2=Label(root,text=' computer win',bg='yellow',fg='red',font='20',padx=40)
        l2.grid(row=10,columnspan=7)
        #print('computer win')

def Exit():
    global co
    global hu
    global imggg1
    global imggg2
    
    co=0
    hu=0
    
    i=0
    
    m=Label(root,image=imggg1)
    m1=Label(root,image=imggg2)
    m.grid(row=3,column=0)
    m1.grid(row=3,column=4)

    l4=Label(root,text=i,bg='red',font=30,padx=10)
    l5=Label(root,text=i,bg='red',font=30,padx=10)
    l2=Label(root,text='start the game',bg='yellow',fg='red' ,font='20',padx=40)

    l2.grid(row=10,columnspan=7)
    l4.grid(row=3,column=1)
    l5.grid(row=3,column=3)


#BUTTONS
button1=Button(root,text='rock',bg='sky blue',padx=70,pady=20,command=lambda:game(0))
button2=Button(root,text='paper',bg='sky blue',padx=70,pady=20,command=lambda:game(1))
button3=Button(root,text='seccor',bg='sky blue',padx=70,pady=20,command=lambda:game(2))
button4=Button(root,text='exit',padx=70,pady=20,command=Exit)

button1.grid(row=5,column=1)
button2.grid(row=5,column=2)
button3.grid(row=5,column=3)
button4.grid(row=5,column=4)

root.mainloop()
'''
import random  

while True:
    num=random.randint(0,2)
    print(num)

    nums=int(input('enter the number'))

    if nums == num:
        print('draw no one will get the point')

    elif num==0 and nums==1:
        print('human win')

    elif num==0 and nums==2:
        print('computer win')

    elif num==1 and nums==0:
        print('computer win')

    elif num==1 and nums==2:
        print('human win')

    elif num==2 and nums==0:
        print('human win')

    elif num==2 and nums==1:
        print('computer win')
'''

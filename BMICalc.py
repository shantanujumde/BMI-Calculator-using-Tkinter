from tkinter import *
from functools import partial  
root = Tk()
from PIL import Image, ImageTk
def BMI(concl,res, n1,n2):
    num1 = int(n1.get())  
    num2 = int(n2.get())  
    result = num2/(num1*num1)
    print(num2,num1,result)
    result = result*10000
    res.config(text="BMI is = %f" % result)  

    if result<=18.5:
        ans = 'underweight'
        load = Image.open('D:\Aabhyas\Python\OOP with python\BMI Application\Src\BW.jpg')
    elif result<25:
        ans= 'Normal'
        load = Image.open('D:\Aabhyas\Python\OOP with python\BMI Application\Src\AM.jpg')
    elif result<30:
        ans= 'Overweight'
        load = Image.open('D:\Aabhyas\Python\OOP with python\BMI Application\Src\OW.jpg')
    elif result<35:
        ans= 'Obese'
        load = Image.open('D:\Aabhyas\Python\OOP with python\BMI Application\Src\OBSE.jpg')
    elif result>35:
        ans= 'Extremely Obese'
        load = Image.open('D:\Aabhyas\Python\OOP with python\BMI Application\Src\EB.jpg')
    else:
        ans='Parameters are not followed'
    concl.config(text="You are %s" % ans)  
    
    load = load.resize((70, 190), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.grid(row=7,column=0)
    return  


root.title('BMI Calculator')
root.geometry("500x400+500+200")
l=Label(root,text="BMI Calculator",bg = 'grey',fg='Black',padx=190,pady=20,justify=CENTER,font=('Times New Romen',14,'italic'))
l.grid(row = 0,columnspan=3)


l2=Label(root,text="*Enter All the Details in Metirc units",justify=RIGHT)
l2.grid(row = 1)

n1 = StringVar()
n2 = StringVar()
Label(root,text="Enter Height(cms)").grid(row=2)
Label(root,text="Enter weight(kgs)").grid(row=3)
e1 = Entry(root,textvariable = n1)
e1.grid(row=2, column=1)
e2 = Entry(root,textvariable = n2)
e2.grid(row=3, column=1)
res = Label(root)
res.grid(row=6, column=0)  




concl = Label(root)
concl.grid(row=7, column=1)  

BMI = partial(BMI,concl,res,n1,n2)
Button(root,text='Calculate >', command=BMI).grid(row=5,column=1)
root.mainloop()

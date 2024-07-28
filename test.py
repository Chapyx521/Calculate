import tkinter as tk
from math import sqrt,cos,sin,tan,radians,pow,pi
def operation_touch():
    operation= operationswitch.get()
    x=enter_x.get().replace('PI',f'*{pi}')
    y=enter_y.get().replace('PI',f'*{pi}')

    try:
        if operation in ('/','*','^','+','-'):
            x=eval(x) if x else 0
            y=eval(y) if y else 0
            if operation == '+':
                result =x+y
            elif operation=='-':
                result=x-y
            elif operation=='*':
                result=x*y
            elif operation=='/':
                if y!=0:
                    result=x/y
                else:
                    print("Error,In this example Y mustn't to be zero")
            elif operation=='^':
                result=pow(x,y)
        elif operation=='sqrt':
            x=eval(x)
            result=sqrt(x)
        elif operation=='sin':
            x=eval(x)
            result=sin(radians(x))
        elif operation=='cos':
            x=eval(x)
            result=cos(radians(x))
        elif operation=='tan':
            x=eval(x)
            result=tan(radians(x))
        elif operation=='cotan':
            x=eval(x)
            result=1/(tan(radians(x)))
        labelofresult.config(text="Result "+str(result))
    except Exception as e:
        labelofresult.config(text=f"Error: {e}")




#Output window
window=tk.Tk()
window.title("Calculator")
operationswitch=tk.StringVar()


enter_x=tk.Label(window,text="Enter first number(You can use (pi)):")
enter_x.pack()
enter_x=tk.Entry(window)
enter_x.pack()



enter_y=tk.Label(window,text="Enter second number(You can use (pi),if you need):")
enter_y.pack()
enter_y=tk.Entry(window)
enter_y.pack()



operation_label=tk.Label(window,text="Choose operation:")
operation_label.pack()

operations=['+','-','/','*','^','sin','cos','tan','cotan','sqrt']
for op in operations:
    take=tk.Radiobutton(window,text=op,variable=operationswitch)
    take.pack()

button_calculator=tk.Button(window,text="Start",command=operation_touch)
button_calculator.pack()
labelofresult=tk.Label(window,text='Result  ')
labelofresult.pack()

window.mainloop()
















import tkinter
import tkinter as tk
from string import digits, punctuation, ascii_uppercase, ascii_lowercase
from random import choice

root = tk.Tk()
root.title("Password Generator")


def close():
    root.quit()


def passwordUpdate(output):
    password.delete(0, tk.END)
    password.insert(0, output)


def passwordGenerate():
    try:
        length = int(lengthEntry.get())
        charset = ''
        if upper.get():
            charset += f'{charset}{ascii_uppercase}'
        if lower.get():
            charset += f'{charset}{ascii_lowercase}'
        if numeric.get():
            charset += f'{charset}{digits}'
        if punct.get():
            charset += f'{charset}{punctuation}'
        opstr = ''
        while len(opstr) < length:
            opstr += f'{choice(charset)}'
    except IndexError:
        opstr = "Choose character sets!"
    except ValueError:
        opstr = "Choose a valid length!"
    passwordUpdate(opstr)


def copyToClipboard():
    root.clipboard_clear()
    lastpass = password.get()
    root.clipboard_append(lastpass)


# =============================================
# Output frame definition
# =============================================

outputFrame = tk.Frame(root)
outputFrame.columnconfigure(0, weight=1)
outputFrame.rowconfigure(0, weight=1)

passwordLabel = tk.Label(outputFrame, text='Password:', font=('Arial', 18))
passwordLabel.grid(row=0, column=0, sticky=tk.W + tk.E)

password = tk.Entry(outputFrame, font=('Arial', 16))
password.grid(row=0, column=1, sticky=tk.W + tk.E)

outputFrame.pack(pady=10, padx=10)

# =============================================
# Checkbox frame definition
# =============================================
checkFrame = tk.Frame(root)
checkFrame.columnconfigure(0, weight=1)
checkFrame.columnconfigure(1, weight=1)
checkFrame.columnconfigure(2, weight=1)
checkFrame.columnconfigure(3, weight=1)
checkFrame.columnconfigure(4, weight=1)
checkFrame.columnconfigure(5, weight=1)

lengthLabel = tk.Label(checkFrame, text='Length:', font=('Arial', 12))
lengthLabel.grid(row=0, column=0, sticky=tk.W + tk.E)

lengthEntry = tkinter.Entry(checkFrame, font=('Arial', 16), width=4)
lengthEntry.grid(row=0, column=1, sticky=tk.W + tk.E)
lengthEntry.insert(0, '8')

lower = tkinter.IntVar()
lowerCheck = tk.Checkbutton(checkFrame, variable=lower, text='Lower Case', font=('Arial', 12))
lowerCheck.select()
lowerCheck.grid(row=0, column=2, sticky=tk.W + tk.E)

upper = tkinter.IntVar()
upperCheck = tk.Checkbutton(checkFrame, variable=upper, text='Upper Case', font=('Arial', 12))
upperCheck.select()
upperCheck.grid(row=0, column=3, sticky=tk.W + tk.E)

numeric = tkinter.IntVar()
numericCheck = tk.Checkbutton(checkFrame, variable=numeric, text='Digits', font=('Arial', 12))
numericCheck.select()
numericCheck.grid(row=0, column=4, sticky=tk.W + tk.E)

punct = tkinter.IntVar()
check4 = tk.Checkbutton(checkFrame, variable=punct, text='Symbols', font=('Arial', 12))
check4.select()
check4.grid(row=0, column=5, sticky=tk.W + tk.E)

checkFrame.pack(fill=tk.X, pady=10, padx=10)

# =============================================
# Button frame definition
# =============================================

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text='Generate', font=('Arial', 18), command=passwordGenerate)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonFrame, text='Copy', font=('Arial', 18), command=copyToClipboard)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonFrame, text='Exit', font=('Arial', 18), command=close)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

buttonFrame.pack(fill=tk.X, pady=10, padx=10)

# =============================================
#
# =============================================
root.mainloop()

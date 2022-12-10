import tkinter
import tkinter as tk
from string import digits, punctuation, ascii_uppercase, ascii_lowercase
from random import choice, random

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
        if length < 8:
            raise ValueError("Length must be 8 or greater.")
        passOutput = ''
        while len(passOutput) < length:
            if upperEnable.get():
                passOutput += f'{choice(ascii_uppercase)}'
            if lowerEnable.get():
                passOutput += f'{choice(ascii_lowercase)}'
            if numericEnable.get():
                passOutput += f'{choice(digits)}'
            if punctuationEnable.get():
                passOutput += f'{choice(punctuation)}'
        passOutput = ''.join(sorted(passOutput, key=lambda x: random()))
    except IndexError:
        passOutput = "Choose character sets!"
    except ValueError:
        passOutput = "Choose a valid length!"
    passwordUpdate(passOutput)


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

passwordLabel = tk.Label(outputFrame, text='Password:', font=('Arial', 12))
passwordLabel.grid(row=0, column=0, sticky=tk.W + tk.E)

password = tk.Entry(outputFrame, font=('Arial', 12))
password.grid(row=0, column=1, sticky=tk.W + tk.E)

outputFrame.pack(pady=10, padx=10)

# =============================================
# Entry frame definition
# =============================================
entryFrame = tk.Frame(root)
entryFrame.columnconfigure(0, weight=1)
entryFrame.columnconfigure(1, weight=1)
entryFrame.columnconfigure(2, weight=1)

'''
customLabel = tk.Label(entryFrame, text='Custom Set:', font=('Arial', 12))
customLabel.grid(row=1, column=0, sticky=tk.W + tk.E)

customEntry = tkinter.Entry(entryFrame, font=('Arial', 12), width=64)
customEntry.grid(row=1, column=1, sticky=tk.W + tk.E)
# customEntry.insert(0, f'{ascii_lowercase}{ascii_uppercase}{digits}{punctuation}')
'''

entryFrame.pack(fill=tk.X, pady=10, padx=10)

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

lengthEntry = tkinter.Entry(checkFrame, font=('Arial', 12), width=4)
lengthEntry.grid(row=0, column=1, sticky=tk.W + tk.E)
lengthEntry.insert(0, '8')

lowerEnable = tkinter.IntVar()  # tk.IntVar() needed to hold value of checkbox input for comparison
lowerCheck = tk.Checkbutton(checkFrame, variable=lowerEnable, text='Lower Case', font=('Arial', 12))
lowerCheck.select()  # box ticked by default
lowerCheck.grid(row=0, column=2, sticky=tk.W + tk.E)

upperEnable = tkinter.IntVar()
upperCheck = tk.Checkbutton(checkFrame, variable=upperEnable, text='Upper Case', font=('Arial', 12))
upperCheck.select()
upperCheck.grid(row=0, column=3, sticky=tk.W + tk.E)

numericEnable = tkinter.IntVar()
numericCheck = tk.Checkbutton(checkFrame, variable=numericEnable, text='Digits', font=('Arial', 12))
numericCheck.select()
numericCheck.grid(row=0, column=4, sticky=tk.W + tk.E)

punctuationEnable = tkinter.IntVar()
check4 = tk.Checkbutton(checkFrame, variable=punctuationEnable, text='Symbols', font=('Arial', 12))
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

btn1 = tk.Button(buttonFrame, text='Generate', font=('Arial', 12), command=passwordGenerate)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonFrame, text='Copy', font=('Arial', 12), command=copyToClipboard)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonFrame, text='Exit', font=('Arial', 12), command=close)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

buttonFrame.pack(fill=tk.X, pady=10, padx=10)

# =============================================
#
# =============================================
root.mainloop()

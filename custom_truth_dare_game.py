#custom_truth_dare_game

import tkinter as tk
from random import *
import datetime

now = datetime.datetime.now
seed(now)

dares = ["dare: give Rachit 5 euros ;p","dare: cook samosas for Rachit","dare: cook chole bhature for Rachit","dare: buy a beer for Rachit"]
truths = ["truth: do you like Rachit?", "truth: do you really like Rachit","truth: do you think life has meaning?"]

def dare():
    dareoutput = choice(dares)
    print(dareoutput)

def truth():
    truthoutput = choice(truths)
    print(truthoutput)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
#frame.size(4)

TruthButton = tk.Button(frame,
                   text="Truth",
                   fg = "green",
                   command=truth)
TruthButton.pack(side=tk.LEFT)

DareButton = tk.Button(frame,
                   text="Dare",
                   fg = "red",
                   command=dare)
DareButton.pack(side=tk.LEFT)

root.mainloop()    
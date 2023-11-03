
from tkinter import filedialog

origem = filedialog.askopenfilenames()

for c in origem:
    i = c.rfind('/')+1
    print(c[i:])

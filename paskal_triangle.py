import tkinter as tk

def paskal_triangle(old_pt):
    pt = []
    for i in range(len(old_pt)):
        pt.append(old_pt[i-1] + old_pt[i]) if i != 0 else pt.append(old_pt[i])
    pt.append(1)
    return pt

root = tk.Tk()
root.geometry("1200x900")https://github.com/Akkompanist/paskal_triangle/blob/main/paskal_triangle.py
T1 = tk.Text(root, height=900, width=1200, font=("Helvetica", 5))
T1.tag_configure("center", justify='center')


start = [1]
for i in range(101):
    pt = paskal_triangle(start)
    T1.insert("end", start)
    T1.insert("end", "\n")
    start = pt

T1.tag_add("center", "1.0", "end")
T1.pack()

root.mainloop()

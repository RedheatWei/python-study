#coding: utf-8
import Tkinter
class Tkwin:
    def __init__(self, root):
        self.root = root 
        self.frame = Tkinter.Frame(root, bd=2)
        self.edit = Tkinter.Text(self.frame, width=2.8, height=3.3)
        self.edit.pack(side = Tkinter.LEFT)
        self.frame.place(y = 2)
        self.edit.bind('<Button-1>', self.action)
    def action(self, event):
        #self.edit.insert(Tkinter.END, u"窗口坐标x:%d 窗口坐标y:%d\n" % (event.x, event.y))
        self.edit.insert(Tkinter.END, u"x:%d y:%d\n" % (event.x_root, event.y_root))

root = Tkinter.Tk()
window = Tkwin(root)
root.minsize(100,80)
root.maxsize(100,80)
root.mainloop()
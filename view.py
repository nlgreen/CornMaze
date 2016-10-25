from tkinter import *


class View:
    def __init__(self,theMap,thePlayer):
        self.theMap = theMap
        self.thePlayer = thePlayer


    # Draw the map in tkinter
    def draw(self):

        master = Tk()

        canvas_width = self.sidelength * 100 + 20
        canvas_height = self.sidelength * 100 + 20

        w = Canvas(master,
                   width = canvas_width,
                   height = canvas_width)

        
        w.pack()


        def up():
            if self.thePlayer.moveUp():
                master.destroy()
                self.draw()
        def down():
            if self.thePlayer.moveDown():
                master.destroy()
                self.draw()
        def left():
            if self.thePlayer.moveLeft():
                master.destroy()
                self.draw()
        def right():
            if self.thePlayer.moveRight():
                master.destroy()
                self.draw()
            
        u = Button(master,text="Up",command=up)
        d = Button(master,text="Down",command=down)
        l = Button(master,text="Left",command=left)
        r = Button(master,text="Right",command=right)
        u.pack(side = TOP)
        d.pack(side = BOTTOM)
        l.pack(side = LEFT)
        r.pack(side = RIGHT)

        
        height = 10

        # draw walls for each node -- walls technically overlap
        for row in self.theMap.nodelist:
            width = 10
            for node in row:
                if not node:
                    continue
                if not node.top:
                    w.create_line(width,height,width+100,height)
                if not node.bottom:
                    w.create_line(width,height+100,width+100,height+100)
                if not node.left:
                    w.create_line(width,height,width,height+100)
                if not node.right:
                    w.create_line(width+100,height,width+100,height+100)

                if node.player:
                    w.create_oval(width,height,width+100,height+100)

                width += 100
            height += 100

            
        mainloop()

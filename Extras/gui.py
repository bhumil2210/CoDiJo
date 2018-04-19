import tkinter as tk
import mysql.connector
import webbrowser
from search_jobs import *


def gui():
    def dbclick(event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection)
        webbrowser.open(picked, new=1)

    def newframe(root):
        s = location.get()
        job = enter_job.get()
        print(s)
        enter_job.destroy()
        location.destroy()
        b.destroy()
        # load = tk.Frame(root)
        # text = tk.Text(root)
        # text.insert(tk.INSERT, "loading")
        # # load.pack(fill="both", expand=True)
        # text.pack()
        search_jobs_object = Jobs()
        search_jobs_object.search_jobs(job)

        if not search_jobs_object.is_all_alive:
            db = mysql.connector.connect(host="localhost", user="root", passwd="Bhumil2211", db="jobs")
            cursor = db.cursor()
            query = "select * from job_details where experience like \'" + s + "%\' or experience like \'%" + s + "%\' or experience like \'%" + s + "\'"
            print(query)
            cursor.execute(query)
            rows = cursor.fetchall()
            # text.destroy()

            def populate(frame):
                # Put in some fake data
                space = 0
                for row in rows:
                    # tk.Label(frame, text="%s" % row, width=3, borderwidth="1",
                    #          relief="solid").grid(row=row, column=0)
                    # t="this is the second column for row %s" %row
                    # tk.Label(frame, text=t).grid(row=row, column=1)

                    record = tk.Listbox(frame, width="80", height="15", background="#F0F3F4")
                    scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
                    record.insert(1, row[0])
                    record.insert(2, "")
                    record.insert(3, row[1])
                    record.insert(4, "")
                    record.insert(5, row[2])
                    record.insert(6, "")
                    record.insert(7, row[3])
                    record.insert(8, "")
                    record.insert(9, row[4])
                    record.insert(10, "")
                    record.insert(11, row[5])
                    record.insert(12, "")
                    record.insert(13, row[6])
                    # record.pack(pady=20)
                    record.grid(row=space, column=0)
                    record.bind('<<ListboxSelect>>', dbclick)
                    scrollbar.config(command=record.xview)
                    scrollbar.grid(row=space + 1, column=0, sticky=tk.W + tk.E)
                    record.config(xscrollcommand=scrollbar.set)
                    frame.grid_rowconfigure(space + 2, minsize=20)
                    space = space + 3

            def onFrameConfigure(pallete):
                # Reset the scroll region to encompass the inner frame
                pallete.configure(scrollregion=pallete.bbox("all"))

            canvas = tk.Canvas(root, borderwidth=0, background="#A9CCE3")
            frame = tk.Frame(canvas, background="#A9CCE3", padx=300, pady=20)
            vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)

            vsb.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4, 4), window=frame, anchor="nw")

            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

            populate(frame)

            root.mainloop()

    win = tk.Tk()
    enter_job = tk.Entry(win)
    location = tk.Entry(win)
    b = tk.Button(win, command=lambda: newframe(win))
    enter_job.grid(row=0, column=0)
    location.grid(row=1, column=0)
    b.grid(row=2, column=0)
    win.mainloop()


gui()

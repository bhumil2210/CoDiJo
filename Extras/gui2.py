import tkinter as tk
from tkinter.font import Font
import mysql.connector
import webbrowser
from search_jobs import *


def frame2():
    x = ''

    def dbclick(event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection)
        picked = picked.strip("For More Details-")
        webbrowser.open(picked, new=1)


    def newframe(root):
        '''
        s = location.get()
        job = enter_job.get()
        print(s)
        enter_job.destroy()
        location.destroy()
        b.destroy()
        '''

        # location
        loc=e1.get()


        # skills
        list2 = e2.get().split(',')

        s=exp.get()
        job=enter_job.get()
        exp.destroy()
        enter_job.destroy()
        e1.destroy()
        e2.destroy()
        b.destroy()
        w1.destroy()
        w2.destroy()
        w3.destroy()
        w4.destroy()
        T = tk.Label(root, height=2, width=30, font=tk.font.Font(family='Times', size=15), text="Loading...")
        T.configure(bg="#A9CCE3", highlightbackground="black", highlightthickness=0)
        T.pack(pady=10)
        root.after(15000, lambda: T.destroy())
        root.after(15000, lambda: T1.destroy())
        root.after(1000, lambda: root.quit())
        root.mainloop()
        # load = tk.Frame(root)
        # text = tk.Text(root)
        # text.insert(tk.INSERT, "loading")
        # load.pack(fill="both", expand=True)
        # text.pack()
        search_jobs_object = Jobs()
        search_jobs_object.search_jobs(job)
        # root.mainloop()

        if not search_jobs_object.is_all_alive:
            print("loading over")
            # load.destroy()
            # text.destroy()
            db = mysql.connector.connect(host="localhost", user="root", passwd="Bhumil2211", db="jobs")
            cursor = db.cursor()
            query = "select * from job_details where experience like \'" + s + "%\' or experience like \'%" + s + "%\' or experience like \'%" + s + "\'"


            length = len(list2)
            i = 0
            while i < length:
                if i == 0:
                    query1 = "select * from job_details where skills like '%" + list2[i] + "' or '" + list2[
                        i] + "%' or '%" + list2[i] + "%'"
                else:
                    query1 += " or "
                    query1 += "'%" + list2[i] + "' or '" + list2[i] + "%' or '%" + list2[i] + "%'"
                i += 1
            final_query=query1 + " union " +query
            cursor.execute(final_query)
            rows1 = cursor.fetchall()


            def checkpopulate(frame):
                # Put in some fake data

                c=2
                for row in rows1:

                    print('Outside loop')

                    print('Hellllllllo')
                    if row[5].find(loc)!=-1:
                        print('Hello')
                        print(row[5])
                        # print(row[6])
                        record = tk.Listbox(frame,bd=0,width="80",height="15",background="#A9CCE3",font=tk.font.Font(family='Helvetica',size=12))
                        record.config(highlightbackground="black", highlightthickness=0)
                        Scrollbar = tk.Scrollbar(frame)
                        record.insert(1, row[0])
                        record.insert(2, "")
                        record.insert(3, row[1])
                        record.insert(4, "")

                        x = row[2]
                        i = 5
                        y = len(x)
                        start = 0
                        end = 99
                        print(x)
                        while y >= 99:
                            print("Inside loop")
                            print(end - start)
                            # print(x)
                            record.insert(i, x[start:end] + "-")

                            print(x[start:end])
                            print("Start " + x[start])
                            print("End " + x[end])
                            y = y - 99
                            i += 1
                            start += 99
                            end += 99

                        record.insert(i, x[start:])
                        print(x[start:end])



                        record.insert(i+1, "")
                        record.insert(i+2, "Key Skills-"+row[3])
                        record.insert(i+3, "")
                        record.insert(i+4, "Work Experience-"+row[4])
                        record.insert(i+5, "")
                        record.insert(i+6, "Location-"+row[5])
                        record.insert(i+7, "")
                        record.insert(i+8, "For More Details-"+row[6])
                        # record.pack(pady=20)
                        print('This row is inserted')

                        record.grid(row=c, column=0, padx=200)
                        record.bind('<<ListboxSelect>>', dbclick)
                        record.grid_rowconfigure(c + 2, minsize=20)
                        w = tk.Canvas(frame, width=1200, height=10, bd=0, highlightthickness=0)
                        w.configure(bg="#A9CCE3")
                        w.grid(row= c + 4, column=0)
                        w.create_line(-5000, 0, 5000, 0, fill="black", width=10)
                        c = c + 5


            def onFrameConfigure(pallete):
                # Reset the scroll region to encompass the inner frame
                pallete.configure(scrollregion=pallete.bbox("all"))

            def fun():
                frame.quit()

            canvas = tk.Canvas(root, borderwidth=0, background="#A9CCE3")
            frame = tk.Frame(canvas, background="#A9CCE3", padx=300, pady=20)
            vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)

            vsb.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4, 4), window=frame, anchor="nw")
            # quit_btn.pack(side="right",anchor="ne")
            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
            T2 = tk.Label(frame, height=2, width=30, bd=0, font=tk.font.Font(family='Times', size=30), text="CoDiJo")
            T2.configure(bg="#A9CCE3", highlightthickness=0, justify='center')

            T2.grid(row=0, column=0, padx=10, pady=30)
            quit_btn = tk.Button(root, text='Quit', command=root.quit,
                                 font=tk.font.Font(family='Helvetica', size=12)).pack(
                side="right", anchor="n", pady=30, padx=50)
            checkpopulate(frame)

    root = tk.Tk()

    '''
    canvas = tk.Canvas(root, borderwidth=0, background="#A9CCE3")
    frame = tk.Frame(canvas, background="#A9CCE3", padx=300, pady=20)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    '''

    '''
    enter_job.grid(row=1, column=2)
    exp.grid(row=2, column=2)
    e1.grid(row=3,column=2)
    e2.grid(row=4,column=2)
    b.grid(row=5, column=2)
    '''

    T1 = tk.Label(root, height=2, width=30, bd=0, font=tk.font.Font(family='Times', size=30), text="CoDiJo")
    T1.configure(bg="#A9CCE3", highlightthickness=0, justify='center')

    T1.pack(padx=50,pady=(20,0))

    e1 = tk.Entry(root,bd=0,background="#A9CCE3",font=tk.font.Font(family='Helvetica',size=12))
    e1.config(highlightbackground="black", highlightthickness=0,justify='center',fg="#778899")
    e1.insert(0,'Location')
    e1.bind("<FocusIn>", lambda args: e1.delete('0', 'end'))
    e2=tk.Entry(root,bd=0,background="#A9CCE3",font=tk.font.Font(family='Helvetica',size=12))
    e2.config(highlightbackground="black", highlightthickness=0,justify='center',fg="#778899")
    e2.insert(0, 'Skills you are good at:)')
    e2.bind("<FocusIn>", lambda args: e2.delete('0', 'end'))
    b=tk.Button(root,text="Discover Jobs", command=lambda :newframe(root),font=tk.font.Font(family='Helvetica',size=12))
    b.config(highlightbackground="black", highlightthickness=0,justify='center')
    root.geometry("400x600")
    enter_job = tk.Entry(root,background="#A9CCE3",bd=0,font=tk.font.Font(family='Helvetica',size=12))
    enter_job.config(highlightbackground="black", highlightthickness=0,justify='center',fg="#778899")
    enter_job.insert(0, 'Enter Job Field')
    enter_job.bind("<FocusIn>", lambda args: enter_job.delete('0', 'end'))
    exp = tk.Entry(root,bd=0,background="#A9CCE3",font=tk.font.Font(family='Helvetica',size=12))
    exp.config(highlightbackground="black", highlightthickness=0,justify='center',fg="#778899")
    exp.insert(0, 'Work Experience')
    exp.bind("<FocusIn>", lambda args: exp.delete('0', 'end'))
    # b = tk.Button(root, command=lambda: newframe(win))

    enter_job.pack(padx=50,pady=(20,0))
    w1= tk.Canvas(root, width=1000, height=10, bd=0, highlightthickness=0)
    w1.configure(bg="#A9CCE3")
    w1.pack(padx=45, pady=(0,20))
    w1.create_line(-4000, 0, 4000, 0, fill="black", width=5)


    exp.pack(padx=50,pady=(20,0))
    w2= tk.Canvas(root, width=1000, height=10, bd=0, highlightthickness=0)
    w2.configure(bg="#A9CCE3")
    w2.pack(padx=45, pady=(0,20))
    w2.create_line(-4000, 0, 4000, 0, fill="black", width=5)


    e1.pack(padx=50,pady=(20,0))
    w3 = tk.Canvas(root, width=1000, height=10, bd=0, highlightthickness=0)
    w3.configure(bg="#A9CCE3")
    w3.pack(padx=45,pady=(0,20))
    w3.create_line(-4000, 0, 4000, 0, fill="black", width=5)

    e2.pack(padx=50,pady=(20,0))
    w4 = tk.Canvas(root, width=1000, height=10, bd=0, highlightthickness=0)
    w4.configure(bg="#A9CCE3")
    w4.pack(padx=45,pady=(0,20))
    w4.create_line(-4000, 0, 4000, 0, fill="black", width=5)

    b.pack(padx=50,pady=(20,0))

    root.mainloop()


frame2()

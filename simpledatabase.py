import Tkinter
import sqlite3
import ttk


def put(*args):
    try:
        e_name = str(i_name)
        e_pay = int(i_pay)
        conn = sqlite3.connect('*.db')
        c = conn.cursor()
        c.execute('create table if not exists employee(id integer primary key auto increment, name text, salary integer)')
        c.execute('insert into employee(name, salary) values(?,?)',(e_name,e_pay))
        conn.close()
        notice = 'insertion successful'
    except:
        notice ='insert proper values'

def del_id(*args):
    try:
        e_id = int(d_del)
        conn = sqlite3.connect('medha.db')
        c = conn.cursor()
        c.execute('delete from employee where id =?',(e_id))
        notice = 'deleted successfully'
        conn.close()
    except:
        notice = 'insert proper values'

def del_name(*args):
    try:
        e_name = int(d_del)
        conn = sqlite3.connect('medha.db')
        c = conn.cursor()
        c.execute('delete from employee where name = ?',(e_name))
        notice = 'deleted successfully'
        conn.close()
    except:
        notice = 'insert proper values'

root = Tkinter.Tk()
root.title('Python Projet - gui and db')

mainframe = ttk.Frame(root,padding='3 3 12 12' )
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight =1)

i_name = str()
i_id = str()
i_pay = str()
notice = str()
d_del = str()

i_name_entry = ttk.Entry(mainframe, width =7, textvariable = i_name)
i_name_entry.grid(column = 1, row = 1)

i_id_entry = ttk.Entry(mainframe, width =7, textvariable = i_id)
i_id_entry.grid(column = 2, row = 1)

i_pay_entry = ttk.Entry(mainframe, width =7, textvariable = i_pay)
i_pay_entry.grid(column = 3, row = 1)

i_del_entry = ttk.Entry(mainframe, width =7, textvariable = d_del)
i_del_entry.grid(column = 1, row =4)

ttk.Label(mainframe, text ='Name of Employee').grid(column = 1, row = 0)
ttk.Label(mainframe, text ='Employee ID').grid(column = 2, row =0)
ttk.Label(mainframe, text ='Employee Pay').grid(column = 3, row=0)
ttk.Label(mainframe, text ='Name/ID of Employee to delete').grid(column = 1, row=3)
ttk.Label(mainframe, text = notice).grid(column = 1, row = 6)

ttk.Button(mainframe, text='Insert', command = put).grid(column=3, row=2)
ttk.Button(mainframe, text='Delete By ID', command = del_id).grid(column =1, row = 5)
ttk.Button(mainframe, text='Delete By Name', command = del_name).grid(column = 3, row=5)

for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
i_name_entry.focus()

root.mainloop()

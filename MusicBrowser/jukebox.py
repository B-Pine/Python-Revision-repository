import sqlite3
import tkinter

db = sqlite3.connect("music.db")


class ScrollBox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(ScrollBox):

    def __init__(self, window, connection, table_name, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        self.cursor = connection.cursor()
        self.table = table_name
        self.field = field
        self.linked_box = None
        self.link_field = None

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ", ".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_id=None):
        if link_id and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + " = ?" + self.sql_sort
            print(sql)  # todo delete this line
            self.cursor.execute(sql, (link_id,))
        else:
            print(self.sql_select + self.sql_sort)
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for row in self.cursor:
            self.insert(tkinter.END, row[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)  # todo delete this line
            index = self.curselection()
            value = self.get(index.__getitem__(0))

            # get artist id from the database
            link_name, link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?",
                                                     (value,)).fetchone()
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    # Setting up GUI
    mainWindow = tkinter.Tk()
    mainWindow.title("Simple Music Browser")
    mainWindow.geometry('1024x728')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ==== Labels ====
    tkinter.Label(mainWindow, text='Artists').grid(row=0, column=0)
    tkinter.Label(mainWindow, text='Albums').grid(row=0, column=1)
    tkinter.Label(mainWindow, text='Songs').grid(row=0, column=2)

    # ==== Artists listbox====
    artistsList = DataListBox(mainWindow, db, 'artists', 'name')
    artistsList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistsList.config(border=2, relief='sunken')
    artistsList.requery()

    # ==== Albums listbox====
    albumsLv = tkinter.Variable(mainWindow)
    albumsLv.set(('Albums list',))
    albumList = DataListBox(mainWindow, db, 'albums', 'name', ('name',), listvariable=albumsLv)
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')
    # albumList.requery()
    artistsList.link(albumList, 'artist')

    # ==== Songs listbox====
    songsLv = tkinter.Variable(mainWindow)
    songsLv.set(('Songs List',))
    songsList = DataListBox(mainWindow, db, 'songs', 'title', ('track', 'title'), listvariable=songsLv)
    songsList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songsList.config(border=2, relief='sunken')
    # songsList.requery()
    albumList.link(songsList, 'album')

    # ==== Calling main loop====
    # test_list = range(100)
    # albumsLv.set(tuple(test_list))
    mainWindow.mainloop()

    print("Closing database connection..")
    db.close()

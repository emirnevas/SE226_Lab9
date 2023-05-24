import tkinter as tk
from tkinter import simpledialog, messagebox
import pymysql


class SuperheroFilmDB:
    def __init__(self, root):
        self.root = root
        self.construct_widgets()

        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='yourpassword',
                                          database='yourdatabase')

    # Task 4
    def construct_widgets(self):

        self.selection_menu = tk.OptionMenu(self.root, tk.StringVar())
        self.selection_menu.pack()

        self.output_field = tk.Text(self.root)
        self.output_field.pack()

        self.append_button = tk.Button(self.root, text='Add', command=self.insert_data)
        self.append_button.pack()

        self.show_all_button = tk.Button(self.root, text='List All', command=self.display_all)
        self.show_all_button.pack()

    def insert_data(self):
        # Open dialog box
        film_info = simpledialog.askstring('Add Movie', 'Enter movie info (ID MOVIE DATE MCU_PHASE)')

        if film_info:
            # Parse film_info
            film_id, title, release_date, phase = film_info.split()

            # Add the data to the database
            with self.connection.cursor() as cursor:
                query = f"""
                    INSERT INTO Marvel (ID, MOVIE, DATE, MCU_PHASE)
                    VALUES ({int(film_id)}, '{title}', STR_TO_DATE('{release_date}', '%b%d,%Y'), '{phase}')
                """
                cursor.execute(query)
            self.connection.commit()
            messagebox.showinfo('Success', 'Movie info added successfully')

    # Task 7
    def display_all(self):
        # Fetch and display all data from the database
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM Marvel"
            cursor.execute(query)
            result = cursor.fetchall()

            # Clear output_field
            self.output_field.delete(1.0, tk.END)

            # Insert result into output_field
            for row in result:
                self.output_field.insert(tk.END, ' '.join(str(i) for i in row) + '\n')


root = tk.Tk()

app = SuperheroFilmDB(root)

root.mainloop()

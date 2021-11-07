from tkinter import *
from getpass import getpass
import sqlite3

root = Tk()
root.title('Register Window')
root.iconbitmap('images/admin.ico')
root.geometry('350x250')


'''
# Create table for login
curs.execute("""CREATE TABLE login (
			name text,
			email_register text,
			password_register text,
			confirm_password text
			)""")
'''


# Create register function for database
def register():
	# Create a databases or connect to one
	conn = sqlite3.connect('login_book.db')
	# Create a cursor
	curs = conn.cursor()

	# Insert into a table
	curs.execute('INSERT INTO login VALUES (:name, :email_register, :password_register, :confirm_password)',
			{
			 	'name': name.get(),
			 	'email_register': email.get(),
			 	'password_register': password.get(),
			 	'confirm_password': password_confirmation.get()
			}
		)

	# Clear the text boxes
	name.delete(0, END)
	email.delete(0, END)
	password.delete(0, END)
	password_confirmation.delete(0, END)

	# Commit Changes
	conn.commit()

	# Close connection
	conn.close()


# Create a login function for database
def login():
	global logged
	logged = Tk()
	logged.title('Login Window')
	logged.geometry('350x200')

	# Create a databases or connect to one
	conn = sqlite3.connect('login_book.db')
	# Create a cursor
	curs = conn.cursor()

	
	global email_login, password_login

	# Buttons and Text Boxes for Login Window

	# Create text boxes
	email_login = Entry(logged, width=30)
	email_login.grid(row=0, column=1)

	password_login = Entry(logged, width=30)
	password_login.grid(row=1, column=1)


	# Create text boxes label
	email_label_login = Label(logged, text='email').grid(row=0, column=0, pady=(10, 0))
	password_label_login = Label(logged, text='password').grid(row=1, column=0)

	# Create Confirm Logging Button
	confirm_btn = Button(logged, text='Confirm login credentials', command=check)
	confirm_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

	# Create Login Button
	login_btn = Button(logged, text='Login', state=DISABLED)
	login_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=104)

	# Create an Exit Window Button
	exit_btn = Button(logged, text='Exit Window', command=logged.destroy)
	exit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=104)

	# Commit Changes
	conn.commit()

	# Close connection
	conn.close()

def check():
	# Create a databases or connect to one
	conn = sqlite3.connect('login_book.db')
	# Create a cursor
	curs = conn.cursor()


	# Query the database
	curs.execute('SELECT *, oid FROM login ')
	records = curs.fetchall()

	# Check the login credentials
	for record in records:
		if str(record[1]) == email_login.get():
			if str(record[2]) == str(record[3]) and str(record[2]) == password_login.get():
				login_btn = Button(logged, text='Login', command=app)
				login_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=104)

	# Commit Changes
	conn.commit()

	# Close connection
	conn.close()

def app():
	app = Tk()
	app.title('Calculation of Monthly Expenses')
	app.geometry('400x400')

# Buttons and Text Boxes for Register Window

# Create text boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))

email = Entry(root, width=30)
email.grid(row=1, column=1)

password = Entry(root, width=30)
password.grid(row=2, column=1)

password_confirmation = Entry(root, width=30)
password_confirmation.grid(row=3, column=1)

# Create text boxes label
name_label = Label(root, text='name').grid(row=0, column=0, pady=(10, 0))
email_label = Label(root, text='email').grid(row=1, column=0)
password_label = Label(root, text='password').grid(row=2, column=0)
password_confirmation_label = Label(root, text='confirm password').grid(row=3, column=0)

# Create Register Button
register_btn = Button(root, text='Register', command=register)
register_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=116)

# Create a Login Button
enter_login_btn = Button(root, text='Click Here if you are already registered', command=login)
enter_login_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=36)

# Create an Exit Program Button
exit_btn = Button(root, text='Exit Program', command=root.destroy)
exit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=104)


root.mainloop()
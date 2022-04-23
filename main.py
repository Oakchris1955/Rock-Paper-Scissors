# import the tkinter module
import tkinter as tk

# import random module
import random


# make a window
root = tk.Tk()

# change the window title
root.title('Rock, Paper, Scissors - Made by Oakchris1955')

# define some functions
def select_option():
    selection_list = ['Rock', 'Paper', 'Scissors']
    return selection_list[random.randint(0, 2)]

def insert_on_score_textbox(textbox, message):
	if isinstance(textbox, tk.Text):
		textbox.config(state='normal')
		textbox.delete(1.0, tk.END)
		textbox.insert(tk.END, message)
		textbox.tag_add("right", 1.0, "end")
		textbox.config(state='disabled')
	else:
		raise TypeError('Only Textbox is accepted on this function')

def insert_on_log_textbox(message):
	if isinstance(output, tk.Text):
		output.config(state='normal')
		output.insert(tk.END, message)
		output.tag_add("center", 1.0, "end")
		output.config(state='disabled')
	else:
		raise TypeError('Only output is accepted on this function')


def check_which_wins(user_action, computer_action):
	#check if given arguments are valid text
	for action in [user_action, computer_action]:
		if not isinstance(action, str):
			raise TypeError('All arguments must be strings')
		elif not action in ['Rock', 'Paper', 'Scissors']:
			raise KeyError('All arguments must be either Rock, Paper or Scissors')

	# use some if-statements to define the winner
	if user_action == computer_action:
		return 'Both win'

	elif user_action == 'Rock':
		if computer_action == 'Scissors':
			return 'User wins'
		else:
			return 'Computer wins'
	elif user_action == 'Scissors':
		if computer_action == 'Paper':
			return 'User wins'
		else:
			return 'Computer wins'
	elif user_action == 'Paper':
		if computer_action == 'Rock':
			return 'User wins'
		else:
			return 'Computer wins'


def on_click(widget):

	# define some variables
	button_dict = {'Rock': rock, 'Paper': paper, 'Scissors': scissors}


	# get user selection and print it
	user_selection = widget['text']
	print(f'User selection: {user_selection}')

	# make computer select a random option
	computer_selection = select_option()
	print(f'Computer selection: {computer_selection}\n')


	# change all button's bg to normal
	for button in button_dict.values():
		button.config(background='SystemButtonFace')

	# update button background color: cyan for user, grey for computer and dark cyan if the same was chosen
	if user_selection == computer_selection:
		button_dict[user_selection].config(bg='#55a1aa')
		insert_on_log_textbox('Tie. No one gets a point\n')
	else:
		button_dict[user_selection].config(bg='cyan')
		button_dict[computer_selection].config(bg='grey')

		if check_which_wins(user_selection, computer_selection) == 'User wins':
			insert_on_score_textbox(user_textbox, str(int(user_textbox.get(1.0, 'end'))+1))
			insert_on_log_textbox(f'User: {user_selection} - Computer: {computer_selection}. User gains one (1) point\n')
		elif check_which_wins(user_selection, computer_selection) == 'Computer wins':
			insert_on_score_textbox(computer_textbox, str(int(computer_textbox.get(1.0, 'end'))+1))
			insert_on_log_textbox(f'User: {user_selection} - Computer: {computer_selection}. Computer gains one (1) point\n')
		


# load the images
images = {"rock": tk.PhotoImage(file="images/rock.png"),
          "paper": tk.PhotoImage(file="images/paper.png"),
          "scissors": tk.PhotoImage(file="images/scissors.png")}


# make the buttons
rock = tk.Button(root, text='Rock',
                 image=images['rock'], borderwidth=0, command=lambda: on_click(rock))
paper = tk.Button(root, text='Paper',
                  image=images['paper'], borderwidth=0, command=lambda: on_click(paper))
scissors = tk.Button(root, text='Scissors',
                     image=images['scissors'], borderwidth=0, command=lambda: on_click(scissors))

# grid them
rock.grid(row=1, column=0, columnspan=2)
paper.grid(row=2, column=0)
scissors.grid(row=2, column=1)

# add an output label and grid it
output = tk.Text(root, height=10, width=63)
output.grid(row=3, column=0, columnspan=2)
output.tag_configure("center", justify='center')
output.insert(tk.END, "Computer: Click a button\n")
output.tag_add("center", "1.0", "end")
output.config(state=tk.DISABLED)

# also, add a score frame with labels on it
score_frame = tk.Frame()
score_frame.grid(row=0, column=0, columnspan=2)

score_label = tk.Label(score_frame, text='Score')
score_label.grid(row=0, column=0, columnspan=5)

computer_label = tk.Label(score_frame, text='Computer', font=("Comic Sans", 23))
user_label = tk.Label(score_frame, text='User', font=("Comic Sans", 23))
middle_label = tk.Label(score_frame, text='-', font=("Comic Sans", 23))
computer_label.grid(row=0, column=0, padx=3)
user_label.grid(row=0, column=4, padx=3)
middle_label.grid(row=0, column=2, padx=5)

computer_textbox = tk.Text(score_frame, height=1, width=3, font=("Comic Sans", 23))
computer_textbox.grid(row=0, column=1)
user_textbox = tk.Text(score_frame, height=1, width=3, font=("Comic Sans", 23))
user_textbox.grid(row=0, column=3)

for textbox in [computer_textbox, user_textbox]:
	textbox.tag_configure("right", justify='right')
	insert_on_score_textbox(textbox, 0)

# run window until closed by user
root.mainloop()

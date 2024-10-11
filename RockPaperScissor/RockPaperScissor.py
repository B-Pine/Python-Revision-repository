import random
import tkinter

from PIL import Image, ImageTk


def computer_move():
    """Generate move of the computer randomly"""
    return random.choice(['rock', 'paper', 'scissor'])


def update_score_history():
    score_history.set(f"Wins: {wins}, Losses: {losses}, Ties: {tie}")


def result_generator(player_pick):
    global wins
    global losses
    global tie

    computer_pick = computer_move()
    comp_pick_name.set(computer_pick)

    if computer_pick == 'rock':
        if player_pick == 'paper':
            result_label.set('You win.')
            wins += 1
        elif player_pick == 'scissor':
            result_label.set('Comp win.')
            losses += 1
        else:
            result_label.set('Tie.')
            tie += 1

    elif computer_pick == 'paper':
        if player_pick == 'paper':
            result_label.set('Tie.')
            tie += 1
        elif player_pick == 'scissor':
            result_label.set('You win.')
            wins += 1
        else:
            result_label.set('Comp win.')
            losses += 1

    else:
        if player_pick == 'paper':
            result_label.set('Comp win.')
            losses += 1
        elif player_pick == 'scissor':
            result_label.set('Tie.')
            tie += 1
        else:
            result_label.set('You win.')
            wins += 1

    update_score_history()


def player_rock():
    player_pick_name.set('rock')
    result_generator('rock')


def player_paper():
    player_pick_name.set('paper')
    result_generator('paper')


def player_scissor():
    player_pick_name.set('scissor')
    result_generator('scissor')


def reset_score():
    """To reset the score history to zero"""
    global wins
    global losses
    global tie

    wins = losses = tie = 0
    update_score_history()


def image_resized(size, image_path='images/PY_VAR1.png'):
    """Resize the image in specified size"""
    image = Image.open(image_path)
    image = image.resize((size, size))
    return ImageTk.PhotoImage(image)


# Setting GUI
master = tkinter.Tk()
master.title("PineDev RPS")
master.geometry('640x480')
master.configure(background='black', padx=20)

label_title = tkinter.Label(master, text="Rock Paper Scissor",
                            font=('Verdana', 20),
                            background='black', fg='white')
label_title.grid(row=0, column=0, columnspan=3)

# Defining gameFrame
gameFrame = tkinter.Frame(master, background='black')
gameFrame.grid(row=1, column=0, columnspan=3, rowspan=5)

# Keep references to the images to prevent them from being garbage collected
rock_image = image_resized(110, 'images/rock.png')
paper_image = image_resized(110, 'images/paper.png')
scissor_image = image_resized(110, 'images/scissor.png')

# Adding widget for playing icons
# Rock widget
# noinspection PyTypeChecker
rock_button = tkinter.Button(gameFrame, text='click Me!',
                             image=rock_image, command=player_rock)
rock_button.grid(row=0, column=0, sticky='n')
# Paper widget
# noinspection PyTypeChecker
paper_button = tkinter.Button(gameFrame, image=paper_image,
                              command=player_paper)
paper_button.grid(row=0, column=1, sticky='n')
# Scissor widget
# noinspection PyTypeChecker
scissor_button = tkinter.Button(gameFrame, image=scissor_image,
                                command=player_scissor)
scissor_button.grid(row=0, column=2, sticky='n')

# Result Widgets
resultFrame = tkinter.Frame(gameFrame, background='black')
resultFrame.grid(row=1, column=0, rowspan=2, columnspan=2)
# Result label
result_label = tkinter.StringVar()
tkinter.Label(resultFrame, textvariable=result_label, background='black',
              fg='white', font='15').grid(row=0, column=0, columnspan=2,
                                          sticky='w')
# Result details
tkinter.Label(resultFrame, text='You', background='black',
              fg='white').grid(row=1, column=0, sticky='ws')

player_pick_name = tkinter.StringVar()
# noinspection PyTypeChecker
tkinter.Label(resultFrame, textvariable=player_pick_name,
              relief='sunken').grid(
    row=1, column=1, sticky='n')

comp_pick_name = tkinter.StringVar()
# noinspection PyTypeChecker
tkinter.Label(resultFrame, textvariable=comp_pick_name, relief='sunken').grid(
    row=1, column=2, sticky='n')

tkinter.Label(resultFrame, text='Computer', background='black',
              fg='white').grid(row=1, column=3, sticky='es')

# Result history
wins = 0
losses = 0
tie = 0

score_history = tkinter.StringVar()
update_score_history()
(tkinter.Label(resultFrame, textvariable=score_history, bg='black', fg='white')
 .grid(row=2, column=0, columnspan=4))

# Reset score button
tkinter.Button(resultFrame, text='Reset score', command=reset_score).grid(
    row=3, column=0)

tkinter.mainloop()

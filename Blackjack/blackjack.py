import tkinter
import random


def load_images(card_image):
    # loading images on the frame
    suits = ['diamond', 'heart', 'spade', 'club']
    face_cards = ['jack', 'king', 'queen']

    for suit in suits:
        for card in range(1, 11):
            image_path = f"cards/{str(card)}_{suit}.png"
            image_obj = tkinter.PhotoImage(file=image_path)
            card_image.append((card, image_obj))

    for card in face_cards:
        for suit in suits:
            image_path = f"cards/{card}_{suit}.png"
            image_obj = tkinter.PhotoImage(file=image_path)
            card_image.append((10, image_obj))


def deal_card(frame):
    # Removing the first card from the shuffles deck
    next_card = deck.pop(0)
    # Adding removed card on the back of deck
    deck.append(next_card)
    # Adding next card to a frame
    tkinter.Label(frame, image=next_card[1], relief='sunken',
                  background='green').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            score = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)

    if player_score > 21:
        winner.set("Dealer Wins!")


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        winner.set('Dealer Wins!')
    elif dealer_score > 21 or dealer_score < player_score:
        winner.set('Player Wins')
    elif dealer_score > player_score:
        winner.set('Dealer Wins!')
    else:
        winner.set('Draw!')


def initials():
    """Contains the codes to draw the first 3 cards 2 for players and 1 for
    the dealer"""
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(mainFrame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold the card images
    player_card_frame = tkinter.Frame(mainFrame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    winner.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    initials()


def play_game():
    """Initiate the game"""
    initials()

    master.mainloop()


# Setting up GUI
master = tkinter.Tk()
master.title("Black Jack")
master.geometry("640x480")
master.configure(background='green')

winner = tkinter.StringVar()
label = tkinter.Label(master, textvariable=winner)
label.grid(row=0, column=0, columnspan=3)

mainFrame = tkinter.Frame(master, background="green",
                          relief='sunken', borderwidth=2)
mainFrame.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='ew')

# widget for dealer
tkinter.Label(mainFrame, text="Dealer", background="green",
              fg='white').grid(row=0, column=0)
dealer_score_label = tkinter.IntVar()
tkinter.Label(mainFrame, textvariable=dealer_score_label,
              background='green', fg='white').grid(row=1, column=0)

# Dealer card frame
dealer_card_frame = tkinter.Frame(mainFrame, background='green')
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')

# Widget for player
player_score_label = tkinter.IntVar()
tkinter.Label(mainFrame, text='Player', background='green',
              fg='white').grid(row=2, column=0)
tkinter.Label(mainFrame, textvariable=player_score_label, background='green',
              fg='white').grid(row=3, column=0)

# Player card frame
player_card_frame = tkinter.Frame(mainFrame, background='green')
player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

# Adding button frame
button_frame = tkinter.Frame(mainFrame, background='green')
button_frame.grid(row=4, column=0, sticky='w', columnspan=3)
# Dealer button
(tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
 .grid(row=0, column=0))

# Player button
(tkinter.Button(button_frame, text="Player", command=deal_player)
 .grid(row=0, column=1))
# New game Button
tkinter.Button(button_frame, text="New Game", command=new_game).grid(row=0,
                                                                     column=2)

cards = []
load_images(cards)
deck = list(cards)

random.shuffle(deck)
# print(deck)

player_hand = []
dealer_hand = []

if __name__ == "__main__":
    play_game()
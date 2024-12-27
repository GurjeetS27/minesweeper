#Gurjeet Singh
#Minesweeper GUI

import tkinter as tk
import random
import time

# Create a new board of board size and set random mines
def makeboard(board_size, mines):
    board = [[0] * board_size for _ in range(board_size)]

    # Set the bombs
    set_bombs = 0
    while set_bombs < mines:
        #randomly selects the row and col
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)

        if board[row][col] == 'M':
            continue

        board[row][col] = 'M'
        set_bombs += 1

    return board

# Calculate the number of neighboring bombs
def neighboring_bombs(board, row, col):
    adjacent_cells = 0
    for r in range(max(0, row - 1), min(len(board) - 1, row + 1) + 1):
        for c in range(max(0, col - 1), min(len(board[0]) - 1, col + 1) + 1):
            if (r, c) == (row, col):
                continue
            if board[r][c] == 'M':
                adjacent_cells += 1
    return adjacent_cells

#For all the empty spaces, representing the number of neighboring bombs
def assign_values_to_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != 'M':
                board[r][c] = neighboring_bombs(board, r, c)

#Select the choice in board at that location
def select_choice(board, users_choice, row, col):
    if (row, col) in users_choice:
        return True
    users_choice.add((row, col))
    if board[row][col] == 'M':
        return False
    elif board[row][col] > 0:
        return True

    for r in range(max(0, row - 1), min(len(board) - 1, row + 1) + 1):
        for c in range(max(0, col - 1), min(len(board[0]) - 1, col + 1) + 1):
            select_choice(board, users_choice, r, c)

    return True

# Render the board to the player
def render_board(board, users_choice):
    string_rep = ''
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if (i, j) in users_choice:
                string_rep += str(cell)
            else:
                string_rep += ' '
            string_rep += ' | '
        string_rep = string_rep[:-3]
        string_rep += '\n'
    return string_rep

#Save results to the text file
def save_result(board, users_choice, moves, result):
    with open('result.txt', 'w') as file:
        file.write(f"Result: {result}\n\n")
        file.write("Full Board:\n")
        file.write(render_board(board, users_choice))
        file.write("\nList of Moves:\n")
        for move in moves_list:
            file.write(f"{move[0]},{move[1]}, Action: {move[2]}\n")

#main function to play the game
#starts by creating a new board with the default size of 9 and 10 mines
def play(board_size=9, mines=10):
    """
    Function to play the Minesweeper game.

    Args:
        board_size (int): The size of the game board. Default is 9.
        mines (int): The number of mines in the game. Default is 10.
    """
    board = makeboard(board_size, mines)
    assign_values_to_board(board)

    global moves_list
    moves_list = []

    # Rest of the code...
def play(board_size=9, mines=10):
    board = makeboard(board_size, mines)
    assign_values_to_board(board)

    global moves_list
    moves_list = []

    #creates tkinter window
    root = tk.Tk()
    root.title("Minesweeper")

    buttons = []

    #restart the game by using destroy to destroy current gameplay
    def restart_game():
        root.destroy()
        play()

    #reveals the content of the cell and returns the answer acccording to user choice
    def reveal_cell(row, col):
        nonlocal safe
        if (row, col) not in users_choice:
            users_choice.add((row, col))
            if board[row][col] == 'M':
                safe = False
                game_over()
            elif board[row][col] == 0:
                for r in range(max(0, row - 1), min(board_size - 1, row + 1) + 1):
                    for c in range(max(0, col - 1), min(board_size - 1, col + 1) + 1):
                        reveal_cell(r, c)
            buttons[row][col].config(text=str(board[row][col]), state='disabled')
            moves_list.append((row, col, "reveal"))
        check_win()

    #flags the cell if user right clicks on the cell
    def flag_cell(row, col):
        if (row, col) not in users_choice:
            if buttons[row][col].cget("text") == "Flag":
                buttons[row][col].config(text="", bg="black", state='normal')
            else:
                buttons[row][col].config(text="Flag", bg="orange", state='disabled')
        moves_list.append(row, col, "flag")        

    #game over function with setting restart button to normal state
    def game_over():
        nonlocal safe
        safe = False
        for r in range(board_size):
            for c in range(board_size):
                users_choice.add((r, c))
                if board[r][c] == 'M':
                    buttons[r][c].config(text="M", bg="red", state='disabled')
        result_label.config(text="Lost, Good Luck Next Time :)")
        restart_button.config(state='normal')
        timer_label.after_cancel(timer_update)

    #checks if the user has won the game
    def check_win():
        if len(users_choice) == board_size ** 2 - mines:
            for r in range(board_size):
                for c in range(board_size):
                    if board[r][c] == 'M':
                        buttons[r][c].config(text="Flag", state='disabled')
            result_label.config(text="CONGRATULATIONS!")

    users_choice = set()
    safe = True

    #creates the board with buttons and labels
    for i in range(board_size):
        button_row = []
        for j in range(board_size):
            btn = tk.Button(root, text="", bg="white", height=2, width=4,
                            command=lambda row=i, col=j: reveal_cell(row, col))
            btn.grid(row=i, column=j)
            button_row.append(btn)
            btn.bind("<Button-3>", lambda event, row=i, col=j: flag_cell(row, col))
        buttons.append(button_row)

    
    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.grid(row=board_size, columnspan=board_size)

    restart_button = tk.Button(root, text="Restart", font=("Helvetica", 16),
                               command=restart_game, state='disabled')
    restart_button.grid(row=board_size + 2, columnspan=board_size)

    def update_timer():
        nonlocal start_time
        elapsed_time = time.time() - start_time

        #check if 60 seconds have passed
        if elapsed_time >=60:
            elapsed_minutes = int(elapsed_time / 60)
            elapsed_seconds = int(elapsed_time % 60)
            timer_label.config(text=f"Time: {elapsed_minutes} minutes {elapsed_seconds} seconds")

        else:
            timer_label.config(text = f"Time: {int(elapsed_time)} seconds")

        global timer_update
        timer_update = timer_label.after(1000, update_timer)

    start_time = time.time()
    timer_label = tk.Label(root, text="Time: 0 seconds", font=("Helvetica", 16))
    timer_label.grid(row=0, column=board_size, sticky="ne")

    update_timer()  # Start the timer
    root.mainloop()

    if safe:
        result = "Won"
    else:
        result = "Lost"

    save_result(board, users_choice, [], result)
    timer_label.after_cancel(timer_update)

play()

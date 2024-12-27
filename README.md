Minesweeper Game
----------------

A Python-based GUI implementation of the classic Minesweeper game using the `tkinter` library. This project is designed for both beginners and advanced programmers to explore interactive GUI development and logic-based gameplay.

### Features

* **Classic Minesweeper Gameplay**: Navigate through a grid, avoiding hidden mines while uncovering cells.
* **Graphical User Interface (GUI)**: Built with the `tkinter` library for an intuitive and interactive experience.
* **Timer**: Tracks the time spent on each game.
* **Restart Button**: Restart the game at any point with a single click.
* **Flagging System**: Right-click to flag potential mines.
* **Game Results**: Displays whether you win or lose, with mines visually marked on the board.
* **Result Saving**: Saves the game board and moves to a text file for review.

### Installation

1. Clone the repository:
git clone https://github.com/GurjeetS27/minesweeper.git cd minesweeper
2. Ensure you have Python 3.x installed on your system.
3. Install any required dependencies (if needed):
  pip install -r requirements.txt

*(Note: `tkinter` is typically included with Python installations.)*

### How to Play

1. Run the script:
   python minesweeper.py
2. A Minesweeper game window will appear with a grid of buttons.

3. **Gameplay**:
  * Left-click to reveal a cell.
  * Right-click to flag a cell as a potential mine.
  * The numbers in revealed cells indicate how many neighboring mines exist.

4. **Winning Condition**:
  * Uncover all cells without triggering a mine.

5. **Losing Condition**:
  * Clicking on a mine ends the game.

6. Restart the game using the "Restart" button.

### File Structure

  * `minesweeper.py`: The main game logic and GUI code.
  * `result.txt`: A text file where game results (board state and moves) are saved.

### Future Enhancements

  * Add difficulty levels (Easy, Medium, Hard).
  * Implement a hint system to assist players.
  * Introduce animations and sound effects for a more engaging experience.
  * Add a leaderboard to track best times.

### Screenshots

#### Game Interface
![image](https://github.com/user-attachments/assets/62111b3a-d32d-4b07-a3d0-86808c97cc8f)



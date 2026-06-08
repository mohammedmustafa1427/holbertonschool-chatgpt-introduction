#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Ensure we don't try to place more mines than available cells
        num_mines = min(mines, width * height)
        self.mines = set(random.sample(range(width * height), num_mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # Adjusted formatting to accommodate double-digit grid coordinates gracefully
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2}', end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print(' *', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f'{count:2}' if count > 0 else '  ', end=' ')
                else:
                    print(' .', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
            
        # Prevent redundant checks if already revealed
        if self.revealed[y][x]:
            return True
            
        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        # The game is won if the number of revealed cells equals the total safe cells
        revealed_count = sum(row.count(True) for row in self.revealed)
        safe_cells = (self.width * self.height) - len(self.mines)
        return revealed_count == safe_cells

    def play(self):
        while True:
            self.print_board()
            
            # Check for win condition before asking for next move
            if self.check_win():
                self.print_board(reveal=True)
                print("\nCongratulations! You cleared all the mines and won!")
                break
                
            try:
                x = int(input("\nEnter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                # Input boundary validation to prevent IndexError crashes
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Out of bounds! X must be 0-{self.width-1} and Y must be 0-{self.height-1}.")
                    input("Press Enter to continue...")
                    continue
                    
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\nGame Over! You hit a mine.")
                    break
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...") # Pauses so the user can read the error

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
    
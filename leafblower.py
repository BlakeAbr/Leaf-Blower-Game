import pyautogui
import time
import keyboard

def move_mouse_square_continuous():
    while True:
        # Get the screen dimensions
        screen_width, screen_height = pyautogui.size()
        
        # Define the square path
        square_path = [
            (100, 100),  # Top-left corner
            (screen_width - 100, 100),  # Top-right corner
            (screen_width - 100, screen_height - 100),  # Bottom-right corner
            (100, screen_height - 100),  # Bottom-left corner
        ]
        
        # Define the diagonal path (from bottom-left corner to top-right corner)
        diagonal_path = [
            (100, 100),  # Top-left corner
            (screen_width - 100, screen_height - 100),  # Bottom-right corner
            (screen_width - 100, 100),  # Top-right corner
            (100, screen_height - 100),  # Bottom-left corner
        ]

        # Define the duration for each leg of the square (in seconds)
        duration = 2

        # Loop indefinitely to continuously move the mouse along the square path
        for x, y in square_path:
            pyautogui.moveTo(x, y, duration=duration)
            time.sleep(1)  # Wait for 1 second between moves
            
            # Check if "\" key is pressed
            if keyboard.is_pressed("\\"):
                print("Backslash key pressed. Stopping script.")
                return  # Stop the script if "\" key is pressed

        for diagonal_x, diagonal_y in diagonal_path:
            pyautogui.moveTo(diagonal_x, diagonal_y, duration=duration)
            time.sleep(1)  # Wait for 1 second between moves

if __name__ == "__main__":
    move_mouse_square_continuous()
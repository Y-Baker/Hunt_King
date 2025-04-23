import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()
# Get the environment variables
BOARD_ROWS = int(os.getenv("BOARD_ROWS", 5))
BOARD_COLS = int(os.getenv("BOARD_COLS", 5))

# Set default values if not provided
if BOARD_ROWS <= 0 or BOARD_COLS <= 0:
    raise ValueError("BOARD_ROWS and BOARD_COLS must be positive integers.")

# Check if the board size is within reasonable limits
if BOARD_ROWS > 10 or BOARD_COLS > 10:
    raise ValueError("BOARD_ROWS and BOARD_COLS must be less than or equal to 10.")

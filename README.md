# Silent Auction Program

This project is a Python-based **Silent Auction Program** where multiple bidders can anonymously place their bids. At the end of the bidding, the program determines and announces the winner with the highest bid.

---

## Features

1. **Multiple Bidders**:
   - Allows multiple users to place their bids.
   - Supports anonymous bidding by clearing the screen after each bid.

2. **Dynamic Winner Selection**:
   - Automatically identifies the highest bidder at the end of the auction.

3. **Interactive Interface**:
   - Provides a simple and user-friendly way to input bids and check for more participants.

4. **Cross-Platform Console Clear**:
   - Uses `os.system('cls')` to clear the console for a clean interface (works on Windows).

---

## How It Works

1. The program greets the user with a welcome message.
2. Each bidder enters their name and their bid price.
3. After each bid, the program asks if there are more bidders:
   - If `yes`, the screen is cleared, and the next bidder can place their bid.
   - If `no`, the auction ends, and the program announces the winner.
4. The winner is determined by comparing all bid prices.

---

## Code Structure

### **Function: `find_winner(winner_detalis)`**
- Takes a dictionary of bidder names and their bid prices.
- Iterates through the dictionary to find the highest bid.
- Prints the winner's name and bid amount.

### **Main Program Flow**
1. Initializes an empty dictionary `winner` to store bids.
2. Uses a `while` loop to collect bids until no more bidders are present.
3. Calls `find_winner()` to determine the winner at the end.

---

## How to Run

1. Clone the repository or download the script:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Run the script:
   ```bash
   python silent_auction.py
   ```

---

## Example Usage

### Sample Input:
```plaintext
#### WELCOME TO THE SILENT AUCTION PROGRAM ####
Enter your Name: Alice
Enter your bid Price: 150
Are there more Bidders? 'yes' or 'no':
 yes

Enter your Name: Bob
Enter your bid Price: 200
Are there more Bidders? 'yes' or 'no':
 no
```

### Output:
```plaintext
The bidder is Bob and the price is 200
```

---

## Customization

### Changing the Currency:
You can modify the `price` input prompt to reflect a specific currency:
```python
price = int(input("Enter Your bid Price in USD: "))
```

### Cross-Platform Screen Clearing:
Replace `os.system('cls')` with a platform-independent solution:
```python
import os
os.system('cls' if os.name == 'nt' else 'clear')
```

---

## Dependencies
- Python 3.6 or higher
- `os` module (for clearing the console)

---

## Limitations
- The program does not handle ties (two bidders with the same highest bid).
- Only numeric bids are accepted; any invalid input will result in a crash.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contact
For questions or feedback, please contact Shajan J Jacob.


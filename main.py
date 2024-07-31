import random

MAX_VALUES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def deposit():
    while True:
        amount = input("Insert amount $:")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("Amount cannot be 0.")
        else:
            print("Enter Valid Amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Insert number of lines to bet on (1-" + str(MAX_VALUES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if (lines > 0):
                break
            else:
                print("Lines cannot be 0.")
        else:
            print("Enter Valid Lines")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each lines? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter Valid Bet")
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    # stores all the symbols based on there occurances
    all_symbols = []
    # looping through the symbol counts and appending the symbol in array
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # randomly choosing symbol and adding it to each columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_change(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def spin(balance):
    # stores number of lines the bet to be placed
    lines = get_number_of_lines()
    # checks if bet is possible by checking the balance amount
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if(total_bet > balance):
            print(f"You do not have enough balance to bet!!, Your current balance: {balance}")
        else:
            break
    print(f"You are betting on ${bet} on {lines} lines. Total bet is equal to :${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_change(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won: ${winnings}. ")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet


def main():
    # stores deposits
    balance = deposit()
    # keeps playing until you run out of money💸 or quit Yourself
    while True:
        print(f"Current Balance is : ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        else:
            balance += spin(balance)

    print(f"You left with ${balance}")

main()
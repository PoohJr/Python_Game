MAX_LINES = 3 #in all caps due to being a const like js cause this var wont change 
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Gotta be More then 0.")

        print("please enter a number")

    return amount

def get_bet():
    while True:
        amount = input("What would you like to Bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <=  amount <= MAX_BET:
                break
            else:
                print(f"Gotta be between ${MIN_BET} - ${MAX_BET}.")

        print("please enter a number")

    return amount


def get_number_of_lines():
        while True:
            lines = input("Enter te number of Lines you wanna bet on (1-" + str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("enter a valid numer of lines")

            print("please enter a number")

        return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet + lines

        if total > balance:
            print(f"You do not have enougt to bet that amount, your balance is: ${balance}")
        else:
            break
    print(f"Your are betting ${bet} on {lines}. Total bet is equal to ${total}")


main()

import string


def complexity(password):
    plength = len(password)
    upper = any(char in string.ascii_uppercase for char in password)
    lower = any(char in string.ascii_lowercase for char in password)
    number = any(char in string.digits for char in password)
    character = any(char in string.punctuation for char in password)

    with open('rockyou.txt', 'r') as f:
        common = f.read().splitlines()

    score = 0
    if password in common:
        print("Your password is used commonly.")
        print("Your password can be compromised easily!")

    if plength >= 16:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if number:
        score += 1
    if character:
        score += 1

    return score


def strength(password):
    score = complexity(password)

    if score == 5:
        percentage = (score / 5) * 100
        time_req = 'Billion Years!'
        print("\nPassword Complexity: Strong")
        print(f"Strength: {round(percentage, 2)}%")
        print(f"Required Time To Brute Force: {time_req}")

    elif score >= 3:
        percentage = (score / 5) * 100
        if len(password) >= 16:
            time_req = 'Million Years!'
        else:
            time_req = "Few weeks to Years!"
        print("\nPassword Complexity: Medium")
        print(f"Strength: {round(percentage, 2)}%")
        print(f"Required Time To Brute Force: {time_req}")
    else:
        percentage = (score / 5) * 100
        time_req = 'Few seconds to Days'
        print("\nPassword Complexity: Weak")
        print(f"Strength: {round(percentage, 2)}%")
        print(f"Required Time To Brute Force: {time_req}")


def run_program():
    password = input("Enter your Password to analyse (Min. 4 to Max. 32 Characters): ")

    if len(password) > 32 or len(password) < 4:
        print("Please enter your password in the range of 4 to 32 characters.")
    else:
        print(f"Password Length: {len(password)}")
        strength(password)

    run_again = input("\nDo you want to check another Password? (y/n): ").lower()
    if run_again == 'y':
        run_program()
    else:
        print("Exiting the program.")


run_program()

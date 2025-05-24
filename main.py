import sys
from src.gen import Generator


def ask_yes_no(prompt):
    return input(prompt + " (y/n): ").strip().lower() == 'y'


def ask_length(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == '__main__':
    args = sys.argv[1:]
    gen = Generator()

    userlen = None
    passlen = None
    pinlen = None

    generate_user = False
    generate_pass = False
    generate_pin = False

    # Parse arguments if provided. If an argument is provided, it will only generate that argument.
    for arg in args:
        if arg.startswith("userlen="):
            userlen = int(arg.split("=")[1])
            generate_user = True
        elif arg.startswith("passlen="):
            passlen = int(arg.split("=")[1])
            generate_pass = True
        elif arg.startswith("pinlen="):
            pinlen = int(arg.split("=")[1])
            generate_pin = True

    # If no arguments are provided, ask the user for input
    if not args:
        generate_user = ask_yes_no("Do you want to generate a username?")
        generate_pass = ask_yes_no("Do you want to generate a password?")
        generate_pin = ask_yes_no("Do you want to generate a PIN?")

    # Ask for lengths only if needed
    if generate_user and userlen is None:
        userlen = ask_length("How long do you want your username: ")
    if generate_pass and passlen is None:
        passlen = ask_length("How long do you want your password: ")
    if generate_pin and pinlen is None:
        pinlen = ask_length("How long do you want your PIN: ")

    # Perform generation at the end
    print("\n--- Generated Output ---")
    if generate_user:
        print("Generated F.Username: " + gen.generate_username(userlen))
        print("Generated human-readable username: " +
              gen.generate_human_readable_username(userlen))
    if generate_pass:
        print("Generated Password: " + gen.generate_password(passlen))
    if generate_pin:
        print("Generated PIN: " + gen.generate_pin(pinlen))

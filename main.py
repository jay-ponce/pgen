import argparse
from src.gen import Generator


def ask_yes_no(prompt):
    return input(prompt + " (y/n): ").strip().lower() == 'y'


def ask_length(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    parser = argparse.ArgumentParser(description="Credential Generator")

    # Username arguments
    parser.add_argument('--userlen', type=int, help="Length of the username")
    parser.add_argument(
        '--userstyle', choices=['readable', 'random'], help="Username style")

    # Password arguments
    parser.add_argument('--passlen', type=int, help="Length of the password")

    # PIN arguments
    parser.add_argument('--pinlen', type=int, help="Length of the PIN")

    args = parser.parse_args()
    gen = Generator()

    # Flags based on arguments
    generate_user = args.userlen is not None
    generate_pass = args.passlen is not None
    generate_pin = args.pinlen is not None

    # Interactive fallback if no args
    if not any([generate_user, generate_pass, generate_pin]):
        generate_user = ask_yes_no("Do you want to generate a username?")
        generate_pass = ask_yes_no("Do you want to generate a password?")
        generate_pin = ask_yes_no("Do you want to generate a PIN?")

    if generate_user and args.userlen is None:
        args.userlen = ask_length("How long do you want your username: ")
    if generate_pass and args.passlen is None:
        args.passlen = ask_length("How long do you want your password: ")
    if generate_pin and args.pinlen is None:
        args.pinlen = ask_length("How long do you want your PIN: ")

    print("\n--- Generated Output ---")
    if generate_user:
        if args.userstyle == "readable":
            print("Generated human-readable username:",
                  gen.generate_human_readable_username(args.userlen))
        else:
            print("Generated random username:",
                  gen.generate_username(args.userlen))
    if generate_pass:
        print("Generated Password:", gen.generate_password(
            args.passlen
        ))
    if generate_pin:
        print("Generated PIN:", gen.generate_pin(args.pinlen))


if __name__ == '__main__':
    main()

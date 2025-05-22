from src.gen import Generator
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python main.py <username_length> <password_length> <pin_length>")
        sys.exit(1)

    # Read arguments from the command line
    userlen = int(sys.argv[1])
    passlen = int(sys.argv[2])
    pinlen = int(sys.argv[3])

    gen = Generator()

    # userlen = input("How long do you want your username: ")
    # passlen = input("How long do you want your password: ")
    # pinlen = input("How long do you want your PIN: ")
    # strict_mode = input("Use strict PIN mode? (y/n): ").lower() == 'y'

    print("\nGenerated F.Username: " + gen.generate_username(userlen))
    print("Generated human readbale username: " +
          gen.generate_human_readable_username(userlen))
    print("Generated Password: " + gen.generate_password(passlen))
    print("Generated PIN: " + gen.generate_pin(pinlen))

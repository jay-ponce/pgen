# Random Credential Generator

This Python program generates random **usernames**, **passwords**, and **PINs** for use in various applications where secure, unique credentials are needed. It serves as a basic tool for experimenting with randomness and user input.

---

## ❓ Why This Project?

Most online password generators are cloud-based, meaning the password is created on a remote server. That comes with two major problems:

1. **Weak Security Practices**: Many generators produce passwords that are not truly random or don't use the full range of secure characters, making them easier to crack.
2. **Privacy Concerns**: Since passwords are generated server-side, it's impossible to know if they are being stored, logged, or even associated with your IP address or device.

**This project generates passwords entirely on your local machine**, meaning:
- No passwords are sent over the internet.
- No tracking or storage of generated data.
- You stay in full control of your credentials.

This tool is designed with **privacy, security, and transparency** in mind.

---

## 🔧 Features (Current)

✅ **Selective Credential Generation**

  - Generate only the credentials you want — username, password, or PIN — via command-line arguments or prompts.
  - Skips prompts entirely if you supply arguments explicitly.

✅ **Random Username Generator**  
  - Generates usernames composed of random characters, optionally mixed with a randomly generated number.  
  - Two types: one using random characters, another using adjective+noun+number randomly.

✅ **Random Password Generator**  
  - Generates a password of user-defined length using ASCII characters between 33 (`!`) and 125 (`}`), including special characters.

✅ **Random PIN Generator**  
  - Generates numeric PINs of a user-defined length

---

## 🛠 Planned Features

- [ ] Add options for character types (e.g., include/exclude digits, special characters, uppercase).
- [ ] Add persistent storage (e.g., saving credentials to a file securely).
- [ ] GUI or Web Interface (long-term goal).

---

## 🖥 How to Run

You can run the credential generator in two ways: interactively or with command-line flags.

### 🔹 Option 1: Fully Interactive Mode


Run the script without any flags:

```
python main.py
```

You’ll be asked whether you want to generate a username, password, and/or PIN. If you say yes to any, you’ll be prompted for the desired length.

```
Do you want to generate a username? (y/n): y
Do you want to generate a password? (y/n): y
Do you want to generate a PIN? (y/n): n
How long do you want your username: 10
How long do you want your password: 16
```

This is a quick and guided way to generate one or more credentials manually.

### 🔹 Option 2: Command-Line Flags

You can bypass the prompts and specify everything directly:

```
python main.py --userlen=8 --passlen=16 --pinlen=4
```

This generates:
	•	A username of length 8
	•	A password of length 16
	•	A numeric PIN of length 4


You can generate only what you need:
```
python main.py --userlen=12 --passlen=20
```

Only generates the username and password with the specified lengths. PIN is skipped unless specified.

Accepted Arguments:
	•	userlen=<int> — Length of the username.
	•	passlen=<int> — Length of the password.
	•	pinlen=<int> — Length of the PIN.

### 🔹 Optional: Username Style

You can also control the username format:

```
--userstyle=readable    # Generates a human-friendly username (e.g., BraveTiger42)
--userstyle=random      # Generates a fully random string (default behavior)
```

Used with:

```
python main.py --userlen=10 --userstyle=readable
```

### 📋 Available Flags
| 🔧 Flag                  | 📄 Description                                       |
|:-------------------------|:----------------------------------------------------|
| `--userlen <int>`        | Length of the username                              |
| `--userstyle <style>`    | Username style: `readable` or `random`              |
| `--passlen <int>`        | Length of the password                              |
| `--pinlen <int>`         | Length of the numeric PIN                           |

---
## 📌 Example Output

```
$ python main.py --userlen=11 --userstyle=readable --passlen=12

--- Generated Output ---
Generated human-readable username: unrAvell1ng
Generated Password: M`mSCv,4WlK'

$ python main.py
Do you want to generate a username? (y/n): y
Do you want to generate a password? (y/n): y
Do you want to generate a PIN? (y/n): n
How long do you want your username: 10
How long do you want your password: 16

--- Generated Output ---
Generated F.Username: 3A010ruiS1
Generated Password: }mw:Gm5|9/k]p&{w
```

---

## 📚 Dependencies
    •  argparse (built-in)
	•  random (built-in)
	•  string (built-in)
	•  requests (for readable usernames)

---

## 📄 License

This project is under the MIT License. Feel free to use and modify as needed.

---

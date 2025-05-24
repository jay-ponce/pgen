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

[ ] Add options for character types (e.g., include/exclude digits, special characters, uppercase).  
[ ] Enable configuration of username style (e.g., readable vs. random).  
[ ] Add persistent storage (e.g., saving credentials to a file securely).  
[ ] GUI or Web Interface (long-term goal).

---

## 🖥 How to Run

### Option 1: Fully Interactive

```
python main.py
```

You’ll be asked whether you want to generate a username, password, and/or PIN. If you say yes to any, you’ll be prompted for the desired length.

### Option 2: Command-Line Arguments

```
python main.py userlen=8 passlen=20
```

Only generates the username and password with the specified lengths. PIN is skipped unless specified.

Accepted Arguments:
	•	userlen=<int> — Length of the username.
	•	passlen=<int> — Length of the password.
	•	pinlen=<int> — Length of the PIN.

---
## 📌 Example Output

```
$ python main.py userlen=7 pinlen=3

--- Generated Output ---
Generated F.Username: v2XpNMi
Generated human-readable username: OB1oq8UY
Generated PIN: 158

$ python main.py

Do you want to generate a username? (y/n): y  
How long do you want your username: 10

Do you want to generate a password? (y/n): y  
How long do you want your password: 16

Do you want to generate a PIN? (y/n): n  

--- Generated Output ---
Generated F.Username: Ab1xK9pLm3
Generated human-readable username: BraveTiger42
Generated Password: &A!x9Ld#sW@q2V!
```

---

## 📚 Dependencies
	• random (built-in)
	• string (built-in)
	• sys (built-in)

---

## 📄 License

This project is under the MIT License. Feel free to use and modify as needed.

---

# Random Credential Generator

This Python program generates random **usernames**, **passwords**, and **PINs** for use in various applications where secure, unique credentials are needed. It serves as a basic tool for experimenting with randomness and user input.

---

## 🔧 Features (Current)

✅ **Random Username Generator**  
  - Generates usernames composed of random characters, optionally mixed with a randomly generated number.  
  - Two types: one using random characters, another using adjective+noun+number approach.

✅ **Random Password Generator**  
  - Generates a password of user-defined length using ASCII characters between 33 (`!`) and 125 (`}`), including special characters.

✅ **Random PIN Generator**  
  - Generates a numeric PIN (4-digit by default, adjustable by input length).

---

## 🛠 Planned Features

[ ] Allow users to choose which items to generate (username, password, PIN, or any combination).  
[ ] Add options for character types (e.g., include/exclude digits, special characters, uppercase).  
[ ] Enable configuration of username style (e.g., readable vs. random).  
[ ] Add persistent storage (e.g., saving credentials to a file securely).  
[ ] GUI or Web Interface (long-term goal).

---

## 🖥 How to Run

1. Make sure Python 3 is installed.

2. Run the script:
   ```bash
   python your_script_name.py
   ```
   
3. Follow the prompts to input desired lengths for the username, password, and PIN.

---
## 📌 Example Output

```
How long do you want your username: 12
How long do you want your password: 16
How long do you want your PIN: 4

Generated F.Username: abcdxyzuvw123
Generated L.Username: J8kF2pX9UzGw
Generated Password: &A!x9Ld#sW@q2V!
Generated PIN: 4582
```

---

## 📚 Dependencies
	• random (built-in)
	• string (built-in)

---

## 📄 License

This project is under the MIT License. Feel free to use and modify as needed.

---

# Password Strength Checker & Brute Force Simulator

A simple Python project that checks the strength of a given password and demonstrates how brute-force attacks work on weak passwords.

## Features

- Checks password strength (Weak, Moderate, Strong)
- Simulates a brute-force attack on 3-letter weak passwords
- Educational purpose to promote strong password practices

## How It Works

1. The user enters a password.
2. The script evaluates its strength based on:
   - Length
   - Uppercase letters
   - Lowercase letters
   - Digits
   - Special characters
3. If the password is weak and short (e.g., 3 characters), a brute-force simulation is triggered to show how easily it can be cracked.

## Demo

```bash
python password_strength_and_brute_force_simulator.py

Example Output

Enter a password to test: abc
[!] Password Strength: Weak

[+] Simulating brute-force attack...
[i] Tried 1000 combinations...
[!] Password cracked: abc
[i] Attempts: 1400
[i] Time taken: 2.3 seconds

Note

This is a simulation and meant for educational purposes only. Do not use for unethical purposes.

Author

Abuzar
GitHub Profile



import string
import time

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 5:
        remarks = "Strong"
    elif strength >= 3:
        remarks = "Moderate"
    else:
        remarks = "Weak"

    return remarks

# Brute force simulator (demo)
def brute_force_simulator(password):
    print("\n[+] Simulating brute-force attack...")
    chars = string.ascii_letters + string.digits
    attempt = ""
    attempts = 0

    start_time = time.time()

    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                attempt = char1 + char2 + char3
                attempts += 1
                if attempt == password:
                    end_time = time.time()
                    print(f"\n[!] Password cracked: {attempt}")
                    print(f"[i] Attempts: {attempts}")
                    print(f"[i] Time taken: {round(end_time - start_time, 2)} seconds")
                    return
                if attempts % 1000 == 0:
                    print(f"[i] Tried {attempts} combinations...")

    print("[x] Password not cracked (only simulates 3-letter brute force)")

# Main program
if __name__ == "__main__":
    print("=== Password Strength Checker & Brute Force Simulator ===\n")
    user_password = input("Enter a password to test: ")
    strength = check_password_strength(user_password)
    print(f"\n[!] Password Strength: {strength}")

    if strength == "Weak":
        brute_force_simulator(user_password)
    else:
        print("\n[!] Brute-force simulation skipped (password not weak enough).")

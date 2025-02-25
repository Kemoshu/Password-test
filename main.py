import tkinter as tk
from tkinter import messagebox
from strength_checker import evaluate_password, generate_strong_password

# Function to check password strength
def check_password_strength():
    password = password_entry.get()  # Get password from input field
    if not password:
        messagebox.showwarning("Input a password.")  # Show warning if input is empty
        return
    
    strength = evaluate_password(password)  # Evaluate password strength
    result_label.config(text=f"Strength: {strength}")  # Display result
    
    if "Weak" in strength:  # Suggest a new password if weak
        suggested_password = generate_strong_password()
        suggestion_label.config(text=f"Try: {suggested_password}")
    else:
        suggestion_label.config(text="")  # Clear previous suggestion

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Create label for input field
tk.Label(root, text="Enter Password:").pack(pady=5)

# Create input field for password
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Create button to check password strength
tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=10)

# Label to display password strength result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Label to display password suggestion
suggestion_label = tk.Label(root, text="", font=("Arial", 10), fg="white")
suggestion_label.pack()

# Start the Tkinter event loop
root.mainloop()
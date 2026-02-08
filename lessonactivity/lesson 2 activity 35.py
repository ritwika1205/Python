root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x250")

tk.Label(root, text="Guess a number (1–50)", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Check", command=check_guess).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
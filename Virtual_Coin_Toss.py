import random
import tkinter as tk
from tkinter import messagebox

def coin_flip():
    return random.choice(["Heads", "Tails"])

def show_coin_flip(result):
    # Create a tkinter window to display the coin toss result
    root = tk.Tk()
    root.title("Coin Flip Result")
    root.geometry("200x100")

    label = tk.Label(root, text=result, font=("Arial", 24))
    label.pack(pady=20)

    # Close the window after 1 second
    root.after(1000, root.destroy)
    root.mainloop()

def simulate_coin_flips():
    historical_results = []  # Store results of all sessions

    while True:
        # Ask the user for the number of flips
        while True:
            try:
                num_flips = int(input("How many times do you want to flip the coin? "))
                if num_flips <= 0:
                    print("Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Initialize counters
        heads_count = 0
        tails_count = 0

        # Perform the flips
        for _ in range(num_flips):
            result = coin_flip()
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1

            # Show graphical representation of the coin toss
            show_coin_flip(result)

        # Calculate percentages
        heads_percentage = (heads_count / num_flips) * 100
        tails_percentage = (tails_count / num_flips) * 100

        # Store session results
        session_result = {
            "Heads": heads_count,
            "Tails": tails_count,
            "Heads Percentage": heads_percentage,
            "Tails Percentage": tails_percentage,
        }
        historical_results.append(session_result)

        # Display current session results
        print("\nResults for this session:")
        print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

        # Display historical results
        print("\nHistorical Results:")
        for i, result in enumerate(historical_results, 1):
            print(f"Session {i}:")
            print(f"  Heads: {result['Heads']} ({result['Heads Percentage']:.2f}%)")
            print(f"  Tails: {result['Tails']} ({result['Tails Percentage']:.2f}%)")

        # Ask if the user wants to repeat the session
        while True:
            repeat = input("\nDo you want to flip again? (yes/no): ").strip().lower()
            if repeat in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if repeat != "yes":
            print("Thank you for using the Coin Flip Simulator. Goodbye!")
            break

if __name__ == "__main__":
    simulate_coin_flips()
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, StringVar, messagebox, Frame
from tkinter.ttk import Button, Style  # Use ttk.Button instead of tkinter.Button


# Function to calculate drug concentration
def drug_concentration(t, dose, elimination_rate):
    """Compute the drug concentration at time t."""
    return dose * np.exp(-elimination_rate * t)

# Function to plot the drug concentration
def plot_concentration():
    try:
        # Get user inputs from the GUI
        dose = float(dose_var.get())
        elimination_rate = float(rate_var.get())
        time_start = float(start_var.get())
        time_end = float(end_var.get())
        num_points = int(points_var.get())

        # Create time points and calculate concentration
        t = np.linspace(time_start, time_end, num_points)
        c = drug_concentration(t, dose, elimination_rate)

        # Compute the total drug effect
        total_effect, _ = quad(drug_concentration, time_start, time_end, args=(dose, elimination_rate))

        # Plot the drug concentration curve
        plt.figure(figsize=(8, 6))
        plt.plot(t, c, label='Drug Concentration C(t)', color='blue', linewidth=2)
        plt.fill_between(t, c, color='purple', alpha=0.5, label=f'Total Effect = {total_effect:.2f}')
        plt.title("Drug Concentration Over Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("Concentration")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Confirmation message
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Function to reset fields
def reset_fields():
    dose_var.set("00")
    rate_var.set("0.0")
    start_var.set("0")
    end_var.set("00")
    points_var.set("00")
    messagebox.showinfo("Reset", "All fields have been reset.")

# Create the main Tkinter window
root = Tk()
root.title("Drug Concentration Calculator")
root.geometry("450x350")
root.configure(bg="#f5f5f5")  # Light gray background

# Add an optional logo or header image
# Uncomment and replace 'logo.png' with a valid image file path if available
# logo = PhotoImage(file="logo.png")
# Label(root, image=logo, bg="#f5f5f5").pack(pady=10)

# Style customization
style = Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
style.configure("TLabel", background="#f5f5f5", font=("Arial", 12))

# Define input fields and labels inside a frame
frame = Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
frame.pack(pady=20)

Label(frame, text="Drug Dose (in mg):").grid(row=0, column=0, padx=10, pady=10, sticky='w')
dose_var = StringVar(value="00")
Entry(frame, textvariable=dose_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Elimination Rate (per hour):").grid(row=1, column=0, padx=10, pady=10, sticky='w')
rate_var = StringVar(value="0.0")
Entry(frame, textvariable=rate_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Start Time (0):").grid(row=2, column=0, padx=10, pady=10, sticky='w')
start_var = StringVar(value="00")
Entry(frame, textvariable=start_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)

Label(frame, text="End Time (until observed):").grid(row=3, column=0, padx=10, pady=10, sticky='w')
end_var = StringVar(value="00")
Entry(frame, textvariable=end_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=10)

Label(frame, text="Time Intervals:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
points_var = StringVar(value="00")
Entry(frame, textvariable=points_var, font=("Arial", 12)).grid(row=4, column=1, padx=10, pady=10)

# Add buttons
Button(frame, text="Generate Plot", command=plot_concentration).grid(row=5, column=0, columnspan=2, pady=10)
Button(frame, text="Reset Fields", command=reset_fields).grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()

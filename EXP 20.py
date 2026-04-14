#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert():
    try:
        value = float(entry_value.get())
        conversion_type = combo.get()
        
        if conversion_type == "Rupees to Dollars":
            result = value / 93  # approx rate
            output.set(f"${result:.2f}")
        
        elif conversion_type == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            output.set(f"{result:.2f}°F")
        
        elif conversion_type == "Inches to Feet":
            result = value / 12
            output.set(f"{result:.2f} ft")
        
        else:
            output.set("Select a conversion type")
    
    except ValueError:
        output.set("Invalid input")

# Main window
root = tk.Tk()
root.title("Multi Converter App")
root.geometry("350x250")
root.resizable(False, False)

# Input Label
tk.Label(root, text="Enter Value:", font=("Arial", 12)).pack(pady=5)

# Input Entry
entry_value = tk.Entry(root, font=("Arial", 12))
entry_value.pack(pady=5)

# Dropdown Menu
tk.Label(root, text="Select Conversion:", font=("Arial", 12)).pack(pady=5)
combo = ttk.Combobox(root, font=("Arial", 11), state="readonly")
combo['values'] = (
    "Rupees to Dollars",
    "Celsius to Fahrenheit",
    "Inches to Feet"
)
combo.pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", command=convert, font=("Arial", 12)).pack(pady=10)

# Output Label
output = tk.StringVar()
output.set("Result will appear here")
tk.Label(root, textvariable=output, font=("Arial", 12), fg="blue").pack(pady=10)

# Run app
root.mainloop()
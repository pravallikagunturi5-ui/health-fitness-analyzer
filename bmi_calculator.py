import tkinter as tk

# BMI Calculation function
def calculate_bmi():
    name = name_entry.get()
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    height_cm = float(height_entry.get())

    height = height_cm / 100
    bmi = weight / (height * height)

    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
        suggestion = "Eat nutritious food and increase calorie intake."
    elif bmi < 24.9:
        category = "Normal"
        suggestion = "Maintain your healthy lifestyle."
    elif bmi < 29.9:
        category = "Overweight"
        suggestion = "Exercise regularly and reduce junk food."
    else:
        category = "Obese"
        suggestion = "Follow a strict diet and regular workout."

    # Ideal Weight Range
    min_weight = round(18.5 * (height * height), 2)
    max_weight = round(24.9 * (height * height), 2)

    # Water Intake
    water = round((weight * 35) / 1000, 2)

    result_label.config(
        text=f"Name: {name}\n"
             f"Age: {age}\n"
             f"BMI: {round(bmi,2)}\n"
             f"Category: {category}\n"
             f"Ideal Weight: {min_weight}kg - {max_weight}kg\n"
             f"Water Intake: {water} Liters/day\n"
             f"Suggestion: {suggestion}"
    )
# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x550")
root.config(bg="lightblue")

# Title
title = tk.Label(
    root,
    text="BMI Calculator with Health Suggestions",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=20)

# Name
tk.Label(root, text="Enter Name", bg="lightblue").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Age
tk.Label(root, text="Enter Age", bg="lightblue").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

# Weight
tk.Label(root, text="Enter Weight (kg)", bg="lightblue").pack()
weight_entry = tk.Entry(root, width=30)
weight_entry.pack(pady=5)

# Height
tk.Label(root, text="Enter Height (cm)", bg="lightblue").pack()
height_entry = tk.Entry(root, width=30)
height_entry.pack(pady=5)

# Button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold")
)
calculate_button.pack(pady=20)
calculate_button.config(command=calculate_bmi)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="lightblue"
)
result_label.pack(pady=20)

root.mainloop()
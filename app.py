from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height_cm = float(request.form["height"])

        height = height_cm / 100
        bmi = round(weight / (height * height), 2)

        # Category
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

        # Ideal weight
        min_weight = round(18.5 * (height * height), 2)
        max_weight = round(24.9 * (height * height), 2)

        # Water intake
        water = round((weight * 35) / 1000, 2)

        # BMR calories
        # BMR Calculation (Mifflin-St Jeor Equation)
        if gender == "Male":
            calories = round((10 * weight) + (6.25 * height_cm) - (5 * age) + 5)
        else:
            calories = round((10 * weight) + (6.25 * height_cm) - (5 * age) - 161)

        result = {
            "name": name,
            "age": age,
            "bmi": bmi,
            "gender": gender,
            "category": category,
            "suggestion": suggestion,
            "ideal_weight": f"{min_weight}kg - {max_weight}kg",
            "water": f"{water} Liters/day",
            "calories": f"{calories} kcal/day"
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
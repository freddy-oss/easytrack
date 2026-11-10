from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

expenses = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>EasyTrack Expense Manager</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            padding: 30px;
        }

        .container {
            background: white;
            padding: 25px;
            max-width: 750px;
            margin: auto;
            border-radius: 12px;
        }

        h1 {
            text-align: center;
            color: #2563eb;
        }

        input, select, button {
            padding: 12px;
            margin: 6px;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }

        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }

        th, td {
            padding: 12px;
            border: 1px solid #ddd;
            text-align: left;
        }

        th {
            background: #2563eb;
            color: white;
        }

        .total {
            font-size: 20px;
            color: green;
            font-weight: bold;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>EasyTrack</h1>
    <h3>Personal Expense Management System</h3>

    <form method="POST" action="/add">

        <input name="item" placeholder="Expense name" required>

        <input name="amount" type="number" step="0.01"
        placeholder="Amount (GHS)" required>

        <select name="category">
            <option>Food</option>
            <option>Transport</option>
            <option>Education</option>
            <option>Shopping</option>
            <option>Other</option>
        </select>

        <button type="submit">Add Expense</button>

    </form>

    <p class="total">Total Expenses: GHS {{ total }}</p>

    <h3>Expense Records</h3>

    <table>
        <tr>
            <th>Item</th>
            <th>Amount (GHS)</th>
            <th>Category</th>
        </tr>

        {% for expense in expenses %}
        <tr>
            <td>{{ expense.item }}</td>
            <td>{{ "%.2f"|format(expense.amount) }}</td>
            <td>{{ expense.category }}</td>
        </tr>
        {% endfor %}

    </table>

</div>
</body>
</html>
"""

@app.route("/")
def home():
    total = sum(expense["amount"] for expense in expenses)

    return render_template_string(
        html,
        expenses=expenses,
        total=f"{total:.2f}"
    )

@app.route("/add", methods=["POST"])
def add_expense():
    item = request.form.get("item")
    amount = float(request.form.get("amount"))
    category = request.form.get("category")

    expenses.append({
        "item": item,
        "amount": amount,
        "category": category
    })

    return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

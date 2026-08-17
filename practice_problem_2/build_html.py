import json
import os

problems = [
    {
        "id": 1,
        "title": "University Cafeteria Billing System",
        "description": "A university cafeteria wants to develop a simple billing program for students. A student can purchase rice meals, drinks, and desserts.\n\nThe price of each item is:\nRice Meal = ৳80\nDrink = ৳30\nDessert = ৳50\n\nThe cashier enters the quantity of each item purchased by the student. The program should calculate the total bill.\nIf the total bill is ৳500 or more, the cafeteria provides a 10% discount. Otherwise, no discount is given.\nThe program should display the original bill, discount amount, and final bill.",
        "ios": [
            {"in": "Rice: 4\nDrink: 4\nDessert: 2", "out": "Original Bill: 540\nDiscount: 54\nFinal Bill: 486"},
            {"in": "Rice: 2\nDrink: 2\nDessert: 1", "out": "Original Bill: 270\nDiscount: 0\nFinal Bill: 270"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int rice, drink, dessert;
    int total;
    float discount = 0, final_bill;

    scanf("%d %d %d", &rice, &drink, &dessert);
    total = (rice * 80) + (drink * 30) + (dessert * 50);

    if (total >= 500) {
        discount = total * 0.10;
    }

    final_bill = total - discount;

    printf("Original Bill: %d\\n", total);
    printf("Discount: %.0f\\n", discount);
    printf("Final Bill: %.0f\\n", final_bill);

    return 0;
}"""
    },
    {
        "id": 2,
        "title": "University Electricity Bill",
        "description": "A university department wants to calculate its monthly electricity bill using a simple billing system.\nThe department enters the number of electricity units consumed during the month.\nThe electricity provider uses the following rates:\nIf consumption is 100 units or less, the rate is ৳5 per unit.\nIf consumption is more than 100 but not more than 200 units, the rate is ৳7 per unit.\nIf consumption is more than 200 units, the rate is ৳10 per unit.\nFor this problem, assume that one rate is applied to all consumed units.\nThe program should determine the appropriate rate and calculate the total bill.",
        "ios": [
            {"in": "Units: 80", "out": "Rate: 5\nTotal Bill: 400"},
            {"in": "Units: 150", "out": "Rate: 7\nTotal Bill: 1050"},
            {"in": "Units: 250", "out": "Rate: 10\nTotal Bill: 2500"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int units, rate, bill;
    scanf("%d", &units);

    if (units <= 100) {
        rate = 5;
    } else if (units <= 200) {
        rate = 7;
    } else {
        rate = 10;
    }

    bill = units * rate;
    printf("Rate: %d\\nTotal Bill: %d\\n", rate, bill);

    return 0;
}"""
    },
    {
        "id": 3,
        "title": "Cinema Ticket Booking",
        "description": "A cinema hall wants to create a simple ticket booking system.\nWhen a customer purchases a ticket, the system asks for the customer's age and the number of tickets they want to purchase.\nThe ticket price depends on the customer's age:\nBelow 12 years → ৳150 per ticket\n12 to 59 years → ৳300 per ticket\n60 years or above → ৳200 per ticket\nThe program should determine the ticket price based on the customer's age and calculate the total amount.",
        "ios": [
            {"in": "Age: 10\nTickets: 2", "out": "Total Cost: 300"},
            {"in": "Age: 25\nTickets: 3", "out": "Total Cost: 900"},
            {"in": "Age: 65\nTickets: 3", "out": "Total Cost: 600"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int age, tickets, price, total;
    scanf("%d %d", &age, &tickets);

    if (age < 12) {
        price = 150;
    } else if (age <= 59) {
        price = 300;
    } else {
        price = 200;
    }

    total = price * tickets;
    printf("Total Cost: %d\\n", total);

    return 0;
}"""
    },
    {
        "id": 4,
        "title": "Mobile Data Package",
        "description": "A mobile operator wants to calculate the monthly internet cost for its customers.\nThe company has three packages:\nBasic: 5 GB → ৳300\nStandard: 10 GB → ৳500\nPremium: 20 GB → ৳800\nThe customer enters a package code: B for Basic, S for Standard, P for Premium.\nThe program should display the selected package and its price.\nIf the customer enters anything other than B, S, or P, the program should display: Invalid Package",
        "ios": [
            {"in": "Package: S", "out": "Standard Package\nPrice: 500"},
            {"in": "Package: X", "out": "Invalid Package"}
        ],
        "solution": """#include <stdio.h>

int main() {
    char code;
    scanf(" %c", &code);

    if (code == 'B') {
        printf("Basic Package\\nPrice: 300\\n");
    } else if (code == 'S') {
        printf("Standard Package\\nPrice: 500\\n");
    } else if (code == 'P') {
        printf("Premium Package\\nPrice: 800\\n");
    } else {
        printf("Invalid Package\\n");
    }

    return 0;
}"""
    },
    {
        "id": 5,
        "title": "Student Result Processing",
        "description": "A university wants to create a simple result-processing program for its students.\nThe program takes the marks obtained by a student in three courses.\nFirst, calculate the student's total and average marks.\nThe university then assigns a result based on the average:\nAverage ≥ 80 → Excellent\nAverage ≥ 70 → Good\nAverage ≥ 60 → Satisfactory\nAverage < 60 → Needs Improvement\nThe program should display the total, average, and result category.",
        "ios": [
            {"in": "Marks: 85 90 80", "out": "Total: 255\nAverage: 85\nResult: Excellent"},
            {"in": "Marks: 50 60 55", "out": "Total: 165\nAverage: 55\nResult: Needs Improvement"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int m1, m2, m3, total;
    int average;
    scanf("%d %d %d", &m1, &m2, &m3);
    
    total = m1 + m2 + m3;
    average = total / 3;
    
    printf("Total: %d\\n", total);
    printf("Average: %d\\n", average);
    
    if (average >= 80) {
        printf("Result: Excellent\\n");
    } else if (average >= 70) {
        printf("Result: Good\\n");
    } else if (average >= 60) {
        printf("Result: Satisfactory\\n");
    } else {
        printf("Result: Needs Improvement\\n");
    }

    return 0;
}"""
    },
    {
        "id": 6,
        "title": "ATM Withdrawal System",
        "description": "A bank wants to implement a simple ATM withdrawal program.\nWhen a customer wants to withdraw money, the ATM asks for: Current account balance, Withdrawal amount.\nThe system checks whether the customer has enough money.\nIf the withdrawal amount is greater than the current balance, the ATM should display: Insufficient Balance\nOtherwise, the ATM should calculate the remaining balance.",
        "ios": [
            {"in": "Balance: 25000\nWithdrawal: 8000", "out": "Remaining Balance: 17000"},
            {"in": "Balance: 5000\nWithdrawal: 6000", "out": "Insufficient Balance"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int balance, withdrawal;
    scanf("%d %d", &balance, &withdrawal);

    if (withdrawal > balance) {
        printf("Insufficient Balance\\n");
    } else {
        printf("Remaining Balance: %d\\n", balance - withdrawal);
    }

    return 0;
}"""
    },
    {
        "id": 7,
        "title": "Ride Sharing Fare Calculator",
        "description": "A ride-sharing company wants to calculate the fare for a passenger based on the distance travelled.\nThe company uses different rates depending on the distance:\nUp to 5 km → ৳20 per km\nMore than 5 km and up to 15 km → ৳15 per km\nMore than 15 km → ৳10 per km\nFor this problem, assume that the selected rate is applied to the entire distance.\nThe passenger enters the total distance travelled.\nThe program should determine the appropriate rate and calculate the total fare.",
        "ios": [
            {"in": "Distance: 4", "out": "Fare: 80"},
            {"in": "Distance: 10", "out": "Fare: 150"},
            {"in": "Distance: 20", "out": "Fare: 200"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int distance, rate, fare;
    scanf("%d", &distance);

    if (distance <= 5) {
        rate = 20;
    } else if (distance <= 15) {
        rate = 15;
    } else {
        rate = 10;
    }

    fare = distance * rate;
    printf("Fare: %d\\n", fare);

    return 0;
}"""
    },
    {
        "id": 8,
        "title": "Employee Salary Calculator",
        "description": "A software company wants to calculate the monthly salary of its employees.\nThe employee provides: Basic salary, House rent allowance, Medical allowance.\nThe company calculates gross salary using: Gross Salary = Basic Salary + House Rent + Medical Allowance\nAfter calculating the gross salary, the company provides a performance bonus:\nGross salary ≥ ৳50,000 → 10% bonus\nGross salary ≥ ৳30,000 → 5% bonus\nGross salary < ৳30,000 → No bonus\nThe program should calculate the employee's gross salary, bonus, and final salary.",
        "ios": [
            {"in": "Basic: 30000\nHouse: 15000\nMedical: 5000", "out": "Gross: 50000\nBonus: 5000\nFinal: 55000"},
            {"in": "Basic: 15000\nHouse: 5000\nMedical: 2000", "out": "Gross: 22000\nBonus: 0\nFinal: 22000"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int basic, house, medical, gross;
    float bonus = 0, final_salary;
    
    scanf("%d %d %d", &basic, &house, &medical);
    gross = basic + house + medical;
    
    if (gross >= 50000) {
        bonus = gross * 0.10;
    } else if (gross >= 30000) {
        bonus = gross * 0.05;
    }
    
    final_salary = gross + bonus;
    
    printf("Gross: %d\\n", gross);
    printf("Bonus: %.0f\\n", bonus);
    printf("Final: %.0f\\n", final_salary);

    return 0;
}"""
    },
    {
        "id": 9,
        "title": "Restaurant Discount System",
        "description": "A restaurant wants to introduce an automatic discount system for customers.\nThe customer enters the total amount of their food bill.\nThe restaurant offers:\nBill below ৳1,000 → No discount\nBill from ৳1,000 to below ৳3,000 → 10% discount\nBill ৳3,000 or above → 20% discount\nThe program should calculate the discount and final amount that the customer has to pay.",
        "ios": [
            {"in": "Bill: 4000", "out": "Discount: 800\nFinal Amount: 3200"},
            {"in": "Bill: 800", "out": "Discount: 0\nFinal Amount: 800"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int bill;
    float discount = 0, final_amount;
    
    scanf("%d", &bill);
    
    if (bill >= 3000) {
        discount = bill * 0.20;
    } else if (bill >= 1000) {
        discount = bill * 0.10;
    }
    
    final_amount = bill - discount;
    
    printf("Discount: %.0f\\n", discount);
    printf("Final Amount: %.0f\\n", final_amount);

    return 0;
}"""
    },
    {
        "id": 10,
        "title": "Parking Management System",
        "description": "A shopping mall wants to create a simple parking fee calculator.\nWhen a vehicle enters the parking area, the system records the number of hours it stayed.\nThe parking charges are:\nUp to 2 hours → ৳50\nMore than 2 hours and up to 5 hours → ৳100\nMore than 5 hours → ৳200\nThe program takes the parking duration as input and determines the appropriate parking fee.",
        "ios": [
            {"in": "Hours: 1", "out": "Fee: 50"},
            {"in": "Hours: 4", "out": "Fee: 100"},
            {"in": "Hours: 6", "out": "Fee: 200"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int hours, fee;
    scanf("%d", &hours);

    if (hours <= 2) {
        fee = 50;
    } else if (hours <= 5) {
        fee = 100;
    } else {
        fee = 200;
    }

    printf("Fee: %d\\n", fee);
    return 0;
}"""
    },
    {
        "id": 11,
        "title": "Vending Machine with Quantity",
        "description": "A university vending machine sells three products:\nA: Chips (৳30)\nB: Soda (৳40)\nC: Chocolate (৳50)\nA student selects a product by entering A, B, or C, and then enters the quantity.\nThe machine calculates total price = Quantity * Price.\nIf invalid, display: Invalid Selection",
        "ios": [
            {"in": "Selection: B\nQuantity: 3", "out": "Product: Soda\nTotal Price: 120"},
            {"in": "Selection: X\nQuantity: 1", "out": "Invalid Selection"}
        ],
        "solution": """#include <stdio.h>

int main() {
    char sel;
    int qty, price = 0;
    scanf(" %c %d", &sel, &qty);

    if (sel == 'A') {
        printf("Product: Chips\\n");
        price = 30;
    } else if (sel == 'B') {
        printf("Product: Soda\\n");
        price = 40;
    } else if (sel == 'C') {
        printf("Product: Chocolate\\n");
        price = 50;
    } else {
        printf("Invalid Selection\\n");
        return 0;
    }

    printf("Total Price: %d\\n", price * qty);
    return 0;
}"""
    },
    {
        "id": 12,
        "title": "Internet Bill with Data Usage",
        "description": "An internet service provider calculates a customer's monthly bill based on data usage.\nRates:\nUp to 10 GB → ৳50 per GB\nMore than 10 GB and up to 30 GB → ৳40 per GB\nMore than 30 GB → ৳30 per GB\nProgram displays: Data usage, Rate per GB, Total bill",
        "ios": [
            {"in": "Usage: 15", "out": "Usage: 15\nRate: 40\nTotal: 600"},
            {"in": "Usage: 35", "out": "Usage: 35\nRate: 30\nTotal: 1050"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int usage, rate, total;
    scanf("%d", &usage);

    if (usage <= 10) {
        rate = 50;
    } else if (usage <= 30) {
        rate = 40;
    } else {
        rate = 30;
    }

    total = usage * rate;
    printf("Usage: %d\\nRate: %d\\nTotal: %d\\n", usage, rate, total);
    return 0;
}"""
    },
    {
        "id": 13,
        "title": "Library Late Fee",
        "description": "A university library charges students a late fee when they return books after the due date.\n0–3 days → ৳5 per day\n4–7 days → ৳10 per day\nMore than 7 days → ৳20 per day\nProgram calculates total fine = late days * rate.",
        "ios": [
            {"in": "Days: 5", "out": "Fine: 50"},
            {"in": "Days: 2", "out": "Fine: 10"},
            {"in": "Days: 10", "out": "Fine: 200"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int days, rate, fine;
    scanf("%d", &days);

    if (days <= 3) {
        rate = 5;
    } else if (days <= 7) {
        rate = 10;
    } else {
        rate = 20;
    }

    fine = days * rate;
    printf("Fine: %d\\n", fine);
    return 0;
}"""
    },
    {
        "id": 14,
        "title": "Water Consumption Bill",
        "description": "A city water authority calculates monthly water bill.\nUp to 50 units → ৳8 per unit\nMore than 50 and up to 100 units → ৳10 per unit\nMore than 100 units → ৳15 per unit\nDisplays water consumption, applicable rate, and total bill.",
        "ios": [
            {"in": "Units: 60", "out": "Consumption: 60\nRate: 10\nTotal: 600"},
            {"in": "Units: 120", "out": "Consumption: 120\nRate: 15\nTotal: 1800"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int units, rate, total;
    scanf("%d", &units);

    if (units <= 50) {
        rate = 8;
    } else if (units <= 100) {
        rate = 10;
    } else {
        rate = 15;
    }

    total = units * rate;
    printf("Consumption: %d\\nRate: %d\\nTotal: %d\\n", units, rate, total);
    return 0;
}"""
    },
    {
        "id": 15,
        "title": "Scholarship Eligibility System",
        "description": "Program asks for marks in three courses and calculates the average.\nAverage ≥ 85 → 50% Scholarship\nAverage ≥ 75 → 25% Scholarship\nAverage ≥ 65 → 10% Scholarship\nAverage < 65 → No Scholarship\nDisplays average and category.",
        "ios": [
            {"in": "Marks: 90 85 80", "out": "Average: 85\nScholarship: 50%"},
            {"in": "Marks: 60 70 65", "out": "Average: 65\nScholarship: 10%"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int m1, m2, m3, average;
    scanf("%d %d %d", &m1, &m2, &m3);
    
    average = (m1 + m2 + m3) / 3;
    printf("Average: %d\\n", average);
    
    if (average >= 85) {
        printf("Scholarship: 50%%\\n");
    } else if (average >= 75) {
        printf("Scholarship: 25%%\\n");
    } else if (average >= 65) {
        printf("Scholarship: 10%%\\n");
    } else {
        printf("Scholarship: No Scholarship\\n");
    }

    return 0;
}"""
    },
    {
        "id": 16,
        "title": "Travel Expense Calculator",
        "description": "A student calculates transportation cost based on distance.\nUp to 50 km → ৳8 per km\n51–100 km → ৳6 per km\nAbove 100 km → ৳5 per km\nDisplays distance, rate, and total cost.",
        "ios": [
            {"in": "Distance: 60", "out": "Distance: 60\nRate: 6\nTotal Cost: 360"},
            {"in": "Distance: 120", "out": "Distance: 120\nRate: 5\nTotal Cost: 600"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int dist, rate, cost;
    scanf("%d", &dist);

    if (dist <= 50) {
        rate = 8;
    } else if (dist <= 100) {
        rate = 6;
    } else {
        rate = 5;
    }

    cost = dist * rate;
    printf("Distance: %d\\nRate: %d\\nTotal Cost: %d\\n", dist, rate, cost);
    return 0;
}"""
    },
    {
        "id": 17,
        "title": "Food Delivery Charge",
        "description": "Order below ৳500 → Delivery charge ৳80\nOrder from ৳500 to below ৳1,000 → Delivery charge ৳40\nOrder ৳1,000 or more → Free delivery\nCalculates Final Amount = Food Amount + Delivery Charge.",
        "ios": [
            {"in": "Food: 700", "out": "Food: 700\nDelivery: 40\nFinal: 740"},
            {"in": "Food: 300", "out": "Food: 300\nDelivery: 80\nFinal: 380"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int food, delivery, final_amount;
    scanf("%d", &food);

    if (food >= 1000) {
        delivery = 0;
    } else if (food >= 500) {
        delivery = 40;
    } else {
        delivery = 80;
    }

    final_amount = food + delivery;
    printf("Food: %d\\nDelivery: %d\\nFinal: %d\\n", food, delivery, final_amount);
    return 0;
}"""
    },
    {
        "id": 18,
        "title": "Mobile Recharge Bonus",
        "description": "Recharge below ৳100 → No bonus\nRecharge from ৳100 to below ৳500 → 5% bonus\nRecharge ৳500 or above → 10% bonus\nCalculates bonus and total balance.",
        "ios": [
            {"in": "Recharge: 200", "out": "Bonus: 10\nTotal Balance: 210"},
            {"in": "Recharge: 600", "out": "Bonus: 60\nTotal Balance: 660"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int recharge;
    float bonus = 0, total;
    scanf("%d", &recharge);

    if (recharge >= 500) {
        bonus = recharge * 0.10;
    } else if (recharge >= 100) {
        bonus = recharge * 0.05;
    }

    total = recharge + bonus;
    printf("Bonus: %.0f\\nTotal Balance: %.0f\\n", bonus, total);
    return 0;
}"""
    },
    {
        "id": 19,
        "title": "Simple Loan Eligibility",
        "description": "Bank basic eligibility check.\nSalary must be at least ৳30,000.\nAge must be at least 21.\nIf both, display Eligible for Loan. Otherwise Not Eligible for Loan. (Use &&)",
        "ios": [
            {"in": "Salary: 35000\nAge: 25", "out": "Eligible for Loan"},
            {"in": "Salary: 25000\nAge: 30", "out": "Not Eligible for Loan"}
        ],
        "solution": """#include <stdio.h>

int main() {
    int salary, age;
    scanf("%d %d", &salary, &age);

    if (salary >= 30000 && age >= 21) {
        printf("Eligible for Loan\\n");
    } else {
        printf("Not Eligible for Loan\\n");
    }

    return 0;
}"""
    },
    {
        "id": 20,
        "title": "University Canteen Billing System",
        "description": "Canteen sells: Burger(120), Pizza(250), Sandwich(100).\nFood Code: B, P, S.\nEnter code and quantity.\nTotal cost = Price * Quantity. If total >= 500, 5% discount.\nOutput food name, quantity, original, discount, final.\nIf invalid, Invalid Food Selection.",
        "ios": [
            {"in": "Code: B\nQty: 5", "out": "Food: Burger\nQuantity: 5\nOriginal Cost: 600\nDiscount: 30\nFinal Cost: 570"},
            {"in": "Code: P\nQty: 1", "out": "Food: Pizza\nQuantity: 1\nOriginal Cost: 250\nDiscount: 0\nFinal Cost: 250"}
        ],
        "solution": """#include <stdio.h>

int main() {
    char code;
    int qty, price, total;
    float discount = 0, final_cost;

    scanf(" %c %d", &code, &qty);

    if (code == 'B') {
        printf("Food: Burger\\n");
        price = 120;
    } else if (code == 'P') {
        printf("Food: Pizza\\n");
        price = 250;
    } else if (code == 'S') {
        printf("Food: Sandwich\\n");
        price = 100;
    } else {
        printf("Invalid Food Selection\\n");
        return 0;
    }

    total = price * qty;
    if (total >= 500) {
        discount = total * 0.05;
    }
    final_cost = total - discount;

    printf("Quantity: %d\\n", qty);
    printf("Original Cost: %d\\n", total);
    printf("Discount: %.0f\\n", discount);
    printf("Final Cost: %.0f\\n", final_cost);

    return 0;
}"""
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practice Problem Set 2 - Midterm</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f8fafc;
            --surface-color: #ffffff;
            --surface-color-light: #f1f5f9;
            --text-main: #0f172a;
            --text-muted: #475569;
            --accent-primary: #6d28d9;
            --accent-secondary: #0891b2;
            --border-color: #cbd5e1;
            --success: #10b981;
            --warning: #f59e0b;
            --header-bg: rgba(255, 255, 255, 0.8);
            --desc-bg: rgba(0,0,0,0.03);
            --code-text: #1e293b;
            --sol-bg: #f1f5f9;
            --sol-text: #334155;
        }

        [data-theme="dark"] {
            --bg-color: #0f111a;
            --surface-color: #1a1d2d;
            --surface-color-light: #252a3f;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-primary: #8b5cf6;
            --accent-secondary: #06b6d4;
            --border-color: #2e344e;
            --success: #10b981;
            --warning: #f59e0b;
            --header-bg: rgba(26, 29, 45, 0.8);
            --desc-bg: rgba(0,0,0,0.2);
            --code-text: #e2e8f0;
            --sol-bg: #0d0f17;
            --sol-text: #a5b4fc;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: var(--bg-color);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 4px;
        }

        header {
            background: var(--header-bg);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 1.5rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        header h1 {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--accent-secondary), var(--accent-primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 2rem;
        }

        .sidebar {
            position: sticky;
            top: 100px;
            height: calc(100vh - 120px);
            overflow-y: auto;
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.5rem;
        }

        .sidebar h3 {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }

        .problem-link {
            display: block;
            padding: 0.75rem 1rem;
            color: var(--text-muted);
            text-decoration: none;
            border-radius: 8px;
            margin-bottom: 0.5rem;
            transition: all 0.2s;
            font-size: 0.95rem;
            font-weight: 500;
        }

        .problem-link:hover {
            background: var(--surface-color-light);
            color: var(--text-main);
            transform: translateX(4px);
        }

        .problem-link.active {
            background: var(--surface-color-light);
            color: var(--accent-primary);
            font-weight: 700;
            border-left: 4px solid var(--accent-primary);
            transform: translateX(4px);
        }

        .problem-card {
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
            scroll-margin-top: 120px;
        }

        .problem-card:hover {
            transform: translateY(-2px);
        }

        .problem-card h2 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--text-main);
        }

        .problem-desc {
            color: var(--text-muted);
            white-space: pre-wrap;
            margin-bottom: 2rem;
            background: var(--desc-bg);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid var(--accent-primary);
        }

        .io-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .io-box {
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1rem;
        }

        .io-box h4 {
            font-size: 0.8rem;
            text-transform: uppercase;
            color: var(--accent-secondary);
            margin-bottom: 0.75rem;
            letter-spacing: 0.5px;
        }

        pre {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            color: var(--code-text);
            white-space: pre-wrap;
        }

        .solution-btn {
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: opacity 0.2s, transform 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .solution-btn:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }

        .solution-btn:disabled {
            background: var(--surface-color-light);
            color: var(--text-muted);
            cursor: not-allowed;
            transform: none;
        }

        .solution-content {
            display: none;
            margin-top: 1.5rem;
            background: var(--sol-bg);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            overflow-x: auto;
        }

        .solution-content.show {
            display: block;
            animation: fadeIn 0.4s ease;
        }

        .solution-content pre {
            color: var(--sol-text);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .countdown-alert {
            background: rgba(245, 158, 11, 0.1);
            border: 1px solid var(--warning);
            color: var(--warning);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            font-weight: 500;
        }

        @media (max-width: 900px) {
            .container {
                grid-template-columns: 1fr;
            }
            .sidebar {
                position: relative;
                top: 0;
                height: auto;
            }
            .io-section {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <header style="display: flex; justify-content: space-between; align-items: center;">
        <h1>Practice Problem Set 2</h1>
        <button id="theme-toggle" style="background: var(--surface-color-light); color: var(--text-main); border: 1px solid var(--border-color); padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">🌓 Toggle Theme</button>
    </header>

    <div class="container">
        <aside class="sidebar">
            <h3>Problems</h3>
            <div id="nav-links">
                <!-- Links injected via JS -->
            </div>
        </aside>

        <main>
            <div class="countdown-alert" id="countdown-alert">
                <span>🕒</span>
                <span id="countdown-text">Solutions will be revealed on August 18, 2026, 10:00 PM BDT.</span>
            </div>

            <div id="problems-container">
                <!-- Problems injected via JS -->
            </div>
        </main>
    </div>

    <script>
        const themeBtn = document.getElementById('theme-toggle');
        themeBtn.addEventListener('click', () => {
            if (document.documentElement.getAttribute('data-theme') === 'dark') {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            }
        });

        if (localStorage.getItem('theme') === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        }

        const releaseDate = new Date('2026-08-18T22:00:00+06:00');
        
        const problems = {problems_json};

        function renderProblems() {
            const navContainer = document.getElementById('nav-links');
            const problemsContainer = document.getElementById('problems-container');

            problems.forEach(p => {
                // Sidebar Link
                const link = document.createElement('a');
                link.href = `#problem-${p.id}`;
                link.className = 'problem-link';
                link.textContent = `${p.id}. ${p.title}`;
                navContainer.appendChild(link);

                // Problem Card
                let iosHtml = '';
                p.ios.forEach((io, index) => {
                    iosHtml += `
                        <div class="io-section">
                            <div class="io-box">
                                <h4>Test Case ${index + 1} - Input</h4>
                                <pre>${io.in}</pre>
                            </div>
                            <div class="io-box">
                                <h4>Test Case ${index + 1} - Expected Output</h4>
                                <pre>${io.out}</pre>
                            </div>
                        </div>
                    `;
                });

                const card = document.createElement('div');
                card.className = 'problem-card';
                card.id = `problem-${p.id}`;
                card.innerHTML = `
                    <h2>${p.id}. ${p.title}</h2>
                    <div class="problem-desc">${p.description}</div>
                    ${iosHtml}
                    <button class="solution-btn" onclick="toggleSolution(${p.id})" id="btn-${p.id}">
                        View Solution Code
                    </button>
                    <div class="solution-content" id="sol-${p.id}">
                        <pre><code>${p.solution.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</code></pre>
                    </div>
                `;
                problemsContainer.appendChild(card);
            });
            
            const observerOptions = {
                root: null,
                rootMargin: '-20% 0px -60% 0px',
                threshold: 0
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.id;
                        document.querySelectorAll('.problem-link').forEach(link => {
                            link.classList.remove('active');
                            if (link.getAttribute('href') === `#${id}`) {
                                link.classList.add('active');
                                link.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                            }
                        });
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.problem-card').forEach(card => {
                observer.observe(card);
            });
            
            checkRelease();
            setInterval(checkRelease, 1000);
        }

        function toggleSolution(id) {
            if (new Date() < releaseDate) {
                alert("Solutions are locked until August 18, 2026, 10:00 PM BDT.");
                return;
            }
            const sol = document.getElementById(`sol-${id}`);
            sol.classList.toggle('show');
        }

        function checkRelease() {
            const now = new Date();
            const alertBox = document.getElementById('countdown-alert');
            const countdownText = document.getElementById('countdown-text');
            
            if (now >= releaseDate) {
                alertBox.style.display = 'none';
                document.querySelectorAll('.solution-btn').forEach(btn => {
                    btn.disabled = false;
                    btn.innerHTML = '✨ View Solution Code';
                });
            } else {
                alertBox.style.display = 'flex';
                
                const timeDiff = releaseDate - now;
                const hours = Math.floor(timeDiff / (1000 * 60 * 60));
                const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
                
                if (countdownText) {
                    countdownText.textContent = `Solutions will be revealed in ${hours}h ${minutes}m ${seconds}s.`;
                }

                document.querySelectorAll('.solution-btn').forEach(btn => {
                    btn.disabled = true;
                    btn.innerHTML = '🔒 Solution Locked';
                });
            }
        }

        renderProblems();
    </script>
</body>
</html>
"""

html_content = html_template.replace('{problems_json}', json.dumps(problems))

with open('/Users/imran/Developer/Running_Project/ICS_Summer_26/practice_problem_2/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully.")

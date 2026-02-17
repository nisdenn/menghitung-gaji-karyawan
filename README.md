# 💼 Employee Salary Calculator (Python)

A Python-based employee salary calculator that computes monthly income based on working hours, overtime pay, and tax deduction.

This project demonstrates the implementation of real-world payroll logic using conditional statements and looping structures in Python.

---

## 🚀 Features

- Employee name input
- Daily working hour input
- Hourly wage input
- Automatic overtime calculation (1.5x rate)
- Monthly salary calculation (30 working days)
- 5% tax deduction system
- Net salary calculation
- Formatted currency output
- Loop system for multiple employee calculations

---

## 🧠 How It Works

The program calculates salary based on the following rules:

### Working Rules:
- Normal working hours: 8 hours per day
- Overtime pay: 1.5 × hourly rate
- Monthly working days: 30 days
- Tax deduction: 5%

---

## 🧮 Salary Formula

### 1️⃣ Daily Salary
- If working hours > 8:
- (8 × hourly_rate) + (overtime_hours × hourly_rate × 1.5)
- If working hours ≤ 8:

---

### 2️⃣ Monthly Salary
daily_salary × 30


---

### 3️⃣ Net Salary
monthly_salary - 5% tax


---

## 🧰 Technologies Used

- Python 3
- Conditional statements
- Loop structure (while loop)
- Basic financial calculation logic

---

## ▶ How to Run

```bash
python MenghitungGajiKaryawan.py
Make sure Python 3 is installed.
```
---

### 📊 Example Output
```
Nama Karyawan    : Andi
Jam Kerja/Hari   : 10 jam
Jam Lembur       : 2 jam
Gaji per Bulan   : Rp 6,000,000
Pajak (5%)       : Rp 300,000
Gaji Bersih      : Rp 5,700,000
```

---

## 🎓 Project Purpose
- This project was developed to practice:
- Financial computation logic
- Real-world salary calculation system
- Conditional branching
- Structured output formatting
- Loop-based user interaction

---

## 💡 Possible Improvements
- Dynamic tax rate configuration
- Variable working days input
- Data storage to file (payroll history)
- Employee ID system
- GUI version using Tkinter
- Export salary slip to PDF

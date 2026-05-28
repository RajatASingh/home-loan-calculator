# Home Loan Prepayment Analyzer

This project is a simple home loan calculator app built with Streamlit.
It helps you understand how extra payments change your loan balance, interest paid, and loan duration.

## What it does

- Lets you enter a loan amount, interest rate, loan tenure, and extra payment amount.
- Calculates the monthly EMI.
- Shows what happens when you pay extra money monthly, quarterly, semi-annually, annually, or on alternate months.
- Compares the normal loan schedule with the extra payment plan.
- Shows graphs and tables to make the result easy to understand.

## Why this project

This is useful when you want a clearer picture of how prepayments affect your home loan.
It is based on a simple loan simulator and shows how much interest you can save.

## How to run

1. Create a Python virtual environment and activate it.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

4. Open the app in your browser using the address shown in the terminal.

## Files

- `main.py` - the Streamlit app interface and calculation flow.
- `src/loan_calculator.py` - functions that simulate loan payments and extra payment schedules.
- `src/get_ip.py` - helper function to get the client IP address when running Streamlit.
- `requirements.txt` - Python packages needed for the project.

## Notes

- The EMI formula is the standard loan EMI calculation.
- The extra payment options are:
  - monthly
  - quarterly
  - semi-annual
  - annual
  - alternate months

## Reference

I used the HDFC Bank EMI calculator as a reference while building this project.

HDFC Bank EMI Calculator: https://homeloans.hdfc.bank.in/home-loan-emi-calculator

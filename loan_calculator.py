import pandas as pd

def loan_simulator(
    loan_amount,
    annual_interest_rate,
    emi,
    extra_payment=0,
    extra_strategy="monthly"  # monthly, quarterly, alternate
):
    monthly_rate = annual_interest_rate / 12 / 100
    balance = loan_amount
    month = 0

    data = []

    while balance > 0:
        month += 1

        opening_balance = balance

        # Interest calculation
        interest = balance * monthly_rate

        # Principal from EMI
        principal = emi - interest

        # Extra payment logic
        extra = 0
        if extra_strategy == "monthly":
            extra = extra_payment
        elif extra_strategy == "quarterly" and month % 3 == 0:
            extra = extra_payment
        elif extra_strategy == "alternate" and month % 2 == 0:
            extra = extra_payment

        # Total deduction
        total_payment = emi + extra

        # Update balance
        balance = balance - principal - extra

        if balance < 0:
            balance = 0

        data.append({
            "Month": month,
            "Opening Balance": round(opening_balance, 2),
            "Interest": round(interest, 2),
            "Principal Paid": round(principal, 2),
            "EMI": emi,
            "Extra Payment": extra,
            "Total Payment": total_payment,
            "Closing Balance": round(balance, 2)
        })

        # Safety break
        if month > 1000:
            break

    df = pd.DataFrame(data)

    return df



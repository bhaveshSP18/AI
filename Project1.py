import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class Transaction:
    def __init__(self,amount,category,t_type):

        self.date=datetime.now().strftime("%d/%m/%Y")
        self.amount=amount
        self.category=category
        self.type=t_type

    def to_dict(self):


         return {"date": self.date,
        "amount": self.amount,
        "category": self.category,
        "type": self.type}

    

class ExpenseManager:
    def __init__(self,filename="expense.csv"):
        self.filename=filename
        try:
            self.data=pd.read_csv(filename)
        except FileNotFoundError:
            self.data=pd.DataFrame(columns=["date","amount","category","type"])

    def add_transaction(self,amount,category,t_type):
        t=Transaction(amount,category,t_type)
        self.data=pd.concat([self.data,pd.DataFrame([t.to_dict()])],ignore_index=True)

    def save_data(self):
        self.data.to_csv(self.filename,index=False)

    def get_summary(self):
        if self.data.empty:
            return "No transaction yet."
        return self.data.groupby(["type","category"])["amount"].sum()

    def stats_numpy(self):

        """Use NumPy for statistics"""
        if self.data.empty:
            return "No data to analyze."
        
        amounts = self.data["amount"].to_numpy()
        
    
    def visualize(self):
        if self.data.empty:
            print("No data to visualize.")
            return
        
        expense_data = self.data[self.data["type"] == "expense"]
        if expense_data.empty:
            print("No expenses to visualize.")
            return
        
        summary = expense_data.groupby("category")["amount"].sum()
        summary.plot(kind="bar", color="skyblue", figsize=(7,4))
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    manager=ExpenseManager()

    while True:
        print("\n---Expense Tracker---")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Summary")
        print("4. Show Stats (NumPy)")
        print("5. Visualize Expenses")
        print("6. Exit")

        choice=input("Enter choice:")


        if choice=="1":
            amt=float(input("Amount:"))
            cat=input("category: ")
            manager.add_transaction(amt,cat,"expense")

        elif choice == "2":
            amt = float(input("Amount: "))
            cat = input("Source: ")
            manager.add_transaction(amt, cat, "income")

        elif choice == "3":
            print("\nSummary:\n", manager.get_summary())

        elif choice == "4":
            print("\nStatistics:\n", manager.stats_numpy())

        elif choice == "5":
            manager.visualize()

        elif choice == "6":
            manager.save_data()
            print("Data saved. Exiting...")
            break


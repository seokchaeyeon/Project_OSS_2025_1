import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def max_expense(self):
    if not self.expenses:
        print("지출 내역이 없습니다.\n")
        return

    max_e = max(self.expenses, key=lambda e: e.amount)
    print(f"\n최대 지출 항목: [{max_e.date}] {max_e.category} - {max_e.description}: {max_e.amount}원\n")


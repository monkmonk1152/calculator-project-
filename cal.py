class RentalProperty:
    def __init__(self, purchase_price, monthly_rent, expenses):
        self.purchase_price = purchase_price
        self.monthly_rent = monthly_rent
        self.expenses = expenses

    def calculate_roi(self):
        total_investment = self.purchase_price + self.expenses
        annual_rent = self.monthly_rent * 12
        roi = (annual_rent / total_investment) * 100
        return roi

# Example usage
property1 = RentalProperty(200000, 1500, 1000)
roi1 = property1.calculate_roi()
print(f"ROI for Property 1: {roi1}%")

property2 = RentalProperty(300000, 2000, 1500)
roi2 = property2.calculate_roi()
print(f"ROI for Property 2: {roi2}%")

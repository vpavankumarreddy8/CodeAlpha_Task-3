# Stock prices (hardcoded dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

# Dictionary to store user's stock quantities
portfolio = {}

print("📊 Enter your stock portfolio (type 'done' to finish):")

# Input loop for stock entries
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\n🧾 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares x ${price} = ${investment}")

print(f"\n💰 Total Investment: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} shares x ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")

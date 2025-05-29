import yfinance as yf

# Stores user’s portfolio as {symbol: shares}
portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol (e.g. AAPL): ").upper()
    try:
        shares = int(input("Number of shares: "))
        if shares <= 0:
            print("❌ Shares must be positive.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return

    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares

    print(f"✅ Added {shares} shares of {symbol}.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol not in portfolio:
        print("⚠ That stock isn't in your portfolio.")
        return

    try:
        shares = int(input("Number of shares to remove: "))
        if shares <= 0:
            print("❌ Shares must be positive.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return

    if shares >= portfolio[symbol]:
        del portfolio[symbol]
        print(f"🗑 Removed all shares of {symbol}.")
    else:
        portfolio[symbol] -= shares
        print(f"➖ Removed {shares} shares of {symbol}.")

def fetch_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        return hist["Close"].iloc[-1] if not hist.empty else None
    except Exception as e:
        return None

def view_portfolio():
    if not portfolio:
        print("📭 Portfolio is empty.")
        return

    print("\n📊 Portfolio Summary")
    print("{:<10} {:<10} {:<10} {:<10}".format("Symbol", "Shares", "Price", "Value"))
    print("-" * 40)

    total = 0
    for symbol, shares in portfolio.items():
        price = fetch_price(symbol)
        if price is None:
            print(f"{symbol:<10} {shares:<10} {'N/A':<10} {'N/A':<10}")
            continue
        value = price * shares
        total += value
        print(f"{symbol:<10} {shares:<10} ${price:<9.2f} ${value:<9.2f}")

    print("-" * 40)
    print(f"{'Total':<10} {'':<10} {'':<10} ${total:.2f}")

def menu():
    while True:
        print("\n📘 MENU")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
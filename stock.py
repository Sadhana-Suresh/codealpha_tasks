import requests

API_KEY = "PWNBV4HLTBJSAMK0"  

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add stocks to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"✅ Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        """Remove stocks from the portfolio."""
        if symbol in self.portfolio and self.portfolio[symbol] >= shares:
            self.portfolio[symbol] -= shares
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"✅ Removed {shares} shares of {symbol} from your portfolio.")
        else:
            print(f"❌ Cannot remove {shares} shares of {symbol}. Not enough shares or stock not found.")

    def get_stock_price(self, symbol):
        """Fetch the current stock price using the Alpha Vantage API."""
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            if "Global Quote" in data and "05. price" in data["Global Quote"]:
                return float(data["Global Quote"]["05. price"])
            else:
                print(f"⚠️ Error fetching stock price for {symbol}. Check API response.")
                return None
        except Exception as e:
            print(f"⚠️ Error fetching stock price: {e}")
            return None

    def display_portfolio(self):
        """Display the portfolio with stock prices and total value."""
        print("\n📊 Your Portfolio:")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                stock_value = price * shares
                total_value += stock_value
                print(f"{symbol}: {shares} shares, Price: ${price:.2f}, Total Value: ${stock_value:.2f}")
            else:
                print(f"{symbol}: {shares} shares, Price: N/A, Total Value: N/A")
        print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")

portfolio = StockPortfolio()

portfolio.add_stock("AAPL", 10)
portfolio.add_stock("TSLA", 5)
portfolio.remove_stock("AAPL", 5)
portfolio.display_portfolio()

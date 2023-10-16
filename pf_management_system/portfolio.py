import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


class Portfolio:
  def __init__(self):
    """Initializ empty portfolio with columns."""
    self.assets_df = pd.DataFrame(columns=["Asset", "Quantity", "Price", "Total Value"])
  
  def add_asset(self, ticker, quantity):
    """Adds an asset to the portfolio using its ticker. Fetches the current price using yfinance"""
    stock = yf.Ticker(ticker)
    price = stock.history(period= "1d")["Close"].iloc[0]
    total_value = price * quantity
    self.assets_df = self.assets_df.append({
      "Asset": ticker,
      "Quantity": quantity,
      "Price": price,
      "Total Value": total_value
      }, ignore_index=True)
    
  
  def update_prices(self):
    """
    Updates the prices of all the assets in the portfolio using yfinance.
    """
    for index, row in self.assets_df.iterrows():
      stock = yf.Ticker(row["Asset"])
      price = stock.history(period="1d")["Close"].iloc[0]
      self.assets_df.at[index, "Price"] = price
      self.assets_df.at[index, "Total Value"] = row["Quantity"] * price

  def top_assets(self, n=5):
    """
    Returns the top n assets with the highest total value.
    """
    return self.assets_df.nlargest(n, "Total Value")
  
  def total_portfolio_value(self):
    """
    Calculates the total value of the portfolio.
    """
    return self.assets_df["Total Value"].sum()
  
  def calculate_return(self, initial_value):
    current_value = self.total_portfolio_value()
    return (current_value - initial_value) / initial_value
  
  def plot_asset_distribution(self):
    """
    Plots a pie chart of the asssets based on their total value
    """
    self.assets_df.set_index("Asset")['Total Value'].plot(kind='pie', autopct='%1.1f%%')
    plt.title("Asset Distribution")
    plt.ylabel("")
    plt.show()


# Example usage:

portfolio = Portfolio()
portfolio.add_asset("AAPL", 10)  # Adding 10 AAPL stocks, price fetched from Yahoo Finance
portfolio.add_asset("GOOGL", 5)  # Adding 5 GOOGL stocks, price fetched from Yahoo Finance
portfolio.add_asset("MSFT", 20)  # Adding 20 MSFT stocks, price fetched from Yahoo Finance
portfolio.add_asset("FB", 30)  # Adding 30 FB stocks, price fetched from Yahoo Finance
portfolio.update_prices()  # Update all asset prices to latest from Yahoo Finance

print(portfolio.top_assets())  # Displaying the top assets by value
print(f"Total Portfolio Value: ${portfolio.total_portfolio_value():.2f}")
portfolio.plot_asset_distribution()
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define your stock portfolio (stock symbol as key, number of shares as value)
portfolio = {}

# Function to fetch stock data (history of the last month)
def fetch_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1mo")  # Last 1 month data
            if data.empty:
                print(f"Warning: No data found for {ticker}. This may be due to the stock being delisted or an incorrect symbol.")
            stock_data[ticker] = data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return stock_data

# Function to calculate the portfolio value
def calculate_portfolio_value(portfolio, stock_data):
    total_value = 0
    for ticker, shares in portfolio.items():
        if ticker in stock_data and not stock_data[ticker].empty:
            try:
                latest_price = stock_data[ticker]['Close'].iloc[-1]  # Safely access the last price
                total_value += latest_price * shares
            except IndexError:
                print(f"Error: No data available for {ticker} to calculate the portfolio value.")
        else:
            print(f"Warning: No valid data for {ticker}, skipping.")
    return total_value

# Function to track the portfolio performance over time
def track_portfolio_performance(portfolio, stock_data):
    portfolio_value = []
    dates = stock_data[list(portfolio.keys())[0]].index if portfolio else []  # Get the dates from the first stock data

    for date in dates:
        total_value = 0
        for ticker, shares in portfolio.items():
            if ticker in stock_data and not stock_data[ticker].empty:
                try:
                    stock_price_on_date = stock_data[ticker].loc[date]['Close']
                    total_value += stock_price_on_date * shares
                except KeyError:
                    print(f"Warning: No price data available for {ticker} on {date}.")
            else:
                print(f"Warning: No valid data for {ticker}, skipping.")
        portfolio_value.append(total_value)

    return dates, portfolio_value

# Function to plot individual stock performance
def plot_individual_stock_performance(stock_data):
    for ticker, data in stock_data.items():
        if not data.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(data.index, data['Close'], label=f"{ticker} Closing Price", color='blue')
            plt.title(f'{ticker} Stock Performance')
            plt.xlabel('Date')
            plt.ylabel('Stock Price (USD)')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

# Function to add stock to portfolio
def add_stock():
    ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()
    shares = int(input(f"Enter the number of shares of {ticker}: "))
    portfolio[ticker] = portfolio.get(ticker, 0) + shares
    print(f"{shares} shares of {ticker} added.")

# Function to remove stock from portfolio
def remove_stock():
    ticker = input("Enter the stock ticker to remove (e.g., AAPL): ").upper()
    if ticker in portfolio:
        shares = int(input(f"Enter the number of shares of {ticker} to remove: "))
        if portfolio[ticker] >= shares:
            portfolio[ticker] -= shares
            if portfolio[ticker] == 0:
                del portfolio[ticker]
            print(f"{shares} shares of {ticker} removed.")
        else:
            print(f"You don't have enough shares of {ticker}.")
    else:
        print(f"{ticker} not found in portfolio.")

# Function to display the portfolio
def display_portfolio():
    if portfolio:
        print("\nCurrent Portfolio:")
        for ticker, shares in portfolio.items():
            print(f"{ticker}: {shares} shares")
    else:
        print("Your portfolio is empty.")

# Main execution
def main():
    while True:
        # Display the menu options
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Track Portfolio Performance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            if not portfolio:
                print("Your portfolio is empty. Please add some stocks first.")
                continue
            # Get stock data for the portfolio
            tickers = list(portfolio.keys())
            stock_data = fetch_stock_data(tickers)

            # Calculate the initial portfolio value
            initial_value = calculate_portfolio_value(portfolio, stock_data)
            print(f"\nInitial Portfolio Value: ${initial_value:.2f}")

            # Track the portfolio performance over time
            dates, portfolio_value = track_portfolio_performance(portfolio, stock_data)

            # Plot the individual stock performance
            plot_individual_stock_performance(stock_data)

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

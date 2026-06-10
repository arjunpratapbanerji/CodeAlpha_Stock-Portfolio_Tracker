# ==============================================================================
# Task 2: Stock Portfolio Tracker
# Goal: Build a simple stock tracker that calculates total investment based on 
#       manually defined stock prices.
# Key Concepts Used: Dictionaries, Input/Output, Basic Arithmetic, File Handling
# ==============================================================================

import os
import csv

# Hardcoded dictionary defining the manual stock prices (USD)
# You can add or modify stock symbols and their corresponding prices here.
STOCK_PRICES = {
    "AAPL": 180.00,  # Apple Inc.
    "TSLA": 250.00,  # Tesla Inc.
    "MSFT": 420.00,  # Microsoft Corp.
    "AMZN": 185.00,  # Amazon.com Inc.
    "GOOGL": 175.00, # Alphabet Inc.
    "NVDA": 120.00,  # NVIDIA Corp.
    "META": 475.00,  # Meta Platforms Inc.
    "NFLX": 640.00   # Netflix Inc.
}

def display_available_stocks():
    """Prints the list of available stocks and their manually defined prices."""
    print("\n" + "=" * 45)
    print("      AVAILABLE STOCKS & PRICES (USD)      ")
    print("=" * 45)
    for symbol, price in STOCK_PRICES.items():
        print(f"  * {symbol:<6} : ${price:>8.2f}")
    print("=" * 45)

def get_positive_number(prompt):
    """
    Helper function to safely get a positive number (int or float) from the user.
    Validates input to prevent program crashes due to invalid formats.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Quantity/Value must be greater than zero. Please try again.")
                continue
            # If it's a whole number, return it as an integer, otherwise float
            return int(value) if value.is_integer() else value
        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")

def add_stock(portfolio):
    """
    Allows the user to add a stock and its quantity to their portfolio.
    If the stock already exists, the quantity is updated.
    """
    display_available_stocks()
    while True:
        symbol = input("\nEnter the Stock Symbol to add (or 'back' to return to menu): ").strip().upper()
        
        if symbol == 'BACK':
            return
            
        if symbol not in STOCK_PRICES:
            print(f"Error: '{symbol}' is not in our active stock list.")
            print("Please choose a valid symbol from the table above.")
            continue
            
        # Get the quantity of shares from the user with validation
        quantity = get_positive_number(f"Enter quantity of shares for {symbol}: ")
        
        # Add to portfolio or update existing shares
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"\nUpdated {symbol} in portfolio. New total shares: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"\nAdded {quantity} shares of {symbol} to your portfolio.")
        break

def calculate_portfolio_value(portfolio):
    """
    Calculates the total value of each stock in the portfolio and the overall portfolio value.
    Returns a dictionary of detailed stock breakdowns and the overall total value.
    """
    details = {}
    grand_total = 0.0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        total_value = quantity * price
        details[symbol] = {
            "quantity": quantity,
            "price": price,
            "total_value": total_value
        }
        grand_total += total_value
        
    return details, grand_total

def display_portfolio(portfolio):
    """Computes and formats the portfolio statistics for console display."""
    if not portfolio:
        print("\n[Your portfolio is currently empty. Add some stocks first!]")
        return
        
    details, grand_total = calculate_portfolio_value(portfolio)
    
    print("\n" + "=" * 60)
    print("                     YOUR STOCK PORTFOLIO                    ")
    print("=" * 60)
    print(f"{'Stock':<10} | {'Shares':<12} | {'Price/Share':<15} | {'Total Value':<15}")
    print("-" * 60)
    for symbol, data in details.items():
        print(f"{symbol:<10} | {data['quantity']:<12g} | ${data['price']:<14.2f} | ${data['total_value']:<14.2f}")
    print("-" * 60)
    print(f"{'GRAND TOTAL INVESTMENT VALUE:':<42} ${grand_total:>14.2f}")
    print("=" * 60)

def save_to_file(portfolio):
    """
    Saves the user's current portfolio to a .txt or .csv file.
    Validates choices and formats data cleanly.
    """
    if not portfolio:
        print("\n[Your portfolio is empty. Nothing to save!]")
        return
        
    details, grand_total = calculate_portfolio_value(portfolio)
    
    print("\nChoose Export Format:")
    print("1. Text File (.txt) - Human-readable report")
    print("2. CSV File (.csv) - Spreadsheet friendly format")
    
    choice = input("Enter choice (1 or 2): ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice. Returning to main menu.")
        return
        
    filename = input("Enter output filename (without extension): ").strip()
    if not filename:
        filename = "portfolio_report"
        
    try:
        if choice == '1':
            filepath = f"{filename}.txt"
            with open(filepath, 'w') as file:
                file.write("=" * 60 + "\n")
                file.write("              STOCK PORTFOLIO REPORT - TXT\n")
                file.write("=" * 60 + "\n")
                file.write(f"{'Stock':<10} | {'Shares':<12} | {'Price/Share':<15} | {'Total Value':<15}\n")
                file.write("-" * 60 + "\n")
                for symbol, data in details.items():
                    file.write(f"{symbol:<10} | {data['quantity']:<12g} | ${data['price']:<14.2f} | ${data['total_value']:<14.2f}\n")
                file.write("-" * 60 + "\n")
                file.write(f"{'GRAND TOTAL INVESTMENT VALUE:':<42} ${grand_total:>14.2f}\n")
                file.write("=" * 60 + "\n")
            print(f"Success! Portfolio saved as '{filepath}' in the current directory.")
            
        elif choice == '2':
            filepath = f"{filename}.csv"
            with open(filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header rows
                writer.writerow(["Stock Symbol", "Shares Owned", "Price Per Share ($)", "Total Value ($)"])
                for symbol, data in details.items():
                    writer.writerow([symbol, data['quantity'], f"{data['price']:.2f}", f"{data['total_value']:.2f}"])
                writer.writerow([])
                writer.writerow(["GRAND TOTAL INVESTMENT VALUE", "", "", f"{grand_total:.2f}"])
            print(f"Success! Portfolio saved as '{filepath}' in the current directory.")
            
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """Main program execution loop."""
    # Dictionary to keep track of user's holdings: { "SYMBOL": quantity }
    portfolio = {}
    
    print("*" * 50)
    print("       Welcome to the Stock Portfolio Tracker!      ")
    print("*" * 50)
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add / Update Stock Shares")
        print("2. View Current Portfolio & Total Value")
        print("3. Export Portfolio to File (.txt/.csv)")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            add_stock(portfolio)
        elif choice == '2':
            display_portfolio(portfolio)
        elif choice == '3':
            save_to_file(portfolio)
        elif choice == '4':
            print("\nThank you for using the Stock Portfolio Tracker! Goodbye.")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

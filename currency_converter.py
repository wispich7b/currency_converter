def convert_currency(amount, rate):
    return amount * rate

def main():
    # Simulated exchange rates (Base: USD)
    exchange_rates = {
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 150.12,
        "CNY": 7.19,
        "BTC": 0.000019
    }

    print("--- Simple Currency Converter (Base: USD) ---")
    print("Available currencies: " + ", ".join(exchange_rates.keys()))

    try:
        usd_amount = float(input("Enter amount in USD: "))
        target_currency = input("Enter target currency code: ").upper()

        if target_currency in exchange_rates:
            rate = exchange_rates[target_currency]
            result = convert_currency(usd_amount, rate)
            print(f"\nResult: {usd_amount} USD = {result:.2f} {target_currency}")
        else:
            print("Error: Currency not supported.")

    except ValueError:
        print("Error: Please enter a numeric value for the amount.")

if __name__ == "__main__":
    main()
    
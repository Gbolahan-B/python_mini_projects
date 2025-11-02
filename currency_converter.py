def get_amount():
    while True:
        amount_input=input("Enter an amount (enter q to quit anytime)").lower()
        if amount_input=="q":
            return None
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Enter a valid positive number.")


def get_currency(prompt):
    currencies = ["USD", "EUR", "NGN", "CAD", "GBP"]
    while True:
        currency = input(f"{prompt} currency ({'/'.join(currencies)}): ").upper()
        if currency not in currencies:
            print("Enter a valid currency.")
        else:
            return currency


def converter(amount, source_currency, target_currency, rates):
    if source_currency == target_currency:
        return amount
    try:
        return amount * rates[source_currency][target_currency]
    except KeyError:
        # Handle missing rate by reversing another
        reverse_rate = 1 / rates[target_currency][source_currency]
        return amount * reverse_rate


def main():
    print("\n--- Multi-Currency Converter ---")
    print("Type 'exit' at any time to quit.\n")

    # Fixed exchange rates (fictional but realistic)
    exchange_rates = {
        "USD": {"NGN": 1500, "EUR": 0.91, "CAD": 1.38, "GBP": 0.78},
        "NGN": {"USD": 0.00067, "EUR": 0.00061, "CAD": 0.00092, "GBP": 0.00052},
        "EUR": {"USD": 1.10, "NGN": 1650, "CAD": 1.51, "GBP": 0.86},
        "CAD": {"USD": 0.72, "NGN": 1100, "EUR": 0.66, "GBP": 0.57},
        "GBP": {"USD": 1.28, "NGN": 1900, "EUR": 1.17, "CAD": 1.76},
    }

    history = []  # store all conversion results

    while True:
        amount_input = input("Enter an amount (or 'exit' to quit): ").strip()
        if amount_input.lower() == "exit":
            break

        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        source_currency = get_currency("Source")

        print("\n--- Conversion Results ---")
        for target_currency in exchange_rates.keys():
            if target_currency == source_currency:
                continue
            converted = converter(amount, source_currency, target_currency, exchange_rates)
            print(f"{amount:.2f} {source_currency} = {converted:.2f} {target_currency}")
            history.append(f"{amount:.2f} {source_currency} → {converted:.2f} {target_currency}")

        print("-" * 35)

    # Show conversion history before exiting
    print("\n--- Conversion History ---")
    if history:
        for record in history:
            print(record)
    else:
        print("No conversions were made.")

    print("\nThank you for using the Multi-Currency Converter!")


if __name__ == "__main__":
    main()
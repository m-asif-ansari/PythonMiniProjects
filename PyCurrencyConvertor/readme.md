# PyCurrencyConvertor

### this is a Python program that creates a currency converter. It allows users to convert between different currencies using exchange rates fetched from an API. Here's a breakdown of how it works:

    Initialization:
        The program starts by creating an instance of the currencyConverter class, which sets up the initial variables and fetches the list of supported currencies.
        It displays a welcome message and presents the main menu with options to convert currencies, view available currencies, or exit.

    Currency Selection:
        If the user chooses to convert currencies (option 1), the program prompts for the base currency and the currency to convert to.
        It validates the entered currency symbols against a list of supported currencies fetched from the API.

    Exchange Rate Retrieval:
        The program uses the requests library to fetch exchange rates from the

    API.
    It stores the retrieved data in convertList to access exchange rates for the chosen currencies.

Conversion and Output:

    The program asks the user if they want to proceed with the conversion.
    If confirmed, the user enters the amount to convert.
    It calculates the converted amount using the exchange rate and displays the result, including the currency symbols retrieved from another API.

Additional Features:

    The program also allows users to view all available currencies (option 2).
    It fetches and displays a list of currencies and their corresponding names using the

        API.

    Exit:
        The program exits if the user chooses option 3.

In summary,
utilizes external APIs to fetch currency data, provides a user-friendly interface to select currencies and amounts, calculates conversions, and displays the results in a formatted way.

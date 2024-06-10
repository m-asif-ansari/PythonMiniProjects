# PyDictionary

### this is a python program that uses the requests library to fetch data from a dictionary API. It allows users to enter a word and retrieve information about it, including phonetics and definitions. Here's a breakdown of how it works:

    Initialization:
        The dictionary class is initialized, setting up the base URL for the API (

    ).

Setting the Word:

    The setWord() method takes a word as input and stores it

Fetching Data:

    The getInfoOfWord() method uses the requests.get() method to make a GET request to the API, concatenating the base URL with the word (
        ) to form the complete API endpoint.
        The response data is converted into a JSON object using self.URLData.json().

    Processing Phonetics:
        The phonetics() method extracts phonetic information from the JSON response. It checks for the presence of a 'license' key in the response data, indicating a successful API call.
        If the word is found, it iterates through the 'phonetics' data and prints the 'text' (written pronunciation) and 'audio' (audio URL for pronunciation).
        If the word is not found, it prints a message suggesting a Google search.

    Processing Definitions:
        The definitionWord() method extracts definition information from the JSON response. It similarly checks for the 'license' key for successful retrieval.
        If the word is found, it iterates through the 'meanings' data and prints the 'partOfSpeech', 'definition', 'synonyms', 'antonyms', and 'example' for each context.
        If the word is not found, it prints a message suggesting a Google search.

    Handling Errors:
        The wrongData() method checks the status code of the API response.
        If the status code is not 200 (indicating a successful request), it prints an error message suggesting a Google search.
        Otherwise, it calls the phonetics() and definitionWord() methods to process the retrieved data.

    Main Function:
        The main() function creates an instance of the dictionary class.
        It prompts the user to enter a word and then calls the necessary methods to retrieve and display information about the word.
        The loop continues until the user enters 'n' or 'N' to stop the program.

In summary, the code interacts with a dictionary API to retrieve and display information about a user-provided word, handling errors and presenting the data in a structured format.

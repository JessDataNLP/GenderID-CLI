# GenderID-CLI
GenderID-CLI is a command-line tool that uses the OpenAI API to identify gender based on personal names. With just an API key and the name of the column containing personal names, GenderID-CLI automatically appends a new column to your dataset containing gender identification (Male/Female)

## Features

- **Ease of Use**: Simple CLI interface for straightforward execution. Users can specify the API key and the column name containing personal names for processing.
- **OpenAI Integration**: Directly utilizes the OpenAI API for LLM-based gender identification.
- **Nationality definition*: The prompt can be customized by adding the nationality when prompted in the command line
  


## Disclaimer


GenderID-CLI is primarily designed for languages with high gender differentiation in personal names, such as Italian, French, and German. Users should be aware that the accuracy of gender identification can vary significantly across languages and cultures. Thus this tools has evident limitations.

- **Not Definitive or Comprehensive**: The results provided by GenderID-CLI are based ondata that may not encompass all cultural or linguistic nuances. Therefore, any identification should not be taken at face value and should be used as an initial guideline rather than a definitive classification.

- **Recognition of Gender Diversity**: Gender is a complex and multifaceted aspect of identity that cannot be fully captured by binary categorizations. GenderID-CLI performs a specific, limited task based on the input data and the current capabilities of Generative AI. This tefiool is not intended to dne or limit the spectrum of gender identity.

- **Cultural Sensitivity and Respect**: Users are encouraged to apply these results with cultural sensitivity and respect for individuals' gender identities. This tool is not designed for making personal or policy decisions that affect individuals' lives or rights.

GenderID-CLI aims to assist in tasks where gender inference from names is relevant, but it is crucial to use this tool responsibly, considering its limitations and the broader context of gender diversity and inclusivity.

## Getting Started

To get started with GenderID-CLI, clone the repository, set up your environment with the required dependencies, and you're ready to add gender identification to your datasets with just a few commands.

## Contribution

Contributions are welcome! Whether it's improving the identification algorithm, enhancing usability, or fixing bugs, feel free to fork the repository and submit your pull requests.

## License

Distributed under the GNU License. See `LICENSE` for more information.




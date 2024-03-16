# azure_clu_cooking_test
# Back-end Testing Case
This repository contains Python code for a testing case related to the back-end functionality of an application. Specifically, it involves retrieving intents from a Machine Learning model using the Azure Conversational Language Understanding (CLU) service.
## Requirements
Before running the code, make sure you have the following:
- Python installed on your system.
- An Azure account for accessing the Azure CLU service.
- Access to a Key Vault in Azure to store and retrieve the API key securely.
## Setup
1. If you don't have an Azure account, create one.
2. Navigate to the Azure portal (https://portal.azure.com).
3. Create a new resource: Conversational Language Understanding.
4. Note down the service endpoint URL and API key for later use.
5. Store the API key as a secret in the Key Vault. Note the name of the secret.
## Code Structure
### azure_cooking_clu.py
This file contains a Python class Azure_cooking_clu that interacts with the Azure CLU service to retrieve intents for given queries.
### test_clu.py
This file contains test cases written using pytest to verify the functionality of the Azure_cooking_clu class. It includes tests for different intents related to recipe cooking.
### retrieve_key.py
This file contains code to retrieve the API key securely from the Key Vault using Azure SDK.
Running the Tests
Clone this repository to your local machine.
Install the required dependencies by running:
'''pip install -r requirements.txt'''
Set up the environment variables:
- AZURE_CONVERSATIONS_ENDPOINT: URL of the Azure CLU service.
- AZURE_CONVERSATIONS_KEY: API key retrieved from the Key Vault.
 -AZURE_CONVERSATIONS_PROJECT_NAME: Name of the Azure CLU project.
- AZURE_CONVERSATIONS_DEPLOYMENT_NAME: Name of the deployment.
Run the tests using pytest:
'''pytest test_clu.py'''
## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
## License
This project is licensed under the MIT License.

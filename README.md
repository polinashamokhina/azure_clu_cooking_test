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
## Intents and Utterances
In the Azure Language Studio, three main intents were defined along with corresponding utterances:
1. get_recipe 's utterances:
- Do you have a recipe for blinis?
- Can you give me a recipe for dumplings?
- Looking for a recipe for Russian salad.
- What ingredients are needed for solyanka soup?
- Show me the recipe for borscht.
2. nutritional_information 's utterances:
- How many carbs are in a serving of blinis?
- What vitamins are in borscht?
- Give me the protein content of Russian salad.
- I'd like to know the nutritional value of dumplings.
- What are the calories in solyanka soup?
- Can you tell me the nutritional information for blinis?
3. substitutions ' utterances:
- I don't have any fresh herbs, what's a good substitution?
- Can I use coconut milk instead of regular milk?
- What can I use instead of sugar?
- Is there a gluten-free option for flour?
- Can I replace butter with margarine?
- Are there any dairy-free alternatives for cream in this dish?
- What can I use instead of eggs in this recipe?
## Entities
Entities are named parameters extracted from utterances that provide important information for understanding the user's intent. Two main entities were defined:
- dish_name: Used in the get_recipe and nutritional_information intents to specify the name of the dish.
- modification: Used in the substitutions intent to specify the modification or substitution needed.
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

import pytest
import os
from azure_cooking_clu import Azure_cooking_clu

class TestCLU:

    @pytest.fixture
    def azure_clu_instance(self):
        os.environ["AZURE_CONVERSATIONS_ENDPOINT"] = "https://polina-shsamokhina.cognitiveservices.azure.com/"
        os.environ["AZURE_CONVERSATIONS_KEY"] = "fake_secret_value"
        os.environ["AZURE_CONVERSATIONS_PROJECT_NAME"] = "dataleon-polina-test"
        os.environ["AZURE_CONVERSATIONS_DEPLOYMENT_NAME"] = "cooking_recipes_deployment"
        return Azure_cooking_clu()

    # trying out different intents' values 
    @pytest.mark.parametrize("utterance, expected_intent", [
        ("Show me the recipe for borscht", "get_recipe"),
        ("How many carbs are in a serving of blinis", "nutritional_information"),
        ("Can I use coconut milk instead of regular milk", "substitutions")
    ]) 
    def test_retrieve_intent(self, azure_clu_instance, utterance, expected_intent):
        # call retrieve_intent method 
        _, intent_value, _ = azure_clu_instance.retrieve_intent(utterance)

        assert intent_value == expected_intent




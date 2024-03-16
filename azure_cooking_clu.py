import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
from retrieve_key import secret_value

class Azure_cooking_clu:
    def __init__(self):
        # s et up environment variables
        os.environ["AZURE_CONVERSATIONS_ENDPOINT"] = "https://polina-shsamokhina.cognitiveservices.azure.com/"
        os.environ["AZURE_CONVERSATIONS_KEY"] = secret_value
        os.environ["AZURE_CONVERSATIONS_PROJECT_NAME"] = "dataleon-polina-test"
        os.environ["AZURE_CONVERSATIONS_DEPLOYMENT_NAME"] = "cooking_recipes_deployment"

    def retrieve_intent(self, query):
        # get secrets
        clu_endpoint = os.environ["AZURE_CONVERSATIONS_ENDPOINT"]
        clu_key = os.environ["AZURE_CONVERSATIONS_KEY"]
        project_name = os.environ["AZURE_CONVERSATIONS_PROJECT_NAME"]
        deployment_name = os.environ["AZURE_CONVERSATIONS_DEPLOYMENT_NAME"]

        # analysis
        client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
        with client:
            result = client.analyze_conversation(
                task={
                    "kind": "Conversation",
                    "analysisInput": {
                        "conversationItem": {
                            "participantId": "1",
                            "id": "1",
                            "modality": "text",
                            "language": "en",
                            "text": query
                        },
                        "isLoggingEnabled": False
                    },
                    "parameters": {
                        "projectName": project_name,
                        "deploymentName": deployment_name,
                        "verbose": True
                    }
                }
            )
        # save results 
        utterance_result = result['result']['query']
        intent_value = result['result']['prediction']['topIntent']
        confidence_score = result['result']['prediction']['intents'][0]['confidenceScore']

        return utterance_result, intent_value, confidence_score
        
if __name__ == '__main__':
    analysis = Azure_cooking_clu()
    query = "Show me the recipe for borscht"
    utterance_result, intent_value, confidence_score = analysis.retrieve_intent(query)

    print(f"query: {utterance_result}")
    print(f"intent value: {intent_value}")
    print(f"confidence score: {confidence_score}")
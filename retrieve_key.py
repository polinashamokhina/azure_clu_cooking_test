from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# values of the Key Vault URL and secret name
key_vault_url = "https://first-keyvault-test.vault.azure.net/"
secret_name = "FirstKey"

credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# retrieve the secret value
secret_value = secret_client.get_secret(secret_name).value


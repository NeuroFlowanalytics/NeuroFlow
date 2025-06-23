from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

credential = DefaultAzureCredential()
client = CostManagementClient(credential)

print("✅ Azure connection successful!")
# Votre logique d'optimisation ici
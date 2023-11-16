from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python network_interface_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="398d5b6a-e001-458d-9c69-e909098d0b68",
    )

    response = client.network_interfaces.begin_create_or_update(
        resource_group_name="NOSA.VM_group",
        network_interface_name="nic4",
        parameters={
            "location": "uksouth",
            "properties": {
                "ipConfigurations": [
                    {
                        "name": "ipconfig1",
                        "properties": {
                            "publicIPAddress": {
                                "id": "/subscriptions/398d5b6a-e001-458d-9c69-e909098d0b68/resourceGroups/NOSA.VM_group/providers/Microsoft.Network/publicIPAddresses/ip5"
                            },
                            "subnet": {
                                "id": "/subscriptions/398d5b6a-e001-458d-9c69-e909098d0b68/resourceGroups/NOSA.VM_group/providers/Microsoft.Network/virtualNetworks/NOSA.VM-vnet/subnets/default"
                            },
                        },
                    }
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/NetworkInterfaceCreate.json
if __name__ == "__main__":
    main()
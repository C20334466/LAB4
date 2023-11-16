from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_create_custom_image_vm_from_an_unmanaged_generalized_os_image.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="398d5b6a-e001-458d-9c69-e909098d0b68",
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name="NOSA.VM_group",
        vm_name="{vm-name}",
        parameters={
            "location": "uksouth",
            "properties": {
                "hardwareProfile": {"vmSize": "Standard_D1_v2"},
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/398d5b6a-e001-458d-9c69-e909098d0b68/resourceGroups/NOSA.VM_group/providers/Microsoft.Network/networkInterfaces/nic4",
                            "properties": {"primary": True},
                        }
                    ]
                },
                "osProfile": {
                    "adminUsername": "C20334466",
                    "computerName": "vm4",
                },
                "storageProfile": {
                    "osDisk": {
                        "caching": "ReadWrite",
                        "createOption": "FromImage",
                        "image": {
                            "uri": "http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/{existing-generalized-os-image-blob-name}.vhd"
                        },
                        "name": "myVMosdisk",
                        "osType": "Windows",
                        "vhd": {
                            "uri": "http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk.vhd"
                        },
                    }
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachine_Create_CustomImageVmFromAnUnmanagedGeneralizedOsImage.json
if __name__ == "__main__":
    main()
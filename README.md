# azure_flask_deployment
This is an azure flask deployment. My Azure Webapp link is below.


Welcome to My Healthcare Webpage: 
[my-hha504-webapp.azurewebsites.net](my-hha504-webapp.azurewebsites.net)


## Step-by-step Guide on Setup and Deployment of Application Locally 
1. 

## Step-by-step Guide on Setup and Deployment of Application via Azure 
1. Azure Account:
Sign in to your Azure portal (https://portal.azure.com/) or create a new Azure account if you don't have one.
2. Create an App Service:
In the Azure portal, create a new Azure App Service and resource group.
3. Code Your Application: (Used shell.google.cloud)
4. Enter the following commands in the Linux terminal to initiate deployment:
   ``` python
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   az
   az login --use-device-code
   az account list --output table
   az account set --subscription yoursubscriptionId
   az group list
   To launch:
      az webapp up --resource-group (name of resource group) --name (your app service name) --runtime PYTHON:3.9 --sku B1
   To delete:
      az webapp delete --name MyWebapp --resource-group MyResourceGroup
   ```


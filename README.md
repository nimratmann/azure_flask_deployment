# azure_flask_deployment
This is an azure flask deployment. My Azure Webapp link is below.


Welcome to My Healthcare Webpage: 
[my-hha504-webapp.azurewebsites.net](my-hha504-webapp.azurewebsites.net)


## Step-by-step Guide on Setup and Deployment of Web Application using Azure and HTML.
Step 1:
Using Github, create a new repository including a Readme file and name it ```azure_flask_deployment```. Then go to "shell.google.cloud" to open the Google Shell Environment and import your GitHub repository using the git clone command followed by link of repo.

Step 2:
Create an ```app.py``` file and copy and paste python code from  hantswilliams/hha504/wk2/flaskapp_0/app.py folder. In this folder, import Flask and Pandas.

Step 3:
Create a ```requirements.txt``` file and insert ```python-dotenv, pandas, flask, gunicorn```.

Step 4:
Create a new folder labeled "Templates" and add ```base.html, about.html and data.html``` files. These files will consist of code copied and pasted from hantswilliams/hha504/wk2/flaskapp_0/Templates folder.

Step 5:
Ensure to push these changes back to Github to update repository using the following commands in the terminal 
```
git add .
git commit-m 'Message'
git push
```



















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


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
Create a new folder labeled "Dataset" and then right click and select "upload files" to upload the dataset you will be displaying on your webpage.

Step 5:
Ensure to push these changes back to Github to update repository using the following commands in the terminal.
```
git add .
git commit-m 'Message'
git push
```
Step 6:
To run the flask application locally on the terminal type the command ```python app.py```. This will display a url that you can click and will prompt you to a new tab with your working webpage.

Step 7:
To run the flask application via Azure App Service. Use the following command ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash``` to initiate Azure Cli package installation.

Step 8:
Then, in your terminal, use the following commands ```az ``` and ```az login--use-device-code.```, type in "az." You are then going to click the URL from the terminal and enter the code to authenticate. Use your Stony Brook account and press continue. You can then exit out of that tab and go back to the Google Shell environment. You will see that you were successfully authenticated.  

Step 9:
 Then insert the command ```az account list --output table``` into your terminal. You are going to be given a list of different subscription IDs. To change this ID to the "Azure for Students" one, use the command ```az account set --subscription subscriptionId```.

Step 10:
Now, log into the Azure Web Portal and create a new resource group under the "Resource Groups" tab. Ensure your resource group is under the "Azure for Students" subscription and has a simple name with no white space and no special characters. 

Step 11:
Then redirect to the Google Shell Environment and in the terminal use the command ```az group list```. 

Step 12:
To launch the azure web application, insert the command'''az webapp up --name-insert resource group here-flask --runtime PYTHON:3.9 --sku B1." You have to insert a preferred "name" and "resource group" name you created in your Azure account.

Step 13:
The terminal will then say that the webapp does not exist, and it will create the resource group and start the zip deployment process. (This process takes a few minutes)

Step 14: 
You can now login into your Azure account and view your running wbepage URL under "App Services"















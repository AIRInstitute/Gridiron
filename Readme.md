# GRIDIRON
Biosensors are interesting devices arising from a synergistic combination of well-established scientific knowledge and cutting-edge technologies including nanotechnology, rational design, materials science, and microfluidics. These devices have proved to be useful in various sectors (e.g., medical, agrifood, environmental) and have demonstrated good practicality, sensitivity, reproducibility, and fast response. However, a critical analysis of the worldwide biosensor market suggests that there is a bottleneck in the technology readiness level in prototype development, corresponding to a severe gap between academic research and industrial investments.

The global biosensors market size was valued at USD 22.4 billion in 2020 and is expected to expand at a compound annual growth rate (CAGR) of 7.9% from 2021 to 2028. Biosensors, owing to their ability to assess health status, and disease onset and progression, are being used extensively in-home healthcare by patients, and hence, are expected to boost market growth over the forecast period. Furthermore, technological advancements, as well as various non-medical-based applications are expected to enhance the applicability of the market for biosensors, thus promoting its growth.

Therefore, there is a need to automate and optimize production processes in the manufacture of biosensors and auxiliary electronic materials to reduce costs and false negatives in diagnostic tests. In this regard, there is a growing trend in investment in solutions that detect production failures in increasingly robotic biosensor manufacturing environments. GRIDIRON project deals with these issues and aims to detect and prevent potential errors in circuitry, electrodes and vials used in testing.

## Install

The different components are going to be deployed in docker containers, so it is necessary to have docker installed in the machine or machines where it is going to be deployed. Of the different components that are going to be deployed, there are two that are mandatory to be deployed on the pc that is connected to the microscope and the pipette robot. 

These components are "microscopeAPI" and "pipetteAPI". The rest of the components can be deployed on another remote machine if desired. We will also make use of a postman collection for the configuration of the different components, so it will be necessary to have postman installed.

First, we are going to create the images and the containers of all the components and then we will make the different configurations that are necessary. We will start by creating the images and the API containers that will be launched on the computer that is connected to the miscroscope and the pipette robot.

We start with the microscope(This component is the only one that cannot be launched with docker, because the library that allows us to connect to the microscope, is programmed to run only on windows, so it cannot be launched with docker)(To install and deploy this component we will need to install python 3.7.8 previously):

???	Open the .env file in the "microscopeAPI/src" folder and modify the IP addresses by the corresponding ones for our case.

???	Open a powershell terminal.

???	In the terminal open the folder "microscopeAPI".

???	Once inside we are going to enter the following command to create a python virtual environment 
```
python ???m venv venv
```
???	When the command is finished executing, enter the following command to use the virtual enviroment: 
```
./venv/Scripts/Activate.ps1
```
???	Once finished executing the command, we are going to install the necessary libraries inside the environment with the command 
```
pip install -r requirements.txt
```
 (before doing this command we must be in the directory where the requirements.txt file is located).
???	Now we go into the "src" folder and enter the following command 
```
python __init__.py
```
Now we will create the image and the container of the pipette api, for this we will follow the next steps:

???	Open the .env file in the "pipetteAPI/src" folder and modify the IP addresses by the corresponding ones for our case.

???	Open a powershell terminal.

???	In the terminal we navigate to the folder "pipetteAPI".

???	Once inside we introduce the following command: 
```
docker build -t pipetteapi ./
```
???	When the command finishes executing enter the following command: 
```
docker-compose -f docker-compose.yml up -d
```
???	When finished we enter the command 
```
docker ps
```
and check that the container is running correctly.

Now we will launch the rest of the components that can be launched either on the same machine as the previous components or on a remote machine:

???	First go to the "backend/Backend_Django" folder and modify the .env file with the corresponding IP addresses.

???	Enter the command 
```
docker build -t backend-django ./
``` 
???	Followed by the command 
```
docker-compose -f docker-compose.yml up -d
```
???	Now let's go inside the "docker" folder located in the same directory and enter the following command: 
```
docker-compose -f docker-compose.yml up -d
```
???	Once this is done, let's go back to the "backend" directory and now enter the "keyrock" subdirectory.

???	Inside we enter the command 
```
docker-compose -f docker-compose up -d
```
???	Now we launch the component "backendAI" for which we go to the folder "backendAI/backendAI/src" and modify the necessary IP addresses.

???	Then you have to download the model from the next link and save it on the direcotry "backendAI/modelo":
```
https://drive.google.com/file/d/1nkJ7dnj4R1LIJ6idzrxp-yra35NgX8Y1/view?usp=sharing
```
???	Now we go back to the base folder "backendAI" and enter the following commands 
```
docker build -t backendai ./
```
 and 
```
docker-compose -f docker-compose.yml up -d
```
???	Then we have to go to postman, import the postman collection and the postman environment situated in the folder ???config???, change the IPs and ports of the environment for those of the machine where the components will be deploy and then execute all the http calls of the postman collection in order to configure the platform.

Now we only have to launch the component that is the frontend of the project. But first we must configure keyrock to be able to launch the frontend.

To do this, we follow the steps below:

???	Access the keyrock interface at the address "http://{{IP}:3005" and log in with the e-mail address admin@test.com and the password "1234".

![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen1.png)

A screen like the following one will appear:
 
![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen2.png)

???	Click in the button ???Register??? and enter the corresponding information about the application frontend:
 
![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen3.png)

???	Once you have done this, the application will have been created and will show you the application management screen, where you can perform tasks such as managing the pep proxy, register users in the application or, what interests us, obtain the Oauth2.0 credentials to use them to launch our last component, the frontend.
 
![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen4.png)

Now we are going to launch the last component, which is the frontend:

???	-we need to copy the credentials "Client ID" and "Client Secret", obtained in the previous step, in the .env file in the directory "Gridiron-web-main/vue-template-main/src", and in the same file, we also have to change the IP where keyrock component is located.

???	Now inside the directory "vue-template-main" we introduce the command 
```
docker build -t frontend ./
```
???	After this we will introduce the command 
```
docker-compose -f docker-compose up -d
```
and we will have launched all the components of the platform.


## Usage

The use of the platform is really simple:

First we find a screen where we can login:

![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen5.png)

Once we login we are redirected to a main menu where we can select if we want to use the microscope or the pipette, first we are going to use the microscope, whose tab is as shown below.

![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen6.png)

In this tab we can obtain images from the microscope and process them by machine learning algorithms for cell counting.

![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen7.png)

Primero realizaremos una imagen de una muestra sin aplicar la trypan blue solution y despues otra aplicando la solucion

Now we will go to the pipette tab, where we will be able to select which protocol we want to execute, fill in the necessary values for the execution of that protocol and execute it.

![Image text](https://github.com/AIRInstitute/Gridiron-DIH2/blob/master/imagenes/Imagen8.png)
<!-- ## Contributing

PRs accepted. -->

<!-- ## License

MIT ?? Richard McRichface -->

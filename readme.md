# Installation requirements

To install the required packages run the following command (to use this you will need pip or pip3 on mac) : 
```
pip install -r requirements.txt
```
(the virtualenv must be activated before running this command)


## Using the virtual environment

Creating a virtualenv
```
virtualenv -p python3 envname
```

Activating the environment
```
source ./envname/bin/activate
```

Deactivating the environment
```
deactivate
````

## Runing the API
To run the project : 

Run the main.py file, this will start the server in development mode.
```
python3 main.py
```

To request the API use a REST Client (ex: Insomnia) or use the interface directly built on top of the API that runs on http://0.0.0.0/index



## Contributor
Océane CHARLERY - Sereyvuth CHUM - Emilie DAONGAM
# API Hosting & Queries

This API is hosted on pythonanywhere [here](http://oceanecharlery.pythonanywhere.com/index) 


## Queries Examples

Here are some queries examples to request this API with a REST Client.

* Query by Messier ID (ex: M76): `http://oceanecharlery.pythonanywhere.com/galaxies/messier/M76`

* Query by NGC ID (ex: NGC 650) :  ` http://oceanecharlery.pythonanywhere.com/galaxies/ngc/NGC%20650 `

* Query by Object Type (ex: Globular Cluster) : ` http://oceanecharlery.pythonanywhere.com/galaxies/object_type/Globular%20Cluster%20/%20Amas%20Globulaire `

* Query by Season (ex: Spring) : ` http://oceanecharlery.pythonanywhere.com/galaxies/season/Spring%20/%20Printemps `

* Query by Constellation EN (ex: Hair of Berenice) : ` http://oceanecharlery.pythonanywhere.com/galaxies/constellation_en/Hair%20of%20Berenice `

* Query by Constellation FR (ex: Chevelure de Bérénice) : ` http://oceanecharlery.pythonanywhere.com/galaxies/constellation_fr/Chevelure%20de%20B%C3%A9r%C3%A9nice `

* Query by Constellation Latin (ex: Coma Berenices) : ` http://oceanecharlery.pythonanywhere.com/galaxies/constellation_fr/Coma%20Berenices `

* Query by Right Ascension (ex: 12:31:59.16) : ` http://oceanecharlery.pythonanywhere.com/galaxies/right_ascension/12:31:59.16 `

* Query by year of discovery (for objects discovered between 1600 and 1720) : ` http://oceanecharlery.pythonanywhere.com/galaxies/year/1600/1720 `

* Query by Size (ex: 24,0') : ` http://oceanecharlery.pythonanywhere.com/galaxies/size/24,0' `
 

# Installation Guide

To install the required packages run the following command (to use this you will need a recent version of pip or pip3 on mac) : 
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
```

## Runing the API
To run the project : 

Run the main.py file, this will start the server in development mode.
```
python3 main.py
```

To request the API use a REST Client (ex: Insomnia) or use the interface directly built on top of the API that runs on http://0.0.0.0/index


## Contributors
Océane CHARLERY - Sereyvuth CHUM - Emilie DAONGAM
# trkr-cli
`trkr` is a simple tool that keeps the track of tasks from your command line.  
## DISCLAIMER  
`trkr` is in development at the moment and is not yet stable, so if you install it and try to use, please don't get upset about the bugs. The stable version will be announced.  :v:
## Structure 
The project is structured based on [skele-cli](https://github.com/rdegges/skele-cli) by Randall Degges.   
## Installation  
After cloning the repository or downloading the files, run   
`$ pip install -e .`  
trkr is platfrom independent, but requires at least `python 3.5` to be sure to run properly and `pip` package manager in order to install.
## Data  
The application maintains its local SQLite database in a custom directory `~/trkr/`, where `~` is the default user/home directory specific to the platform.

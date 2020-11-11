# Fantasy Football Data Analysis

## Discussion:
As someone who knows nothing about football, I thought it would be interesting to see if I could get reasonable Fantasy Football picks for the 2020 season using a simple linear regression model. The model looks for players who have consistently improved their score in past seasons and have performed well overall.
## Requirements:
* Python3

## Dependencies:
 This project relies on the following dependencies, which are included in the requirements.txt for setting up the project.
#### Python:
* joblib==0.16.0
* numpy==1.19.1
* pandas==1.1.1
* pkg-resources==0.0.0
* python-dateutil==2.8.1
* pytz==2020.1
* scikit-learn==0.23.2
* scipy==1.5.2
* six==1.15.0
* threadpoolctl==2.1.0


## Virtual Environment:
You may wish to run the project in a virtual environment to avoid conflicts with other projects' dependencies or organization purposes. If there are no concerns with this, this section can be skipped. Otherwise, execute the following commands in the top level directory:

    1. python3 -m venv environment
    2. source environment/bin/activate

To exit the virtual environment when finished hosting the website, execute the following command:

    1. deactivate

## To Install :
This command will only have to be executed when running the program for the first time and will install all the dependent python libraries in <strong>requirements.txt</strong>.
##### Linux/Mac/Windows:
python -m pip install -r requirements.txt --ignore-installed

## To Run:
The project will run and output the top <strong>k</strong> best fantasy football players for the upcoming season, based on the data provided. This can be adjusted in the <strong>analyze.py</strong> file in the top level directory. Execute the following command:

    1. python3 analyze.py

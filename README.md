# Example Python Solution

## Setup

### Pre-requisites
- Install Git: https://github.com/git-guides/install-git
- Install Python 3.8: https://www.python.org/downloads/release/python-380/
  - (the testing solution is not proven yet to work with Python 3.9)
- Install pipenv: https://pypi.org/project/pipenv
- Install the solution:
  - Open a command line in a folder where you want to store the testing solution and clone the python_framework_test solution
    (You can find the command in github)

### For this example, the following environment variables need to be set: APP_URL, USER_NAME and USER_PASSWORD 
(The testing user should be already created. Once you create a testing user, use this user name and password to set the variables.)

For environment variables, duplicate .env-sample and rename it to .env. Then edit the .env file with your own values.

OR

Set the environment variables in the command line:
- APP_URL
  - Windows: ```set APP_URL=https://demoqa.com/```
  - Linux: ```export APP_URL=https://demoqa.com/```
- USER_NAME
  - Windows: ```set USER_NAME=<testing_user_name>```
  - Linux: ```export USER_NAME='<testing_user_name>'```
- USER_PASSWORD
  - Windows: ```set USER_PASSWORD=<testing_user_password>```
  - Linux: ```export USER_PASSWORD=<testing_user_password>```
 
OR

If you are using Pycharm, create a configuration and set there the environment variables. At the end of this file you can find the explanation about how to create a configuration in Pycharm. The environment variables are added in the Environment variables field like this:

PYTHONUNBUFFERED=1;APP_URL=https://demoqa.com/;USER_NAME=<testing_user_name>;USER_PASSWORD=<testing_user_password>

### Install testing solution dependencies
From root project folder execute the following command: ```pipenv install```

### To execute tests locally:

Execute the following command, by replacing \<TAG\> by any scenario tags you would like to execute:
```
pipenv run behavex -t <TAG> -D browser=chrome
```

OR

If you are using Pycharm, create a new Python configuration to execute the tests locally. You should configure the following:

- Name
- In the Run section you need to:
  
    - Select the pipenv env you are using as the python to be used
    - In the dropdown select 'module'
    - In the field next to the dropdown write behavex.runner as the runner
    - In the last field write the parameters: -t <TAG> -D browser=chrome
- In the working directory, select the automation project directory
- Add the environment variables as it was explained before

### Running in headless mode
If you need to run locally in headless mode, you need to add the following parameter: -D headless_browser=true

Executing by the terminal:

```
pipenv run behavex -t <TAG> -D browser=chrome -D headless_browser=true
```

Adding it in the Pycharm configuration as a parameter:

-t <TAG> -D browser=chrome -D headless_browser=true
  

### Testing solution documentation
As the testing solution consists of a wrapper (called BehaveX) on top of Python Behave, please take a look at the Behave documentation:
https://behave.readthedocs.io/en/stable/

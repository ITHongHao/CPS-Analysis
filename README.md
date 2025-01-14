# Installation
Before installation, I would recommend setting up and launching a python virtual environemnt to ensure no package version conflicts occur. This can be as easy as follows:
```
python -m venv py_env    # (If you use a different name for your venv please add this folder to the gitignore)

on windows:
.\py_env\Scripts\activate

on mac:
source py_env/bin/activate
```

Once activated you should see the environment name on the left side of your command prompt. To exit, simply run:
```
deactivate
```

To install all required packages to run the flask application, run the following command from the base directory of this repository (if using a virtual environment make sure your environment is ON):
```
pip install -r requirements.txt
```


# Dependencies
This project uses a .env file to handle access tokens and environment variables. The following variables are needed to run the app and must be inserted into the .env file in the project's base directory:
```
REACT_VERSION=18.2.0
```

# Running The Project
To run this project, cd into the 'CPS-Analysis' folder and run the app.py file. The local address of the dashboard should be logged to the terminal.

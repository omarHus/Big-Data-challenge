# Big Data Challenge


> NOTE: this is still under construction

## Environment setup
### Pre-requisite installations:
- Git
- Python 3.x (confirm by ___python --version___)
- Python pip (confirm by ___pip --version___)
- Python virtualenv
- Visual Studio Code (or any IDE of your choice) 
- *Database TBD...* probably wont need 

### Start steps (API)
1. Open Terminal (or GitBash on Windows) and navigate to `/src` directory
2. Create a venv: `python -m venv env`
3. Activate the virtual environment: `source env/Scripts/activate`
4. Run the following commands to install your environment dependencies: `pip install -r requirements.txt`
5. To run the API application execute the following: `flask run`. You will then be able to hit the API from your browser using ` http://127.0.0.1:5000/`

### Shutdown steps
1. Deactivate the virtual environment: `deactivate`

### Adding Dependencies (If needed)
If you'd like to add dependencies, follow the steps below:
PLEASE NOTE: You need to have your virtual environment activated for the below to work
1. Open Terminal (or GitBash on Windows) and navigate to `/src` directory
2. Install the needed packages: `pip install <package name>`
3. Update requirements file: `pip freeze > requirements.txt`

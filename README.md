# Basic-Flask-Project #


### Follow the instructions to install the project ###

* Download the github project and extract it.
* Install python(3.7 or above) and pip if not already installed.
* To install pip, use command: py -m pip
* You could see that app.py is in the restauranto folder openly and not inside another folder.
* Now let's install the virtual environment. Open the command line inside the restauranto folder. Use the following commands in the command line:
            * pip install virtualenv
            * virtualenv --version
            * virtualenv --python=python3 venv
* You can see a folder named "venv" is created.
* In the command line opened in restauranto folder, write this: "venv\Scripts\activate" and press "enter".  It may be different if it is a git bash.
* If Venv is activated, there will be notation as (venv) near command line address.
* If venv is activated, then install packages in requirements file using command:
                        * "pip install -r requirements.txt"
* This will install all required packages.
* So the project folder contains "app.py","templates","static" and "venv" folder.
* If all the above process is done correctly, Then you can run it on localhost
    using command: "py app.py"
* App will run in http://127.0.0.1:5000/index




* There are some extra dependencies, to install to download bill as pdf. To download pdf from customer module, we have to install "wkhtmltox" which i cannot attach to the git. Install it and set it to environment variable.



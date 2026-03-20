This project demonstrates a scalable API test automation framework built using Python and Pytest. It follows best practices such as separation of concerns, reusable API clients, environment configuration, and fixture-based test setup.

Steps to run :

#Create virtual environment
python3 -m venv venv
source venv/bin/activate

#Install needed packages
pip install pytest requests

#Save the dependencies for future reference
pip freeze > requirements.txt

#Export current directory as python path
export PYTHONPATH=.

#Run Pytest
Pytest

Sample o/p :

![alt text]()
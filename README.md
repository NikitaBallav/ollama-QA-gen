chat_url folder consist of the indexes and the python notebook for the jigyasa bot

jigyasa folder consist of the django api source code 

the dggi folder consist of the training done with dggi website

Steps to follow:

1. In command prompt: git clone
2. In command prompt: cd ollama_QA_gen
3. Open settings.py
4. Update the path of the index in the persist directory according to the local machine path.
5. In command prompt: pip install pipenv (python 3.12 is used, make sure to have the compatible version for pipenv)
6. In command prompt: pipenv install
7. In case of error caused by pipenv compatiblity with the dependencies: in command prompt, del pipenv.log
8. In command prompt: pipenv shell (this will activate the environment required)
9. To run the server: python manage.py runserver 0.0.0.0:7777
10. To check the running status, use postman with a POST request for (0.0.0.0:7777/api/jigyasa), in the request body choose raw and JSON type, write the json format of the input query and send.

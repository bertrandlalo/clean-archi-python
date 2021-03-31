# Clean-Archi-Python 🇬🇧

(Version française [ici](README.fr.md).)

The design is inspired from the book [Cosmic Python](https://www.cosmicpython.com/). By the way, I'd encourage you to read it.

## Guidelines
### Install 
Create a virtual environment, install the packages and the source. 
```
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
pip install -e ./src
```

### Launch the tests
```
docker-compose -f tests/pg-docker-compose.yml up --build
pytest tests 
```

### Launch the app 
```
python src/entrypoints/server.py
```

## "Clean" organization 
Here is a nice illustration on hexagonal clean architecture : 

![hexagonal-archi](hexagonal-1.png)

If you open the src code, you'll notice the following organization :

- **DOMAIN**

  - **ports:** dependency API where we define how the application interacts with external "bricks". For example, a repository port would have a method "add". The actual implementation of those "bricks" are made by adapters. The ports are tested in tests/unit. 

  - **use cases:** all the application specific business rules gets divided into list of use cases, each having a single responsability. For example: create a new user and add it in a repository. The use-cases are tested in tests/unit. 

  - ...

- **ADAPTERS**:
  The actual implementation of the ports. For example, a repository could be implemented with Postgres database, hence the "add" method would be an INSERT. The adapters are tested in tests/integration. 

- **ENTRYPOINTS**:
  - ./server.py : the script to launch the application.
  - ./config.py : preparation of the application instances. 
  The entrypoint is tested in tests/e2e. 

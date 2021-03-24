# Clean-Archi-Python 🇫🇷 🇬

(English version [here](README.md).)


Le design est inspiré du livre [Cosmic Python](https://www.cosmicpython.com/) dont je vous encourage la lecture !

## Guidelines
### Installation
Créer un nouvel environnement virtuel, et y installer les pacquets et la source.
```
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
pip install -e ./src
```

### Lancer les tests
```
docker-compose -f tests/pg-docker-compose.yml up --build
pytest tests 
```

### Lancer l'application
```
python src/entrypoints/server.py
```

## "Clean Archi" 

Si vous ouvrez le dossier src, vous remarquerez l'organisation suivante :

- **DOMAIN**
    - **ports:** API de dépendance où nous définissons comment l'application interagit avec des "briques" externes. Par exemple, un port de dépôt aurait une méthode "add". La mise en œuvre réelle de ces "briques" se fait par des adaptateurs.
    Les ports sont testés dans tests/unit. 

    - **Use cases:** toutes les règles métier spécifiques à l'application sont divisées en une liste de cas d'usage, chacun ayant une seule responsabilité. Par exemple: stocker le nouvel événement dans un dépôt.
    Les use-cases sont testés dans tests/unit.  
    - ...
- **ADAPTATERS**:
    La mise en œuvre réelle des ports. Par exemple, un référentiel pourrait être implémenté avec la base de données Postgres, donc la méthode "add" serait un INSERT. 
    Les adapters sont testés dans tests/integration. 

- **ENTRYPOINTS**:
   - ./server.py: le script pour lancer l'application.
   - ./config.py: préparation des instances de l'application.
   Le serveur est testé dans tests/e2e. 

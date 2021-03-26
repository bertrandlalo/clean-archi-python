import os

from adapters.ndb.ndb_user_repository import NDBUserRepository
from .model import Model

class LocalConfig(Model):
    def __init__(self):
        os.environ['DATASTORE_EMULATOR_HOST'] = '0.0.0.0:8000'  # in docker emulator port.
        self.user_repo = NDBUserRepository(project_id='clean-experquiz')
        self.testing = True
        # self.flask_config = {"TESTING": True, 'SECRET_KEY': '123456'}


from injector import singleton, provider, Module

from flask_app.repos import AccountRepository


class ProdDatabaseModule(Module):
    @singleton
    @provider
    def provide_the_repository(self) -> AccountRepository:
        return AccountRepository()

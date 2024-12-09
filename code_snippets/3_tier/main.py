

# initializer

from business_logic.interfaces.person_repo_interface import PersonRepoInterface
from data_access.repo.person_mapper import PersonMapper
from business_logic.domain_controller import DomainController
from presentation.app import App

def initialize():
    person_mapper: PersonRepoInterface = PersonMapper() 
    domain_controller = DomainController(person_mapper)
    app = App(domain_controller)
    return app

if __name__ == "__main__":
    app = initialize()
    app.run()



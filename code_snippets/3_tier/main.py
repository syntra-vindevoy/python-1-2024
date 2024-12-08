

# initializer

from presentation import Presentation
from business_logic import BusinessLogic
from data_access import DataAccess

def initialize():
    data_access = DataAccess()
    business_logic = BusinessLogic(data_access)
    presentation = Presentation(business_logic)
    return presentation

if __name__ == "__main__":
    presentation = initialize()
    presentation.run()



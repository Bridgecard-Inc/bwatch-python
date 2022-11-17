import sys


# this is a pointer to the module object instance itself.
this = sys.modules[__name__]


def init(app_id: str):
    """
    Initialises Bwatch package.

    """
    this.app_id = app_id
    return 
    

def __get_app_id():
    """
    Internal function to get get current app id

    """
    return this.app_id 
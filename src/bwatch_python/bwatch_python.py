import sys


# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

class Bwatch:
    def __init__(self, app_id: str):
        """
        Initialises Bwatch package.

        """
        this.app_id = app_id
        return 

    
import importlib
import os
from backend.config import LIBS_LOCATION
from backend.log import debug

def create_namespace() -> dict[str, any]:
    """
    Looks in the 'libs' folder and dynamically creates a namespace,
    which is returned back to the program
    """
    namespace = {

    }

    for lib in os.listdir(LIBS_LOCATION):
        if lib in ["__init__.py", "__pycache__"]:
            continue

        debug(f"found library {LIBS_LOCATION}/{lib}")

        # Converts, e.g. print to Print (which should be the class name)
        class_name = lib.title()[:-3]
        module_name = lib[:-3]

        lib_class = getattr(importlib.import_module(f"{LIBS_LOCATION}.{module_name}"), class_name)

        class_object = lib_class()

        namespace[class_object.function_name] = class_object

        debug(f"generated and added library {module_name} to the namespace")


    return namespace

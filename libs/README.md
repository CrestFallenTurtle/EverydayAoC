Libraries added here that follow the common rules will be dynamically imported
when the software is executed.

## General syntax to follow
In order to get your lib imported, your library needs to follow a certain guideline.

#### File name
The file name should be the class name but in all lowercase, for example, if the class name is "Print", then the filename should be "print.py"

#### Class structure
Each class should have a titled filename, so if the file is called "print.py", then the class should be called "Print".

Each class should atleast have two methods definied, `__init__` and `start`.
The `__init__` method should not take in any arguments, and should really only contain the variable, `self.function_name` which should contain
the required function name that the programmer enters in order to execute this class.

All the magic is left to be done in the `start` method, which is required to have the following imports
    
    * self
    * arguments:list[str]
    * var_namespace:dict[str, any]
    * method_namespace:dict[str, any]
    * lib_namespace:dict[str, any]

If these aren't present, or if there is more arguments, then the main importer will fail to import your class

So, to give a shitty explanation on things here, 

    * arguments will contain every argument passed to your method
    * var_namespace is a namespace were every variable definied will be contained
    * method_namespace is a namespace were every method definied will be contained
    * lib_namespace is a namespace were every library definied will be contained

    
#### Example class
Here is an example class that you can easily build ontop off
```
class <Class Name>:

    def __init__(self) -> None:
        self.function_name = "<function to call to execute this class>"

        def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """ main meat method each library """
        < do the libraries magic >

```
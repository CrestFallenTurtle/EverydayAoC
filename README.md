# PyAss

![](images/craiyon_125433_A_slithering_diamondback_rattlesnake_casually_coils_across_a_table__eyeing_a_pile_of_.png)



## Syntax and program layout

### Variable Declaration
Within each program there is a dedicated section where the programmer can declare all variables that will be utilized
during the programs execution and lifetime. This area begins with a `WAKE UP` followed by a simple variable declaration as can be seen in multiple languages.

#### Example
```
WAKE UP
 A = 10
 B = 20
 C = 30

...
```
The declaration area will continue until the function declaration area is declared.

No function calls are allowed to take place within this section, and are reserved to the function declaration and the main declaration.

### Function Declaration
Method/functions can only be declared within the `EVERYDAY I WAKE UP` section, variables are not allowed to be declared here.

#### Example
```
EVERYDAY I WAKE UP

    foo:
        print $str
        add $a, $b, $c

    boo:
        print $c
```

### Main loop Declaration
All of the meat of the program should primarly be reserved to the main loop, `PIECE OF SHIT`. 

#### Example
```
PIECE OF SHIT
    gtfo foo, boo
```

### Exiting loop Declaration
The exiting loop, `FUCK THIS SHIT`, is left to be utilized by the user in order to do some last minute things before the software exits.

```
FUCK THIS SHIT
    print "I'm out of here"
```

### Program Layout

### Available syntaxes
General operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `print` | Prints the provides value/s | `print $a, $c, "Hello"` |
| `obtain`| Takes a user input, and saves it in a variable  | `obtain $a` |
| `ass`| Assigns the provided value into one or more variables during runtime | `ass 69, $a, $b` |
| `judge`| Compares two values, and jumps to one of the corresponding methods as a result | `judge $a, $b, foo, boo` |

Bitwise operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `band` | Bitwise And, results are placed in the last provided variable  | `band $a, $b, $c` |
| `bor`| Bitwise Or, results are placed in the last provided variable  | `bor $a, $b, $c` |
| `bxor`| Bitwise Xor, results are placed in the last provided variable  | `bxor $a, $b, $c` |
| `lshift`| Bitwise left shift, results are placed in the last provided variable | `lshift $a, $b, $c` |
| `rshift`| Bitwise right shift, results are placed in the last provided variable | `rshift $a, $b, $c` |
| `bnot`| Bitwise not, results are placed in the last provided variable | `bnot $a, $c` |

Math operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `add` | Adds two values, results are placed in the last provided variable | `add $a, $b, $c` |
| `sub`| Subs two values, results are placed in the last provided variable | `sub $a, $b, $c` |
| `mult`| Multiplies two values, results are placed in the last provided variable | `mult $a, $b, $c` |
| `div`| Divides two values, results are placed in the last provided variable | `div $a, $b, $c` |
| `mod`| Perfoms a modular operation on two values, results are placed in the last provided variable | `mod $a, $b, $c` |


### Example program
```
WAKE UP
    str="Hello World"
    a=10
    b=20
    c=0

EVERYDAY I WAKE UP

    foo:
        print $str
        add $a, $b, $c

    boo:
        print $c

PIECE OF SHIT
    gtfo foo, boo

FUCK THIS SHIT

```

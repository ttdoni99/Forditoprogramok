# CYK Algorithm in Python

This python script is an implementation of the CYK Algorithm. This scripts can determine whether a string can be derived from a grammar based on the rules of the (context free) grammar.

## Usage:
### Linux(on distros where python2 is default)
```bash
    python3 main.py <file containing the rules> [string to be analyzed]
```
If you leave out the string to be analyzed then at the start of the script it will prompt the user to input it.

### Windows and other Linux distros
```bash
    python main.py <file containing the rules> [string to be analyzed]
```
If you leave out the string to be analyzed then at the start of the script it will prompt the user to input it.

### Note:
This will probably work on MacOS the same as one of the options mentioned before.

## The format of the file containing the rules of the grammar:
This script can't handle rules like:  
```
S -> AB | CB | d
```  
You can define rules like this:  
```
S AB
S CB
S d
```  
You must not include the '->'s in the rule file. And you have to write out separately all the rules, can't combine the ones with the same left-side.

## Note:
This is probably not the most efficient implementation of the CYK algorithm but it's short and works just fine.
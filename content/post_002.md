Title: List Comps
Date: 2015-07-07
Category: python
Tags: arcpy

If I had to choose my single favorite programming idiom in Python, I wouldn't even need to pause to consider; hands down, it's list comprehensions. I use them all the time, and once you understand them, so will you. They are easy to, well, comprehend, and yet allow you to do powerful things concisely.

### Syntax
Let's look at the basic syntax. At its heart, a list comprehension (or 'list comp') is simply a way to build a new list from an existing sequence or iterable. Suppose you have a list of words:
```python
words = ['i', 'freaking', 'love', 'list', 'comps']
```
Now let's say you want to build a list of uppercase words from this list of lowercase words. You might first create an empty list, and then in a ```for``` loop append the result of ```upper()```:
```python
cap_words = []
for word in words:
    cap_words.append(word.upper())
> ['I', 'FREAKING', 'LOVE', 'LIST', 'COMPS']
```
Using a list comp, you can do this more effieciently:
```python
cap_words = [word.upper() for word in words]
> ['I', 'FREAKING', 'LOVE', 'LIST', 'COMPS']
```
Basically you now have an expression (the part doing the real work here) followed by a ```for``` loop, all wrapped up in brackets and assigned to ```cap_words```. Three lines have become one. The gain in conciseness is reason enough to use them, but list comps also give you the ability to filter while constructing your new list.

### Filtering Using ```if```
List comps accept an optional ```if``` clause at the end, after the ```for``` loop:
```python
cap_words = [word.upper() for word in words if word is 'freaking']
> ['FREAKING']
```
What happened here? The ```if``` statement (```if word is 'freaking'```) was applied to each element of ```words``` in turn. Only those elements which evaluate to True are passed to the expression ```word.upper()```. 

Note that this list comprehension is very readable. Say it out loud: it returns "word dot upper for word in words if word is 'freaking'." Once you understand list comp syntax, it is easy to grasp what any given list comp is doing (nested list comps being a possible exception). Using a list comp is like thinking a complete thought or phrase. This ease of expression is one of its great strengths.

### ```if...else```
List comps can accept ```if...else``` statements as well, though the the order is different:
```python
cap_words = [word.upper() if word is 'freaking' else word for word in words]
> ['i', 'FREAKING', 'love', 'list', 'comps']
```
Nested list comps can be slightly more confusing, but allow you to create a list by iterating through multiple lists. See 'Further Reading' for examples.

### Use-Cases
Let's get to some specific arcpy use-cases. I frequently use list comps to iterate through specific file types in a directory. For instance, let's say I want to do something to a folder full of mxds, while leaving other files in the folder alone. Use a list comprehension with a filter to put the mxd names into a list:
```python
import os
mxds = [file for file in os.listdir(<directory path>) if file.endswith('.mxd')]
> ['Figure 1.mxd', 'Figure 2.mxd', etc...]
```
Now it is easy to iterate over only those mxds:
```python
for mxd in mxds:
    # do something
```

Need full paths to those mxds? Use a list comp to transform the ```mxds``` list into a new list:
```python
import os
dir = r'C:\project'
full_paths = [os.path.join(dir, mxd) for mxd in mxds]
> ['C:\project\Figure 1.mxd', 'C:\project\Figure 2.mxd', etc...]
```
Or, create full paths at the same time you filter for .mxd:
```python
import os
dir = r'C:\project'
full_paths = [os.path.join(dir, file) for file in os.listdir(<directory path>) if file.endswith('.mxd')]
```
Another use is to build a list of fieldnames from a feature class:
```python
import arcpy
fieldnames = [field.name for field in arcpy.ListFields(<path to feature class>)]
```
Or read a feature class into a list:
```python
fields = arcpy.ListFields(<mxd path>)
data = [row for row in arcpy.da.SearchCursor(<path to feature class>, fields)]
```
Any time you want to build a list, filter a list, or transform one list into another, you should think to yourself: "I FREAKING LOVE LIST COMPS"!

### Further Reading:

+ https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

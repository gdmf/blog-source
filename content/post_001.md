Title: arcpy documentation
Date: 2015-06-29
Tags: python, arcpy

Need a listing of the arcpy package? Here's how to write the documentation to a file:

```python
import arcpy
import pydoc
out_file = r'c:\home\pydev\arcpy_docs.txt' 
strhelp = pydoc.plain(pydoc.render_doc(arcpy, "Help on %s"))
with open(out_file, 'w') as destination:
	destination.write(strhelp)
```

Two things about this were not obvious to me. First, for unknown (to me, at least) reasons, writing ```arcpy.__doc__``` to a file results in a TypeError. The call to ```pydoc.render_doc``` [gets around](http://stackoverflow.com/questions/7123660/python-help-function-printing-docstrings, "Thanks, stackoverflow!") that. 

Secondly, the output contains some unsightly boldface formatting. The call to ```pydoc.plain``` [removes it](http://stackoverflow.com/questions/15133537/pydoc-render-doc-adds-characters-how-to-avoid-that,).

Here's another useful tip: use arcpy's Usage method to list the parameters for any tool.
```python
print arcpy.Usage("Clip_analysis")
```
Get complete help information from the docstring:
```python
print arcpy.Clip_analysis.__doc__
```


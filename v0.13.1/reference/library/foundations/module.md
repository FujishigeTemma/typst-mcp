# Module

A collection of variables and functions that are commonly related to
a single theme.

A module can
- be built-in
- stem from a [file import]($scripting/#modules)
- stem from a [package import]($scripting/#packages) (and thus indirectly
  its entrypoint file)
- result from a call to the [plugin]($plugin) function

You can access definitions from the module using [field access
notation]($scripting/#fields) and interact with it using the [import and
include syntaxes]($scripting/#modules). Alternatively, it is possible to
convert a module to a dictionary, and therefore access its contents
dynamically, using the [dictionary constructor]($dictionary/#constructor).

# Example
```example
<<< #import "utils.typ"
<<< #utils.add(2, 5)

<<< #import utils: sub
<<< #sub(1, 4)
>>> #7
>>>
>>> #(-3)
```


# Evaluate

## `eval`

Evaluates a string as Typst code.

This function should only be used as a last resort.

# Example
```example
#eval("1 + 1") \
#eval("(1, 2, 3, 4)").len() \
#eval("*Markup!*", mode: "markup") \
```

## Parameters

### source *(required)*

A string of Typst code to evaluate.

### mode 

The [syntactical mode]($reference/syntax/#modes) in which the string is
parsed.



### scope 

A scope of definitions that are made available.



## Returns

- any


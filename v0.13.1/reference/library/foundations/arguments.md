# Arguments

Captured arguments to a function.

# Argument Sinks
Like built-in functions, custom functions can also take a variable number of
arguments. You can specify an _argument sink_ which collects all excess
arguments as `..sink`. The resulting `sink` value is of the `arguments`
type. It exposes methods to access the positional and named arguments.

```example
#let format(title, ..authors) = {
  let by = authors
    .pos()
    .join(", ", last: " and ")

  [*#title* \ _Written by #by;_]
}

#format("ArtosFlow", "Jane", "Joe")
```

# Spreading
Inversely to an argument sink, you can _spread_ arguments, arrays and
dictionaries into a function call with the `..spread` operator:

```example
#let array = (2, 3, 5)
#calc.min(..array)
#let dict = (fill: blue)
#text(..dict)[Hello]
```

## Constructor

### `arguments`

Construct spreadable arguments in place.

This function behaves like `{let args(..sink) = sink}`.




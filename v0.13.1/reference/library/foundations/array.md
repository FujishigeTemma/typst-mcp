# Array

A sequence of values.

You can construct an array by enclosing a comma-separated sequence of values
in parentheses. The values do not have to be of the same type.

You can access and update array items with the `.at()` method. Indices are
zero-based and negative indices wrap around to the end of the array. You can
iterate over an array using a [for loop]($scripting/#loops). Arrays can be
added together with the `+` operator, [joined together]($scripting/#blocks)
and multiplied with integers.

**Note:** An array of length one needs a trailing comma, as in `{(1,)}`.
This is to disambiguate from a simple parenthesized expressions like `{(1 +
2) * 3}`. An empty array is written as `{()}`.

# Example
```example
#let values = (1, 7, 4, -3, 2)

#values.at(0) \
#(values.at(0) = 3)
#values.at(-1) \
#values.find(calc.even) \
#values.filter(calc.odd) \
#values.map(calc.abs) \
#values.rev() \
#(1, (2, 3)).flatten() \
#(("A", "B", "C")
    .join(", ", last: " and "))
```

## Constructor

### `array`

Converts a value to an array.

Note that this function is only intended for conversion of a collection-like
value to an array, not for creation of an array from individual items. Use
the array syntax `(1, 2, 3)` (or `(1,)` for a single-element array) instead.




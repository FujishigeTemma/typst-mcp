# Float

A floating-point number.

A limited-precision representation of a real number. Typst uses 64 bits to
store floats. Wherever a float is expected, you can also pass an
[integer]($int).

You can convert a value to a float with this type's constructor.

NaN and positive infinity are available as `{float.nan}` and `{float.inf}`
respectively.

# Example
```example
#3.14 \
#1e4 \
#(10 / 4)
```

## Constructor

### `float`

Converts a value to a float.

- Booleans are converted to `0.0` or `1.0`.
- Integers are converted to the closest 64-bit float. For integers with
  absolute value less than `{calc.pow(2, 53)}`, this conversion is
  exact.
- Ratios are divided by 100%.
- Strings are parsed in base 10 to the closest 64-bit float. Exponential
  notation is supported.




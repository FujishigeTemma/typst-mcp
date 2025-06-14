# Integer

A whole number.

The number can be negative, zero, or positive. As Typst uses 64 bits to
store integers, integers cannot be smaller than `{-9223372036854775808}` or
larger than `{9223372036854775807}`. Integer literals are always positive,
so a negative integer such as `{-1}` is semantically the negation `-` of the
positive literal `1`. A positive integer greater than the maximum value and
a negative integer less than or equal to the minimum value cannot be
represented as an integer literal, and are instead parsed as a `{float}`.
The minimum integer value can still be obtained through integer arithmetic.

The number can also be specified as hexadecimal, octal, or binary by
starting it with a zero followed by either `x`, `o`, or `b`.

You can convert a value to an integer with this type's constructor.

# Example
```example
#(1 + 2) \
#(2 - 5) \
#(3 + 4 < 8)

#0xff \
#0o10 \
#0b1001
```

## Constructor

### `int`

Converts a value to an integer. Raises an error if there is an attempt
to produce an integer larger than the maximum 64-bit signed integer
or smaller than the minimum 64-bit signed integer.

- Booleans are converted to `0` or `1`.
- Floats and decimals are truncated to the next 64-bit integer.
- Strings are parsed in base 10.




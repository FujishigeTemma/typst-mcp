# Calculation

Module for calculations and processing of numeric values.

These definitions are part of the `calc` module and not imported by default.
In addition to the functions listed below, the `calc` module also defines
the constants `pi`, `tau`, `e`, and `inf`.


## Functions

### `abs`

Calculates the absolute value of a numeric value.



### `pow`

Raises a value to some exponent.



### `exp`

Raises a value to some exponent of e.



### `sqrt`

Calculates the square root of a number.



### `root`

Calculates the real nth root of a number.

If the number is negative, then n must be odd.



### `sin`

Calculates the sine of an angle.

When called with an integer or a float, they will be interpreted as
radians.



### `cos`

Calculates the cosine of an angle.

When called with an integer or a float, they will be interpreted as
radians.



### `tan`

Calculates the tangent of an angle.

When called with an integer or a float, they will be interpreted as
radians.



### `asin`

Calculates the arcsine of a number.



### `acos`

Calculates the arccosine of a number.



### `atan`

Calculates the arctangent of a number.



### `atan2`

Calculates the four-quadrant arctangent of a coordinate.

The arguments are `(x, y)`, not `(y, x)`.



### `sinh`

Calculates the hyperbolic sine of a hyperbolic angle.



### `cosh`

Calculates the hyperbolic cosine of a hyperbolic angle.



### `tanh`

Calculates the hyperbolic tangent of an hyperbolic angle.



### `log`

Calculates the logarithm of a number.

If the base is not specified, the logarithm is calculated in base 10.



### `ln`

Calculates the natural logarithm of a number.



### `fact`

Calculates the factorial of a number.



### `perm`

Calculates a permutation.

Returns the `k`-permutation of `n`, or the number of ways to choose `k`
items from a set of `n` with regard to order.



### `binom`

Calculates a binomial coefficient.

Returns the `k`-combination of `n`, or the number of ways to choose `k`
items from a set of `n` without regard to order.



### `gcd`

Calculates the greatest common divisor of two integers.



### `lcm`

Calculates the least common multiple of two integers.



### `floor`

Rounds a number down to the nearest integer.

If the number is already an integer, it is returned unchanged.

Note that this function will always return an [integer]($int), and will
error if the resulting [`float`] or [`decimal`] is larger than the maximum
64-bit signed integer or smaller than the minimum for that type.



### `ceil`

Rounds a number up to the nearest integer.

If the number is already an integer, it is returned unchanged.

Note that this function will always return an [integer]($int), and will
error if the resulting [`float`] or [`decimal`] is larger than the maximum
64-bit signed integer or smaller than the minimum for that type.



### `trunc`

Returns the integer part of a number.

If the number is already an integer, it is returned unchanged.

Note that this function will always return an [integer]($int), and will
error if the resulting [`float`] or [`decimal`] is larger than the maximum
64-bit signed integer or smaller than the minimum for that type.



### `fract`

Returns the fractional part of a number.

If the number is an integer, returns `0`.



### `round`

Rounds a number to the nearest integer.

Half-integers are rounded away from zero.

Optionally, a number of decimal places can be specified. If negative, its
absolute value will indicate the amount of significant integer digits to
remove before the decimal point.

Note that this function will return the same type as the operand. That is,
applying `round` to a [`float`] will return a `float`, and to a [`decimal`],
another `decimal`. You may explicitly convert the output of this function to
an integer with [`int`], but note that such a conversion will error if the
`float` or `decimal` is larger than the maximum 64-bit signed integer or
smaller than the minimum integer.

In addition, this function can error if there is an attempt to round beyond
the maximum or minimum integer or `decimal`. If the number is a `float`,
such an attempt will cause `{float.inf}` or `{-float.inf}` to be returned
for maximum and minimum respectively.



### `clamp`

Clamps a number between a minimum and maximum value.



### `min`

Determines the minimum of a sequence of values.



### `max`

Determines the maximum of a sequence of values.



### `even`

Determines whether an integer is even.



### `odd`

Determines whether an integer is odd.



### `rem`

Calculates the remainder of two numbers.

The value `calc.rem(x, y)` always has the same sign as `x`, and is smaller
in magnitude than `y`.

This can error if given a [`decimal`] input and the dividend is too small in
magnitude compared to the divisor.



### `div-euclid`

Performs euclidean division of two numbers.

The result of this computation is that of a division rounded to the integer
`{n}` such that the dividend is greater than or equal to `{n}` times the divisor.



### `rem-euclid`

This calculates the least nonnegative remainder of a division.

Warning: Due to a floating point round-off error, the remainder may equal
the absolute value of the divisor if the dividend is much smaller in
magnitude than the divisor and the dividend is negative. This only applies
for floating point inputs.

In addition, this can error if given a [`decimal`] input and the dividend is
too small in magnitude compared to the divisor.



### `quo`

Calculates the quotient (floored division) of two numbers.

Note that this function will always return an [integer]($int), and will
error if the resulting [`float`] or [`decimal`] is larger than the maximum
64-bit signed integer or smaller than the minimum for that type.



### `norm`

Calculates the p-norm of a sequence of values.




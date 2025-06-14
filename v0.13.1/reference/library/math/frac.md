# Fraction

## `frac`

A mathematical fraction.

# Example
```example
$ 1/2 < (x+1)/2 $
$ ((x+1)) / 2 = frac(a, b) $
```

# Syntax
This function also has dedicated syntax: Use a slash to turn neighbouring
expressions into a fraction. Multiple atoms can be grouped into a single
expression using round grouping parentheses. Such parentheses are removed
from the output, but you can nest multiple to force them.

## Parameters

### num *(required)*

The fraction's numerator.

### denom *(required)*

The fraction's denominator.

## Returns

- content


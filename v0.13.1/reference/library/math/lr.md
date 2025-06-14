# Left/Right

Delimiter matching.

The `lr` function allows you to match two delimiters and scale them with the
content they contain. While this also happens automatically for delimiters
that match syntactically, `lr` allows you to match two arbitrary delimiters
and control their size exactly. Apart from the `lr` function, Typst provides
a few more functions that create delimiter pairings for absolute, ceiled,
and floored values as well as norms.

To prevent a delimiter from being matched by Typst, and thus auto-scaled,
escape it with a backslash. To instead disable auto-scaling completely, use
`{set math.lr(size: 1em)}`.

# Example
```example
$ [a, b/2] $
$ lr(]sum_(x=1)^n], size: #50%) x $
$ abs((x + y) / 2) $
$ \{ (x / y) \} $
#set math.lr(size: 1em)
$ { (a / b), a, b in (0; 1/2] } $
```


## Functions

### `lr`

Scales delimiters.

While matched delimiters scale by default, this can be used to scale
unmatched delimiters and to control the delimiter scaling more precisely.

### `mid`

Scales delimiters vertically to the nearest surrounding `{lr()}` group.



### `abs`

Takes the absolute value of an expression.



### `norm`

Takes the norm of an expression.



### `floor`

Floors an expression.



### `ceil`

Ceils an expression.



### `round`

Rounds an expression.




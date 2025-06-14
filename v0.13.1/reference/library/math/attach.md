# Attach

Subscript, superscripts, and limits.

Attachments can be displayed either as sub/superscripts, or limits. Typst
automatically decides which is more suitable depending on the base, but you
can also control this manually with the `scripts` and `limits` functions.

If you want the base to stretch to fit long top and bottom attachments (for
example, an arrow with text above it), use the [`stretch`]($math.stretch)
function.

# Example
```example
$ sum_(i=0)^n a_i = 2^(1+i) $
```

# Syntax
This function also has dedicated syntax for attachments after the base: Use
the underscore (`_`) to indicate a subscript i.e. bottom attachment and the
hat (`^`) to indicate a superscript i.e. top attachment.


## Functions

### `attach`

A base with optional attachments.



### `scripts`

Forces a base to display attachments as scripts.



### `limits`

Forces a base to display attachments as limits.




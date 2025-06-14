# Equation

## `equation`

A mathematical equation.

Can be displayed inline with text or as a separate block. An equation
becomes block-level through the presence of at least one space after the
opening dollar sign and one space before the closing dollar sign.

# Example
```example
#set text(font: "New Computer Modern")

Let $a$, $b$, and $c$ be the side
lengths of right-angled triangle.
Then, we know that:
$ a^2 + b^2 = c^2 $

Prove by induction:
$ sum_(k=1)^n k = (n(n+1)) / 2 $
```

By default, block-level equations will not break across pages. This can be
changed through `{show math.equation: set block(breakable: true)}`.

# Syntax
This function also has dedicated syntax: Write mathematical markup within
dollar signs to create an equation. Starting and ending the equation with at
least one space lifts it into a separate block that is centered
horizontally. For more details about math syntax, see the
[main math page]($category/math).

## Parameters

### block 

Whether the equation is displayed as a separate block.

### numbering 

How to [number]($numbering) block-level equations.



### number-align 

The alignment of the equation numbering.

By default, the alignment is `{end + horizon}`. For the horizontal
component, you can use `{right}`, `{left}`, or `{start}` and `{end}`
of the text direction; for the vertical component, you can use
`{top}`, `{horizon}`, or `{bottom}`.



### supplement 

A supplement for the equation.

For references to equations, this is added before the referenced number.

If a function is specified, it is passed the referenced equation and
should return content.



### body *(required)*

The contents of the equation.

## Returns

- content


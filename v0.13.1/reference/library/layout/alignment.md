# Alignment

Where to [align] something along an axis.

Possible values are:
- `start`: Aligns at the [start]($direction.start) of the [text
  direction]($text.dir).
- `end`: Aligns at the [end]($direction.end) of the [text
  direction]($text.dir).
- `left`: Align at the left.
- `center`: Aligns in the middle, horizontally.
- `right`: Aligns at the right.
- `top`: Aligns at the top.
- `horizon`: Aligns in the middle, vertically.
- `bottom`: Align at the bottom.

These values are available globally and also in the alignment type's scope,
so you can write either of the following two:

```example
#align(center)[Hi]
#align(alignment.center)[Hi]
```

# 2D alignments
To align along both axes at the same time, add the two alignments using the
`+` operator. For example, `top + right` aligns the content to the top right
corner.

```example
#set page(height: 3cm)
#align(center + bottom)[Hi]
```

# Fields
The `x` and `y` fields hold the alignment's horizontal and vertical
components, respectively (as yet another `alignment`). They may be `{none}`.

```example
#(top + right).x \
#left.x \
#left.y (none)
```


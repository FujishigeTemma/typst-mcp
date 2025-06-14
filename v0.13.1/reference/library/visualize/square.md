# Square

## `square`

A square with optional content.

# Example
```example
// Without content.
#square(size: 40pt)

// With content.
#square[
  Automatically \
  sized to fit.
]
```

## Parameters

### size 

The square's side length. This is mutually exclusive with `width` and
`height`.

### width 

The square's width. This is mutually exclusive with `size` and `height`.

In contrast to `size`, this can be relative to the parent container's
width.

### height 

The square's height. This is mutually exclusive with `size` and `width`.

In contrast to `size`, this can be relative to the parent container's
height.

### fill 

How to fill the square. See the [rectangle's documentation]($rect.fill)
for more details.

### stroke 

How to stroke the square. See the
[rectangle's documentation]($rect.stroke) for more details.

### radius 

How much to round the square's corners. See the
[rectangle's documentation]($rect.radius) for more details.

### inset 

How much to pad the square's content. See the
[box's documentation]($box.inset) for more details.

### outset 

How much to expand the square's size without affecting the layout. See
the [box's documentation]($box.outset) for more details.

### body 

The content to place into the square. The square expands to fit this
content, keeping the 1-1 aspect ratio.

When this is omitted, the square takes on a default size of at most
`{30pt}`.

## Returns

- content


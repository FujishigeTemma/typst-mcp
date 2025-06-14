# Rectangle

## `rect`

A rectangle with optional content.

# Example
```example
// Without content.
#rect(width: 35%, height: 30pt)

// With content.
#rect[
  Automatically sized \
  to fit the content.
]
```

## Parameters

### width 

The rectangle's width, relative to its parent container.

### height 

The rectangle's height, relative to its parent container.

### fill 

How to fill the rectangle.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.



### stroke 

How to stroke the rectangle. This can be:

- `{none}` to disable stroking
- `{auto}` for a stroke of `{1pt + black}` if and if only if no fill is
  given.
- Any kind of [stroke]
- A dictionary describing the stroke for each side individually. The
  dictionary can contain the following keys in order of precedence:
  - `top`: The top stroke.
  - `right`: The right stroke.
  - `bottom`: The bottom stroke.
  - `left`: The left stroke.
  - `x`: The horizontal stroke.
  - `y`: The vertical stroke.
  - `rest`: The stroke on all sides except those for which the
    dictionary explicitly sets a size.



### radius 

How much to round the rectangle's corners, relative to the minimum of
the width and height divided by two. This can be:

- A relative length for a uniform corner radius.
- A dictionary: With a dictionary, the stroke for each side can be set
  individually. The dictionary can contain the following keys in order
  of precedence:
  - `top-left`: The top-left corner radius.
  - `top-right`: The top-right corner radius.
  - `bottom-right`: The bottom-right corner radius.
  - `bottom-left`: The bottom-left corner radius.
  - `left`: The top-left and bottom-left corner radii.
  - `top`: The top-left and top-right corner radii.
  - `right`: The top-right and bottom-right corner radii.
  - `bottom`: The bottom-left and bottom-right corner radii.
  - `rest`: The radii for all corners except those for which the
    dictionary explicitly sets a size.



### inset 

How much to pad the rectangle's content.
See the [box's documentation]($box.inset) for more details.

### outset 

How much to expand the rectangle's size without affecting the layout.
See the [box's documentation]($box.outset) for more details.

### body 

The content to place into the rectangle.

When this is omitted, the rectangle takes on a default size of at most
`{45pt}` by `{30pt}`.

## Returns

- content


# Ellipse

## `ellipse`

An ellipse with optional content.

# Example
```example
// Without content.
#ellipse(width: 35%, height: 30pt)

// With content.
#ellipse[
  #set align(center)
  Automatically sized \
  to fit the content.
]
```

## Parameters

### width 

The ellipse's width, relative to its parent container.

### height 

The ellipse's height, relative to its parent container.

### fill 

How to fill the ellipse. See the [rectangle's documentation]($rect.fill)
for more details.

### stroke 

How to stroke the ellipse. See the
[rectangle's documentation]($rect.stroke) for more details.

### inset 

How much to pad the ellipse's content. See the
[box's documentation]($box.inset) for more details.

### outset 

How much to expand the ellipse's size without affecting the layout. See
the [box's documentation]($box.outset) for more details.

### body 

The content to place into the ellipse.

When this is omitted, the ellipse takes on a default size of at most
`{45pt}` by `{30pt}`.

## Returns

- content


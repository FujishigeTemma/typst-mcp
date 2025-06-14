# Circle

## `circle`

A circle with optional content.

# Example
```example
// Without content.
#circle(radius: 25pt)

// With content.
#circle[
  #set align(center + horizon)
  Automatically \
  sized to fit.
]
```

## Parameters

### radius 

The circle's radius. This is mutually exclusive with `width` and
`height`.

### width 

The circle's width. This is mutually exclusive with `radius` and
`height`.

In contrast to `radius`, this can be relative to the parent container's
width.

### height 

The circle's height. This is mutually exclusive with `radius` and
`width`.

In contrast to `radius`, this can be relative to the parent container's
height.

### fill 

How to fill the circle. See the [rectangle's documentation]($rect.fill)
for more details.

### stroke 

How to stroke the circle. See the
[rectangle's documentation]($rect.stroke) for more details.

### inset 

How much to pad the circle's content. See the
[box's documentation]($box.inset) for more details.

### outset 

How much to expand the circle's size without affecting the layout. See
the [box's documentation]($box.outset) for more details.

### body 

The content to place into the circle. The circle expands to fit this
content, keeping the 1-1 aspect ratio.

## Returns

- content


# Repeat

## `repeat`

Repeats content to the available space.

This can be useful when implementing a custom index, reference, or outline.

Space may be inserted between the instances of the body parameter, so be
sure to adjust the [`justify`]($repeat.justify) parameter accordingly.

Errors if there are no bounds on the available space, as it would create
infinite content.

# Example
```example
Sign on the dotted line:
#box(width: 1fr, repeat[.])

#set text(10pt)
#v(8pt, weak: true)
#align(right)[
  Berlin, the 22nd of December, 2022
]
```

## Parameters

### body *(required)*

The content to repeat.

### gap 

The gap between each instance of the body.

### justify 

Whether to increase the gap between instances to completely fill the
available space.

## Returns

- content


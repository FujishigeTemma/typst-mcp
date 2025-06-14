# Move

## `move`

Moves content without affecting layout.

The `move` function allows you to move content while the layout still 'sees'
it at the original positions. Containers will still be sized as if the
content was not moved.

# Example
```example
#rect(inset: 0pt, move(
  dx: 6pt, dy: 6pt,
  rect(
    inset: 8pt,
    fill: white,
    stroke: black,
    [Abra cadabra]
  )
))
```

## Parameters

### dx 

The horizontal displacement of the content.

### dy 

The vertical displacement of the content.

### body *(required)*

The content to move.

## Returns

- content


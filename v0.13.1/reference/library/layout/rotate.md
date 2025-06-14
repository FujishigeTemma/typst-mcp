# Rotate

## `rotate`

Rotates content without affecting layout.

Rotates an element by a given angle. The layout will act as if the element
was not rotated unless you specify `{reflow: true}`.

# Example
```example
#stack(
  dir: ltr,
  spacing: 1fr,
  ..range(16)
    .map(i => rotate(24deg * i)[X]),
)
```

## Parameters

### angle 

The amount of rotation.



### origin 

The origin of the rotation.

If, for instance, you wanted the bottom left corner of the rotated
element to stay aligned with the baseline, you would set it to `bottom +
left` instead.



### reflow 

Whether the rotation impacts the layout.

If set to `{false}`, the rotated content will retain the bounding box of
the original content. If set to `{true}`, the bounding box will take the
rotation of the content into account and adjust the layout accordingly.



### body *(required)*

The content to rotate.

## Returns

- content


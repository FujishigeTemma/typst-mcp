# Skew

## `skew`

Skews content.

Skews an element in horizontal and/or vertical direction. The layout will
act as if the element was not skewed unless you specify `{reflow: true}`.

# Example
```example
#skew(ax: -12deg)[
  This is some fake italic text.
]
```

## Parameters

### ax 

The horizontal skewing angle.



### ay 

The vertical skewing angle.



### origin 

The origin of the skew transformation.

The origin will stay fixed during the operation.



### reflow 

Whether the skew transformation impacts the layout.

If set to `{false}`, the skewed content will retain the bounding box of
the original content. If set to `{true}`, the bounding box will take the
transformation of the content into account and adjust the layout accordingly.



### body *(required)*

The content to skew.

## Returns

- content


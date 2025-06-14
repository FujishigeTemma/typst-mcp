# Scale

## `scale`

Scales content without affecting layout.

Lets you mirror content by specifying a negative scale on a single axis.

# Example
```example
#set align(center)
#scale(x: -100%)[This is mirrored.]
#scale(x: -100%, reflow: true)[This is mirrored.]
```

## Parameters

### factor 

The scaling factor for both axes, as a positional argument. This is just
an optional shorthand notation for setting `x` and `y` to the same
value.

### x 

The horizontal scaling factor.

The body will be mirrored horizontally if the parameter is negative.

### y 

The vertical scaling factor.

The body will be mirrored vertically if the parameter is negative.

### origin 

The origin of the transformation.



### reflow 

Whether the scaling impacts the layout.

If set to `{false}`, the scaled content will be allowed to overlap
other content. If set to `{true}`, it will compute the new size of
the scaled content and adjust the layout accordingly.



### body *(required)*

The content to scale.

## Returns

- content


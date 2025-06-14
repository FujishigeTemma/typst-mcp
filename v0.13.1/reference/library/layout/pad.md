# Padding

## `pad`

Adds spacing around content.

The spacing can be specified for each side individually, or for all sides at
once by specifying a positional argument.

# Example
```example
#set align(center)

#pad(x: 16pt, image("typing.jpg"))
_Typing speeds can be
 measured in words per minute._
```

## Parameters

### left 

The padding at the left side.

### top 

The padding at the top side.

### right 

The padding at the right side.

### bottom 

The padding at the bottom side.

### x 

A shorthand to set `left` and `right` to the same value.

### y 

A shorthand to set `top` and `bottom` to the same value.

### rest 

A shorthand to set all four sides to the same value.

### body *(required)*

The content to pad at the sides.

## Returns

- content


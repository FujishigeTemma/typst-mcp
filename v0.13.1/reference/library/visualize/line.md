# Line

## `line`

A line from one point to another.

# Example
```example
#set page(height: 100pt)

#line(length: 100%)
#line(end: (50%, 50%))
#line(
  length: 4cm,
  stroke: 2pt + maroon,
)
```

## Parameters

### start 

The start point of the line.

Must be an array of exactly two relative lengths.

### end 

The point where the line ends.

### length 

The line's length. This is only respected if `end` is `{none}`.

### angle 

The angle at which the line points away from the origin. This is only
respected if `end` is `{none}`.

### stroke 

How to [stroke] the line.



## Returns

- content


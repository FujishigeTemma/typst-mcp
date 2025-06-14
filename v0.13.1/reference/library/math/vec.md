# Vector

## `vec`

A column vector.

Content in the vector's elements can be aligned with the
[`align`]($math.vec.align) parameter, or the `&` symbol.

# Example
```example
$ vec(a, b, c) dot vec(1, 2, 3)
    = a + 2b + 3c $
```

## Parameters

### delim 

The delimiter to use.

Can be a single character specifying the left delimiter, in which case
the right delimiter is inferred. Otherwise, can be an array containing a
left and a right delimiter.



### align 

The horizontal alignment that each element should have.



### gap 

The gap between elements.



### children *(required)*

The elements of the vector.

## Returns

- content


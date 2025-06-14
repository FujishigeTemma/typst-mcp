# Cases

## `cases`

A case distinction.

Content across different branches can be aligned with the `&` symbol.

# Example
```example
$ f(x, y) := cases(
  1 "if" (x dot y)/2 <= 0,
  2 "if" x "is even",
  3 "if" x in NN,
  4 "else",
) $
```

## Parameters

### delim 

The delimiter to use.

Can be a single character specifying the left delimiter, in which case
the right delimiter is inferred. Otherwise, can be an array containing a
left and a right delimiter.



### reverse 

Whether the direction of cases should be reversed.



### gap 

The gap between branches.



### children *(required)*

The branches of the case distinction.

## Returns

- content


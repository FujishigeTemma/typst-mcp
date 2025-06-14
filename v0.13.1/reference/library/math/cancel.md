# Cancel

## `cancel`

Displays a diagonal line over a part of an equation.

This is commonly used to show the elimination of a term.

# Example
```example
>>> #set page(width: 140pt)
Here, we can simplify:
$ (a dot b dot cancel(x)) /
    cancel(x) $
```

## Parameters

### body *(required)*

The content over which the line should be placed.

### length 

The length of the line, relative to the length of the diagonal spanning
the whole element being "cancelled". A value of `{100%}` would then have
the line span precisely the element's diagonal.



### inverted 

Whether the cancel line should be inverted (flipped along the y-axis).
For the default angle setting, inverted means the cancel line
points to the top left instead of top right.



### cross 

Whether two opposing cancel lines should be drawn, forming a cross over
the element. Overrides `inverted`.



### angle 

How much to rotate the cancel line.

- If given an angle, the line is rotated by that angle clockwise with
  respect to the y-axis.
- If `{auto}`, the line assumes the default angle; that is, along the
  rising diagonal of the content box.
- If given a function `angle => angle`, the line is rotated, with
  respect to the y-axis, by the angle returned by that function. The
  function receives the default angle as its input.



### stroke 

How to [stroke]($stroke) the cancel line.



## Returns

- content


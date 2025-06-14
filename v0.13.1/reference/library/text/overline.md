# Overline

## `overline`

Adds a line over text.

# Example
```example
#overline[A line over text.]
```

## Parameters

### stroke 

How to [stroke] the line.

If set to `{auto}`, takes on the text's color and a thickness defined in
the current font.



### offset 

The position of the line relative to the baseline. Read from the font
tables if `{auto}`.



### extent 

The amount by which to extend the line beyond (or within if negative)
the content.



### evade 

Whether the line skips sections in which it would collide with the
glyphs.



### background 

Whether the line is placed behind the content it overlines.



### body *(required)*

The content to add a line over.

## Returns

- content


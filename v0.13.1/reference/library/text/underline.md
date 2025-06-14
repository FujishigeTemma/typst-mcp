# Underline

## `underline`

Underlines text.

# Example
```example
This is #underline[important].
```

## Parameters

### stroke 

How to [stroke] the line.

If set to `{auto}`, takes on the text's color and a thickness defined in
the current font.



### offset 

The position of the line relative to the baseline, read from the font
tables if `{auto}`.



### extent 

The amount by which to extend the line beyond (or within if negative)
the content.



### evade 

Whether the line skips sections in which it would collide with the
glyphs.



### background 

Whether the line is placed behind the content it underlines.



### body *(required)*

The content to underline.

## Returns

- content


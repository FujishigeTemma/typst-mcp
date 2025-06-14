# Strikethrough

## `strike`

Strikes through text.

# Example
```example
This is #strike[not] relevant.
```

## Parameters

### stroke 

How to [stroke] the line.

If set to `{auto}`, takes on the text's color and a thickness defined in
the current font.

_Note:_ Please don't use this for real redaction as you can still copy
paste the text.



### offset 

The position of the line relative to the baseline. Read from the font
tables if `{auto}`.

This is useful if you are unhappy with the offset your font provides.



### extent 

The amount by which to extend the line beyond (or within if negative)
the content.



### background 

Whether the line is placed behind the content.



### body *(required)*

The content to strike through.

## Returns

- content


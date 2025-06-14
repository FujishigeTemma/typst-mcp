# Superscript

## `super`

Renders text in superscript.

The text is rendered smaller and its baseline is raised.

# Example
```example
1#super[st] try!
```

## Parameters

### typographic 

Whether to prefer the dedicated superscript characters of the font.

If this is enabled, Typst first tries to transform the text to
superscript codepoints. If that fails, it falls back to rendering
raised and shrunk normal letters.



### baseline 

The baseline shift for synthetic superscripts. Does not apply if
`typographic` is true and the font has superscript codepoints for the
given `body`.

### size 

The font size for synthetic superscripts. Does not apply if
`typographic` is true and the font has superscript codepoints for the
given `body`.

### body *(required)*

The text to display in superscript.

## Returns

- content


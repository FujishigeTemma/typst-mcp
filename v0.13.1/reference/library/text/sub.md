# Subscript

## `sub`

Renders text in subscript.

The text is rendered smaller and its baseline is lowered.

# Example
```example
Revenue#sub[yearly]
```

## Parameters

### typographic 

Whether to prefer the dedicated subscript characters of the font.

If this is enabled, Typst first tries to transform the text to subscript
codepoints. If that fails, it falls back to rendering lowered and shrunk
normal letters.



### baseline 

The baseline shift for synthetic subscripts. Does not apply if
`typographic` is true and the font has subscript codepoints for the
given `body`.

### size 

The font size for synthetic subscripts. Does not apply if
`typographic` is true and the font has subscript codepoints for the
given `body`.

### body *(required)*

The text to display in subscript.

## Returns

- content


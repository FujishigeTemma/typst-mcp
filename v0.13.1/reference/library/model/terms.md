# Term List

## `terms`

A list of terms and their descriptions.

Displays a sequence of terms and their descriptions vertically. When the
descriptions span over multiple lines, they use hanging indent to
communicate the visual hierarchy.

# Example
```example
/ Ligature: A merged glyph.
/ Kerning: A spacing adjustment
  between two adjacent letters.
```

# Syntax
This function also has dedicated syntax: Starting a line with a slash,
followed by a term, a colon and a description creates a term list item.

## Parameters

### tight 

Defines the default [spacing]($terms.spacing) of the term list. If it is
`{false}`, the items are spaced apart with
[paragraph spacing]($par.spacing). If it is `{true}`, they use
[paragraph leading]($par.leading) instead. This makes the list more
compact, which can look better if the items are short.

In markup mode, the value of this parameter is determined based on
whether items are separated with a blank line. If items directly follow
each other, this is set to `{true}`; if items are separated by a blank
line, this is set to `{false}`. The markup-defined tightness cannot be
overridden with set rules.



### separator 

The separator between the item and the description.

If you want to just separate them with a certain amount of space, use
`{h(2cm, weak: true)}` as the separator and replace `{2cm}` with your
desired amount of space.



### indent 

The indentation of each item.

### hanging-indent 

The hanging indent of the description.

This is in addition to the whole item's `indent`.



### spacing 

The spacing between the items of the term list.

If set to `{auto}`, uses paragraph [`leading`]($par.leading) for tight
term lists and paragraph [`spacing`]($par.spacing) for wide
(non-tight) term lists.

### children *(required)*

The term list's children.

When using the term list syntax, adjacent items are automatically
collected into term lists, even through constructs like for loops.



## Returns

- content


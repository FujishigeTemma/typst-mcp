# Bullet List

## `list`

A bullet list.

Displays a sequence of items vertically, with each item introduced by a
marker.

# Example
```example
Normal list.
- Text
- Math
- Layout
- ...

Multiple lines.
- This list item spans multiple
  lines because it is indented.

Function call.
#list(
  [Foundations],
  [Calculate],
  [Construct],
  [Data Loading],
)
```

# Syntax
This functions also has dedicated syntax: Start a line with a hyphen,
followed by a space to create a list item. A list item can contain multiple
paragraphs and other block-level content. All content that is indented
more than an item's marker becomes part of that item.

## Parameters

### tight 

Defines the default [spacing]($list.spacing) of the list. If it is
`{false}`, the items are spaced apart with
[paragraph spacing]($par.spacing). If it is `{true}`, they use
[paragraph leading]($par.leading) instead. This makes the list more
compact, which can look better if the items are short.

In markup mode, the value of this parameter is determined based on
whether items are separated with a blank line. If items directly follow
each other, this is set to `{true}`; if items are separated by a blank
line, this is set to `{false}`. The markup-defined tightness cannot be
overridden with set rules.



### marker 

The marker which introduces each item.

Instead of plain content, you can also pass an array with multiple
markers that should be used for nested lists. If the list nesting depth
exceeds the number of markers, the markers are cycled. For total
control, you may pass a function that maps the list's nesting depth
(starting from `{0}`) to a desired marker.



### indent 

The indent of each item.

### body-indent 

The spacing between the marker and the body of each item.

### spacing 

The spacing between the items of the list.

If set to `{auto}`, uses paragraph [`leading`]($par.leading) for tight
lists and paragraph [`spacing`]($par.spacing) for wide (non-tight)
lists.

### children *(required)*

The bullet list's children.

When using the list syntax, adjacent items are automatically collected
into lists, even through constructs like for loops.



## Returns

- content


# Box

## `box`

An inline-level container that sizes content.

All elements except inline math, text, and boxes are block-level and cannot
occur inside of a [paragraph]($par). The box function can be used to
integrate such elements into a paragraph. Boxes take the size of their
contents by default but can also be sized explicitly.

# Example
```example
Refer to the docs
#box(
  height: 9pt,
  image("docs.svg")
)
for more information.
```

## Parameters

### width 

The width of the box.

Boxes can have [fractional]($fraction) widths, as the example below
demonstrates.

_Note:_ Currently, only boxes and only their widths might be fractionally
sized within paragraphs. Support for fractionally sized images, shapes,
and more might be added in the future.



### height 

The height of the box.

### baseline 

An amount to shift the box's baseline by.



### fill 

The box's background color. See the
[rectangle's documentation]($rect.fill) for more details.

### stroke 

The box's border color. See the
[rectangle's documentation]($rect.stroke) for more details.

### radius 

How much to round the box's corners. See the
[rectangle's documentation]($rect.radius) for more details.

### inset 

How much to pad the box's content.

_Note:_ When the box contains text, its exact size depends on the
current [text edges]($text.top-edge).



### outset 

How much to expand the box's size without affecting the layout.

This is useful to prevent padding from affecting line layout. For a
generalized version of the example below, see the documentation for the
[raw text's block parameter]($raw.block).



### clip 

Whether to clip the content inside the box.

Clipping is useful when the box's content is larger than the box itself,
as any content that exceeds the box's bounds will be hidden.



### body 

The contents of the box.

## Returns

- content


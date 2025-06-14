# Tiling

A repeating tiling fill.

Typst supports the most common type of tilings, where a pattern is repeated
in a grid-like fashion, covering the entire area of an element that is
filled or stroked. The pattern is defined by a tile size and a body defining
the content of each cell. You can also add horizontal or vertical spacing
between the cells of the tiling.

# Examples

```example
#let pat = tiling(size: (30pt, 30pt))[
  #place(line(start: (0%, 0%), end: (100%, 100%)))
  #place(line(start: (0%, 100%), end: (100%, 0%)))
]

#rect(fill: pat, width: 100%, height: 60pt, stroke: 1pt)
```

Tilings are also supported on text, but only when setting the
[relativeness]($tiling.relative) to either `{auto}` (the default value) or
`{"parent"}`. To create word-by-word or glyph-by-glyph tilings, you can
wrap the words or characters of your text in [boxes]($box) manually or
through a [show rule]($styling/#show-rules).

```example
#let pat = tiling(
  size: (30pt, 30pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
      .conic(..color.map.rainbow),
  )
)

#set text(fill: pat)
#lorem(10)
```

You can also space the elements further or closer apart using the
[`spacing`]($tiling.spacing) feature of the tiling. If the spacing
is lower than the size of the tiling, the tiling will overlap.
If it is higher, the tiling will have gaps of the same color as the
background of the tiling.

```example
#let pat = tiling(
  size: (30pt, 30pt),
  spacing: (10pt, 10pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
     .conic(..color.map.rainbow),
  ),
)

#rect(
  width: 100%,
  height: 60pt,
  fill: pat,
)
```

# Relativeness
The location of the starting point of the tiling is dependent on the
dimensions of a container. This container can either be the shape that it is
being painted on, or the closest surrounding container. This is controlled
by the `relative` argument of a tiling constructor. By default, tilings
are relative to the shape they are being painted on, unless the tiling is
applied on text, in which case they are relative to the closest ancestor
container.

Typst determines the ancestor container as follows:
- For shapes that are placed at the root/top level of the document, the
  closest ancestor is the page itself.
- For other shapes, the ancestor is the innermost [`block`] or [`box`] that
  contains the shape. This includes the boxes and blocks that are implicitly
  created by show rules and elements. For example, a [`rotate`] will not
  affect the parent of a gradient, but a [`grid`] will.

# Compatibility
This type used to be called `pattern`. The name remains as an alias, but is
deprecated since Typst 0.13.

## Constructor

### `tiling`

Construct a new tiling.




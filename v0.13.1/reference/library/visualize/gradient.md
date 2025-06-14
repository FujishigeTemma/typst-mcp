# Gradient

A color gradient.

Typst supports linear gradients through the
[`gradient.linear` function]($gradient.linear), radial gradients through
the [`gradient.radial` function]($gradient.radial), and conic gradients
through the [`gradient.conic` function]($gradient.conic).

A gradient can be used for the following purposes:
- As a fill to paint the interior of a shape:
  `{rect(fill: gradient.linear(..))}`
- As a stroke to paint the outline of a shape:
  `{rect(stroke: 1pt + gradient.linear(..))}`
- As the fill of text:
  `{set text(fill: gradient.linear(..))}`
- As a color map you can [sample]($gradient.sample) from:
  `{gradient.linear(..).sample(50%)}`

# Examples
```example
>>> #set square(size: 50pt)
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(..color.map.rainbow)),
  square(fill: gradient.radial(..color.map.rainbow)),
  square(fill: gradient.conic(..color.map.rainbow)),
)
```

Gradients are also supported on text, but only when setting the
[relativeness]($gradient.relative) to either `{auto}` (the default value) or
`{"parent"}`. To create word-by-word or glyph-by-glyph gradients, you can
wrap the words or characters of your text in [boxes]($box) manually or
through a [show rule]($styling/#show-rules).

```example
>>> #set page(width: auto, height: auto, margin: 12pt)
>>> #set text(size: 12pt)
#set text(fill: gradient.linear(red, blue))
#let rainbow(content) = {
  set text(fill: gradient.linear(..color.map.rainbow))
  box(content)
}

This is a gradient on text, but with a #rainbow[twist]!
```

# Stops
A gradient is composed of a series of stops. Each of these stops has a color
and an offset. The offset is a [ratio]($ratio) between `{0%}` and `{100%}` or
an angle between `{0deg}` and `{360deg}`. The offset is a relative position
that determines how far along the gradient the stop is located. The stop's
color is the color of the gradient at that position. You can choose to omit
the offsets when defining a gradient. In this case, Typst will space all
stops evenly.

Typst predefines color maps that you can use as stops. See the
[`color`]($color/#predefined-color-maps) documentation for more details.

# Relativeness
The location of the `{0%}` and `{100%}` stops depends on the dimensions
of a container. This container can either be the shape that it is being
painted on, or the closest surrounding container. This is controlled by the
`relative` argument of a gradient constructor. By default, gradients are
relative to the shape they are being painted on, unless the gradient is
applied on text, in which case they are relative to the closest ancestor
container.

Typst determines the ancestor container as follows:
- For shapes that are placed at the root/top level of the document, the
  closest ancestor is the page itself.
- For other shapes, the ancestor is the innermost [`block`] or [`box`] that
  contains the shape. This includes the boxes and blocks that are implicitly
  created by show rules and elements. For example, a [`rotate`] will not
  affect the parent of a gradient, but a [`grid`] will.

# Color spaces and interpolation
Gradients can be interpolated in any color space. By default, gradients are
interpolated in the [Oklab]($color.oklab) color space, which is a
[perceptually uniform](https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/index.html)
color space. This means that the gradient will be perceived as having a
smooth progression of colors. This is particularly useful for data
visualization.

However, you can choose to interpolate the gradient in any supported color
space you want, but beware that some color spaces are not suitable for
perceptually interpolating between colors. Consult the table below when
choosing an interpolation space.

|           Color space           | Perceptually uniform? |
| ------------------------------- |-----------------------|
| [Oklab]($color.oklab)           | *Yes*                 |
| [Oklch]($color.oklch)           | *Yes*                 |
| [sRGB]($color.rgb)              | *No*                  |
| [linear-RGB]($color.linear-rgb) | *Yes*                 |
| [CMYK]($color.cmyk)             | *No*                  |
| [Grayscale]($color.luma)        | *Yes*                 |
| [HSL]($color.hsl)               | *No*                  |
| [HSV]($color.hsv)               | *No*                  |

```preview
>>> #set text(fill: white, font: "IBM Plex Sans", 8pt)
>>> #set block(spacing: 0pt)
#let spaces = (
  ("Oklab", color.oklab),
  ("Oklch", color.oklch),
  ("sRGB", color.rgb),
  ("linear-RGB", color.linear-rgb),
  ("CMYK", color.cmyk),
  ("Grayscale", color.luma),
  ("HSL", color.hsl),
  ("HSV", color.hsv),
)

#for (name, space) in spaces {
  block(
    width: 100%,
    inset: 4pt,
    fill: gradient.linear(
      red,
      blue,
      space: space,
    ),
    strong(upper(name)),
  )
}
```

# Direction
Some gradients are sensitive to direction. For example, a linear gradient
has an angle that determines its direction. Typst uses a clockwise angle,
with 0° being from left to right, 90° from top to bottom, 180° from right to
left, and 270° from bottom to top.

```example
>>> #set square(size: 50pt)
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(red, blue, angle: 0deg)),
  square(fill: gradient.linear(red, blue, angle: 90deg)),
  square(fill: gradient.linear(red, blue, angle: 180deg)),
  square(fill: gradient.linear(red, blue, angle: 270deg)),
)
```

# Note on file sizes

Gradients can be quite large, especially if they have many stops. This is
because gradients are stored as a list of colors and offsets, which can
take up a lot of space. If you are concerned about file sizes, you should
consider the following:
- SVG gradients are currently inefficiently encoded. This will be improved
  in the future.
- PDF gradients in the [`color.oklab`]($color.oklab), [`color.hsv`]($color.hsv),
  [`color.hsl`]($color.hsl), and [`color.oklch`]($color.oklch) color spaces
  are stored as a list of [`color.rgb`]($color.rgb) colors with extra stops
  in between. This avoids needing to encode these color spaces in your PDF
  file, but it does add extra stops to your gradient, which can increase
  the file size.


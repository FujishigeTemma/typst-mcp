# Color

A color in a specific color space.

Typst supports:
- sRGB through the [`rgb` function]($color.rgb)
- Device CMYK through [`cmyk` function]($color.cmyk)
- D65 Gray through the [`luma` function]($color.luma)
- Oklab through the [`oklab` function]($color.oklab)
- Oklch through the [`oklch` function]($color.oklch)
- Linear RGB through the [`color.linear-rgb` function]($color.linear-rgb)
- HSL through the [`color.hsl` function]($color.hsl)
- HSV through the [`color.hsv` function]($color.hsv)


# Example

```example
#rect(fill: aqua)
```

# Predefined colors
Typst defines the following built-in colors:

| Color     | Definition         |
|-----------|:-------------------|
| `black`   | `{luma(0)}`        |
| `gray`    | `{luma(170)}`      |
| `silver`  | `{luma(221)}`      |
| `white`   | `{luma(255)}`      |
| `navy`    | `{rgb("#001f3f")}` |
| `blue`    | `{rgb("#0074d9")}` |
| `aqua`    | `{rgb("#7fdbff")}` |
| `teal`    | `{rgb("#39cccc")}` |
| `eastern` | `{rgb("#239dad")}` |
| `purple`  | `{rgb("#b10dc9")}` |
| `fuchsia` | `{rgb("#f012be")}` |
| `maroon`  | `{rgb("#85144b")}` |
| `red`     | `{rgb("#ff4136")}` |
| `orange`  | `{rgb("#ff851b")}` |
| `yellow`  | `{rgb("#ffdc00")}` |
| `olive`   | `{rgb("#3d9970")}` |
| `green`   | `{rgb("#2ecc40")}` |
| `lime`    | `{rgb("#01ff70")}` |

The predefined colors and the most important color constructors are
available globally and also in the color type's scope, so you can write
either `color.red` or just `red`.

```preview
#let colors = (
  "black", "gray", "silver", "white",
  "navy", "blue", "aqua", "teal",
  "eastern", "purple", "fuchsia",
  "maroon", "red", "orange", "yellow",
  "olive", "green", "lime",
)

#set text(font: "PT Sans")
#set page(width: auto)
#grid(
  columns: 9,
  gutter: 10pt,
  ..colors.map(name => {
      let col = eval(name)
      let luminance = luma(col).components().first()
      set text(fill: white) if luminance < 50%
      set square(stroke: black) if col == white
      set align(center + horizon)
      square(size: 50pt,  fill: col, name)
  })
)
```

# Predefined color maps
Typst also includes a number of preset color maps that can be used for
[gradients]($gradient/#stops). These are simply arrays of colors defined in
the module `color.map`.

```example
#circle(fill: gradient.linear(..color.map.crest))
```

| Map        | Details                                                     |
|------------|:------------------------------------------------------------|
| `turbo`    | A perceptually uniform rainbow-like color map. Read [this blog post](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html) for more details. |
| `cividis`  | A blue to gray to yellow color map. See [this blog post](https://bids.github.io/colormap/) for more details. |
| `rainbow`  | Cycles through the full color spectrum. This color map is best used by setting the interpolation color space to [HSL]($color.hsl). The rainbow gradient is **not suitable** for data visualization because it is not perceptually uniform, so the differences between values become unclear to your readers. It should only be used for decorative purposes. |
| `spectral` | Red to yellow to blue color map.                            |
| `viridis`  | A purple to teal to yellow color map.                       |
| `inferno`  | A black to red to yellow color map.                         |
| `magma`    | A black to purple to yellow color map.                      |
| `plasma`   | A purple to pink to yellow color map.                       |
| `rocket`   | A black to red to white color map.                          |
| `mako`     | A black to teal to white color map.                         |
| `vlag`     | A light blue to white to red color map.                     |
| `icefire`  | A light teal to black to orange color map.                  |
| `flare`    | A orange to purple color map that is perceptually uniform.  |
| `crest`    | A light green to blue color map.                            |

Some popular presets are not included because they are not available under a
free licence. Others, like
[Jet](https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/),
are not included because they are not color blind friendly. Feel free to use
or create a package with other presets that are useful to you!

```preview
#set page(width: auto, height: auto)
#set text(font: "PT Sans", size: 8pt)

#let maps = (
  "turbo", "cividis", "rainbow", "spectral",
  "viridis", "inferno", "magma", "plasma",
  "rocket", "mako", "vlag", "icefire",
  "flare", "crest",
)

#stack(dir: ltr, spacing: 3pt, ..maps.map((name) => {
  let map = eval("color.map." + name)
  stack(
    dir: ttb,
    block(
      width: 15pt,
      height: 100pt,
      fill: gradient.linear(..map, angle: 90deg),
    ),
    block(
      width: 15pt,
      height: 32pt,
      move(dy: 8pt, rotate(90deg, name)),
    ),
  )
}))
```


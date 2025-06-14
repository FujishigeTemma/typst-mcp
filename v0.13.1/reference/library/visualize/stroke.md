# Stroke

Defines how to draw a line.

A stroke has a _paint_ (a solid color or gradient), a _thickness,_ a line
_cap,_ a line _join,_ a _miter limit,_ and a _dash_ pattern. All of these
values are optional and have sensible defaults.

# Example
```example
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: 2pt + gradient.linear(..color.map.rainbow)),
)
```

# Simple strokes
You can create a simple solid stroke from a color, a thickness, or a
combination of the two. Specifically, wherever a stroke is expected you can
pass any of the following values:

- A length specifying the stroke's thickness. The color is inherited,
  defaulting to black.
- A color to use for the stroke. The thickness is inherited, defaulting to
  `{1pt}`.
- A stroke combined from color and thickness using the `+` operator as in
  `{2pt + red}`.

For full control, you can also provide a [dictionary] or a `{stroke}` object
to any function that expects a stroke. The dictionary's keys may include any
of the parameters for the constructor function, shown below.

# Fields
On a stroke object, you can access any of the fields listed in the
constructor function. For example, `{(2pt + blue).thickness}` is `{2pt}`.
Meanwhile, `{stroke(red).cap}` is `{auto}` because it's unspecified. Fields
set to `{auto}` are inherited.

## Constructor

### `stroke`

Converts a value to a stroke or constructs a stroke with the given
parameters.

Note that in most cases you do not need to convert values to strokes in
order to use them, as they will be converted automatically. However,
this constructor can be useful to ensure a value has all the fields of a
stroke.




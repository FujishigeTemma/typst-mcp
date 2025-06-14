# Grid

## `grid`

Arranges content in a grid.

The grid element allows you to arrange content in a grid. You can define the
number of rows and columns, as well as the size of the gutters between them.
There are multiple sizing modes for columns and rows that can be used to
create complex layouts.

While the grid and table elements work very similarly, they are intended for
different use cases and carry different semantics. The grid element is
intended for presentational and layout purposes, while the
[`{table}`]($table) element is intended for, in broad terms, presenting
multiple related data points. In the future, Typst will annotate its output
such that screenreaders will announce content in `table` as tabular while a
grid's content will be announced no different than multiple content blocks
in the document flow. Set and show rules on one of these elements do not
affect the other.

A grid's sizing is determined by the track sizes specified in the arguments.
Because each of the sizing parameters accepts the same values, we will
explain them just once, here. Each sizing argument accepts an array of
individual track sizes. A track size is either:

- `{auto}`: The track will be sized to fit its contents. It will be at most
  as large as the remaining space. If there is more than one `{auto}` track
  width, and together they claim more than the available space, the `{auto}`
  tracks will fairly distribute the available space among themselves.

- A fixed or relative length (e.g. `{10pt}` or `{20% - 1cm}`): The track
  will be exactly of this size.

- A fractional length (e.g. `{1fr}`): Once all other tracks have been sized,
  the remaining space will be divided among the fractional tracks according
  to their fractions. For example, if there are two fractional tracks, each
  with a fraction of `{1fr}`, they will each take up half of the remaining
  space.

To specify a single track, the array can be omitted in favor of a single
value. To specify multiple `{auto}` tracks, enter the number of tracks
instead of an array. For example, `columns:` `{3}` is equivalent to
`columns:` `{(auto, auto, auto)}`.

# Examples
The example below demonstrates the different track sizing options. It also
shows how you can use [`grid.cell`]($grid.cell) to make an individual cell
span two grid tracks.

```example
// We use `rect` to emphasize the
// area of cells.
#set rect(
  inset: 8pt,
  fill: rgb("e4e5ea"),
  width: 100%,
)

#grid(
  columns: (60pt, 1fr, 2fr),
  rows: (auto, 60pt),
  gutter: 3pt,
  rect[Fixed width, auto height],
  rect[1/3 of the remains],
  rect[2/3 of the remains],
  rect(height: 100%)[Fixed height],
  grid.cell(
    colspan: 2,
    image("tiger.jpg", width: 100%),
  ),
)
```

You can also [spread]($arguments/#spreading) an array of strings or content
into a grid to populate its cells.

```example
#grid(
  columns: 5,
  gutter: 5pt,
  ..range(25).map(str)
)
```

# Styling the grid
The grid's appearance can be customized through different parameters. These
are the most important ones:

- [`fill`]($grid.fill) to give all cells a background
- [`align`]($grid.align) to change how cells are aligned
- [`inset`]($grid.inset) to optionally add internal padding to each cell
- [`stroke`]($grid.stroke) to optionally enable grid lines with a certain
  stroke

If you need to override one of the above options for a single cell, you can
use the [`grid.cell`]($grid.cell) element. Likewise, you can override
individual grid lines with the [`grid.hline`]($grid.hline) and
[`grid.vline`]($grid.vline) elements.

Alternatively, if you need the appearance options to depend on a cell's
position (column and row), you may specify a function to `fill` or `align`
of the form `(column, row) => value`. You may also use a show rule on
[`grid.cell`]($grid.cell) - see that element's examples or the examples
below for more information.

Locating most of your styling in set and show rules is recommended, as it
keeps the grid's or table's actual usages clean and easy to read. It also
allows you to easily change the grid's appearance in one place.

## Stroke styling precedence
There are three ways to set the stroke of a grid cell: through
[`{grid.cell}`'s `stroke` field]($grid.cell.stroke), by using
[`{grid.hline}`]($grid.hline) and [`{grid.vline}`]($grid.vline), or by
setting the [`{grid}`'s `stroke` field]($grid.stroke). When multiple of
these settings are present and conflict, the `hline` and `vline` settings
take the highest precedence, followed by the `cell` settings, and finally
the `grid` settings.

Furthermore, strokes of a repeated grid header or footer will take
precedence over regular cell strokes.

## Parameters

### columns 

The column sizes.

Either specify a track size array or provide an integer to create a grid
with that many `{auto}`-sized columns. Note that opposed to rows and
gutters, providing a single track size will only ever create a single
column.

### rows 

The row sizes.

If there are more cells than fit the defined rows, the last row is
repeated until there are no more cells.

### gutter 

The gaps between rows and columns.

If there are more gutters than defined sizes, the last gutter is
repeated.

This is a shorthand to set `column-gutter` and `row-gutter` to the same
value.

### column-gutter 

The gaps between columns.

### row-gutter 

The gaps between rows.

### fill 

How to fill the cells.

This can be a color or a function that returns a color. The function
receives the cells' column and row indices, starting from zero. This can
be used to implement striped grids.



### align 

How to align the cells' content.

This can either be a single alignment, an array of alignments
(corresponding to each column) or a function that returns an alignment.
The function receives the cells' column and row indices, starting from
zero. If set to `{auto}`, the outer alignment is used.

You can find an example for this argument at the
[`table.align`]($table.align) parameter.

### stroke 

How to [stroke]($stroke) the cells.

Grids have no strokes by default, which can be changed by setting this
option to the desired stroke.

If it is necessary to place lines which can cross spacing between cells
produced by the `gutter` option, or to override the stroke between
multiple specific cells, consider specifying one or more of
[`grid.hline`]($grid.hline) and [`grid.vline`]($grid.vline) alongside
your grid cells.



### inset 

How much to pad the cells' content.

You can find an example for this argument at the
[`table.inset`]($table.inset) parameter.

### children *(required)*

The contents of the grid cells, plus any extra grid lines specified
with the [`grid.hline`]($grid.hline) and [`grid.vline`]($grid.vline)
elements.

The cells are populated in row-major order.

## Returns

- content


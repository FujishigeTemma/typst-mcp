# Table

## `table`

A table of items.

Tables are used to arrange content in cells. Cells can contain arbitrary
content, including multiple paragraphs and are specified in row-major order.
For a hands-on explanation of all the ways you can use and customize tables
in Typst, check out the [table guide]($guides/table-guide).

Because tables are just grids with different defaults for some cell
properties (notably `stroke` and `inset`), refer to the [grid
documentation]($grid) for more information on how to size the table tracks
and specify the cell appearance properties.

If you are unsure whether you should be using a table or a grid, consider
whether the content you are arranging semantically belongs together as a set
of related data points or similar or whether you are just want to enhance
your presentation by arranging unrelated content in a grid. In the former
case, a table is the right choice, while in the latter case, a grid is more
appropriate. Furthermore, Typst will annotate its output in the future such
that screenreaders will announce content in `table` as tabular while a
grid's content will be announced no different than multiple content blocks
in the document flow.

Note that, to override a particular cell's properties or apply show rules on
table cells, you can use the [`table.cell`]($table.cell) element. See its
documentation for more information.

Although the `table` and the `grid` share most properties, set and show
rules on one of them do not affect the other.

To give a table a caption and make it [referenceable]($ref), put it into a
[figure].

# Example

The example below demonstrates some of the most common table options.
```example
#table(
  columns: (1fr, auto, auto),
  inset: 10pt,
  align: horizon,
  table.header(
    [], [*Volume*], [*Parameters*],
  ),
  image("cylinder.svg"),
  $ pi h (D^2 - d^2) / 4 $,
  [
    $h$: height \
    $D$: outer radius \
    $d$: inner radius
  ],
  image("tetrahedron.svg"),
  $ sqrt(2) / 12 a^3 $,
  [$a$: edge length]
)
```

Much like with grids, you can use [`table.cell`]($table.cell) to customize
the appearance and the position of each cell.

```example
>>> #set page(width: auto)
>>> #set text(font: "IBM Plex Sans")
>>> #let gray = rgb("#565565")
>>>
#set table(
  stroke: none,
  gutter: 0.2em,
  fill: (x, y) =>
    if x == 0 or y == 0 { gray },
  inset: (right: 1.5em),
)

#show table.cell: it => {
  if it.x == 0 or it.y == 0 {
    set text(white)
    strong(it)
  } else if it.body == [] {
    // Replace empty cells with 'N/A'
    pad(..it.inset)[_N/A_]
  } else {
    it
  }
}

#let a = table.cell(
  fill: green.lighten(60%),
)[A]
#let b = table.cell(
  fill: aqua.lighten(60%),
)[B]

#table(
  columns: 4,
  [], [Exam 1], [Exam 2], [Exam 3],

  [John], [], a, [],
  [Mary], [], a, a,
  [Robert], b, a, b,
)
```

## Parameters

### columns 

The column sizes. See the [grid documentation]($grid) for more
information on track sizing.

### rows 

The row sizes. See the [grid documentation]($grid) for more information
on track sizing.

### gutter 

The gaps between rows and columns. This is a shorthand for setting
`column-gutter` and `row-gutter` to the same value. See the [grid
documentation]($grid) for more information on gutters.

### column-gutter 

The gaps between columns. Takes precedence over `gutter`. See the
[grid documentation]($grid) for more information on gutters.

### row-gutter 

The gaps between rows. Takes precedence over `gutter`. See the
[grid documentation]($grid) for more information on gutters.

### fill 

How to fill the cells.

This can be a color or a function that returns a color. The function
receives the cells' column and row indices, starting from zero. This can
be used to implement striped tables.



### align 

How to align the cells' content.

This can either be a single alignment, an array of alignments
(corresponding to each column) or a function that returns an alignment.
The function receives the cells' column and row indices, starting from
zero. If set to `{auto}`, the outer alignment is used.



### stroke 

How to [stroke] the cells.

Strokes can be disabled by setting this to `{none}`.

If it is necessary to place lines which can cross spacing between cells
produced by the `gutter` option, or to override the stroke between
multiple specific cells, consider specifying one or more of
[`table.hline`]($table.hline) and [`table.vline`]($table.vline)
alongside your table cells.

See the [grid documentation]($grid.stroke) for more information on
strokes.

### inset 

How much to pad the cells' content.



### children *(required)*

The contents of the table cells, plus any extra table lines specified
with the [`table.hline`]($table.hline) and
[`table.vline`]($table.vline) elements.

## Returns

- content


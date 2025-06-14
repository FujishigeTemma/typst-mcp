# Columns

## `columns`

Separates a region into multiple equally sized columns.

The `column` function lets you separate the interior of any container into
multiple columns. It will currently not balance the height of the columns.
Instead, the columns will take up the height of their container or the
remaining height on the page. Support for balanced columns is planned for
the future.

# Page-level columns { #page-level }
If you need to insert columns across your whole document, use the `{page}`
function's [`columns` parameter]($page.columns) instead. This will create
the columns directly at the page-level rather than wrapping all of your
content in a layout container. As a result, things like
[pagebreaks]($pagebreak), [footnotes]($footnote), and [line
numbers]($par.line) will continue to work as expected. For more information,
also read the [relevant part of the page setup
guide]($guides/page-setup-guide/#columns).

# Breaking out of columns { #breaking-out }
To temporarily break out of columns (e.g. for a paper's title), use
parent-scoped floating placement:

```example:single
#set page(columns: 2, height: 150pt)

#place(
  top + center,
  scope: "parent",
  float: true,
  text(1.4em, weight: "bold")[
    My document
  ],
)

#lorem(40)
```

## Parameters

### count 

The number of columns.

### gutter 

The size of the gutter space between each column.

### body *(required)*

The content that should be layouted into the columns.

## Returns

- content


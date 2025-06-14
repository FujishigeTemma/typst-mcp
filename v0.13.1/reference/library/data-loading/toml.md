# TOML

## `toml`

Reads structured data from a TOML file.

The file must contain a valid TOML table. TOML tables will be converted into
Typst dictionaries, and TOML arrays will be converted into Typst arrays.
Strings, booleans and datetimes will be converted into the Typst equivalents
and numbers will be converted to floats or integers depending on whether
they are whole numbers.

The TOML file in the example consists of a table with the keys `title`,
`version`, and `authors`.

# Example
```example
#let details = toml("details.toml")

Title: #details.title \
Version: #details.version \
Authors: #(details.authors
  .join(", ", last: " and "))
```

## Parameters

### source *(required)*

A [path]($syntax/#paths) to a TOML file or raw TOML bytes.

## Returns

- any


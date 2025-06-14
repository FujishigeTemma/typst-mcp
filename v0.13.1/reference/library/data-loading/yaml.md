# YAML

## `yaml`

Reads structured data from a YAML file.

The file must contain a valid YAML object or array. YAML mappings will be
converted into Typst dictionaries, and YAML sequences will be converted into
Typst arrays. Strings and booleans will be converted into the Typst
equivalents, null-values (`null`, `~` or empty ``) will be converted into
`{none}`, and numbers will be converted to floats or integers depending on
whether they are whole numbers. Custom YAML tags are ignored, though the
loaded value will still be present.

Be aware that integers larger than 2<sup>63</sup>-1 will be converted to
floating point numbers, which may give an approximative value.

The YAML files in the example contain objects with authors as keys,
each with a sequence of their own submapping with the keys
"title" and "published"

# Example
```example
#let bookshelf(contents) = {
  for (author, works) in contents {
    author
    for work in works [
      - #work.title (#work.published)
    ]
  }
}

#bookshelf(
  yaml("scifi-authors.yaml")
)
```

## Parameters

### source *(required)*

A [path]($syntax/#paths) to a YAML file or raw YAML bytes.

## Returns

- any


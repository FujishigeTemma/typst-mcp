# CBOR

## `cbor`

Reads structured data from a CBOR file.

The file must contain a valid CBOR serialization. Mappings will be
converted into Typst dictionaries, and sequences will be converted into
Typst arrays. Strings and booleans will be converted into the Typst
equivalents, null-values (`null`, `~` or empty ``) will be converted into
`{none}`, and numbers will be converted to floats or integers depending on
whether they are whole numbers.

Be aware that integers larger than 2<sup>63</sup>-1 will be converted to
floating point numbers, which may result in an approximative value.

## Parameters

### source *(required)*

A [path]($syntax/#paths) to a CBOR file or raw CBOR bytes.

## Returns

- any


# Bytes

A sequence of bytes.

This is conceptually similar to an array of [integers]($int) between `{0}`
and `{255}`, but represented much more efficiently. You can iterate over it
using a [for loop]($scripting/#loops).

You can convert
- a [string]($str) or an [array] of integers to bytes with the [`bytes`]
  constructor
- bytes to a string with the [`str`] constructor, with UTF-8 encoding
- bytes to an array of integers with the [`array`] constructor

When [reading]($read) data from a file, you can decide whether to load it
as a string or as raw bytes.

```example
#bytes((123, 160, 22, 0)) \
#bytes("Hello 😃")

#let data = read(
  "rhino.png",
  encoding: none,
)

// Magic bytes.
#array(data.slice(0, 4)) \
#str(data.slice(1, 4))
```

## Constructor

### `bytes`

Converts a value to bytes.

- Strings are encoded in UTF-8.
- Arrays of integers between `{0}` and `{255}` are converted directly. The
  dedicated byte representation is much more efficient than the array
  representation and thus typically used for large byte buffers (e.g. image
  data).




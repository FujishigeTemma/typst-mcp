# String

A sequence of Unicode codepoints.

You can iterate over the grapheme clusters of the string using a [for
loop]($scripting/#loops). Grapheme clusters are basically characters but
keep together things that belong together, e.g. multiple codepoints that
together form a flag emoji. Strings can be added with the `+` operator,
[joined together]($scripting/#blocks) and multiplied with integers.

Typst provides utility methods for string manipulation. Many of these
methods (e.g., `split`, `trim` and `replace`) operate on _patterns:_ A
pattern can be either a string or a [regular expression]($regex). This makes
the methods quite versatile.

All lengths and indices are expressed in terms of UTF-8 bytes. Indices are
zero-based and negative indices wrap around to the end of the string.

You can convert a value to a string with this type's constructor.

# Example
```example
#"hello world!" \
#"\"hello\n  world\"!" \
#"1 2 3".split() \
#"1,2;3".split(regex("[,;]")) \
#(regex("\d+") in "ten euros") \
#(regex("\d+") in "10 euros")
```

# Escape sequences { #escapes }
Just like in markup, you can escape a few symbols in strings:
- `[\\]` for a backslash
- `[\"]` for a quote
- `[\n]` for a newline
- `[\r]` for a carriage return
- `[\t]` for a tab
- `[\u{1f600}]` for a hexadecimal Unicode escape sequence

## Constructor

### `str`

Converts a value to a string.

- Integers are formatted in base 10. This can be overridden with the
  optional `base` parameter.
- Floats are formatted in base 10 and never in exponential notation.
- Negative integers and floats are formatted with the Unicode minus sign
  ("−" U+2212) instead of the ASCII minus sign ("-" U+002D).
- From labels the name is extracted.
- Bytes are decoded as UTF-8.

If you wish to convert from and to Unicode code points, see the
[`to-unicode`]($str.to-unicode) and [`from-unicode`]($str.from-unicode)
functions.




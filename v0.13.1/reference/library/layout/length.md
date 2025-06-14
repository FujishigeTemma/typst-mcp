# Length

A size or distance, possibly expressed with contextual units.

Typst supports the following length units:

- Points: `{72pt}`
- Millimeters: `{254mm}`
- Centimeters: `{2.54cm}`
- Inches: `{1in}`
- Relative to font size: `{2.5em}`

You can multiply lengths with and divide them by integers and floats.

# Example
```example
#rect(width: 20pt)
#rect(width: 2em)
#rect(width: 1in)

#(3em + 5pt).em \
#(20pt).em \
#(40em + 2pt).abs \
#(5em).abs
```

# Fields
- `abs`: A length with just the absolute component of the current length
  (that is, excluding the `em` component).
- `em`: The amount of `em` units in this length, as a [float].


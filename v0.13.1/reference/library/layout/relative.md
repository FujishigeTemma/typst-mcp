# Relative Length

A length in relation to some known length.

This type is a combination of a [length] with a [ratio]. It results from
addition and subtraction of a length and a ratio. Wherever a relative length
is expected, you can also use a bare length or ratio.

# Relative to the page
A common use case is setting the width or height of a layout element (e.g.,
[block], [rect], etc.) as a certain percentage of the width of the page.
Here, the rectangle's width is set to `{25%}`, so it takes up one fourth of
the page's _inner_ width (the width minus margins).

```example
#rect(width: 25%)
```

Bare lengths or ratios are always valid where relative lengths are expected,
but the two can also be freely mixed:
```example
#rect(width: 25% + 1cm)
```

If you're trying to size an element so that it takes up the page's _full_
width, you have a few options (this highly depends on your exact use case):

1. Set page margins to `{0pt}` (`[#set page(margin: 0pt)]`)
2. Multiply the ratio by the known full page width (`{21cm * 69%}`)
3. Use padding which will negate the margins (`[#pad(x: -2.5cm, ...)]`)
4. Use the page [background](page.background) or
   [foreground](page.foreground) field as those don't take margins into
   account (note that it will render the content outside of the document
   flow, see [place] to control the content position)

# Relative to a container
When a layout element (e.g. a [rect]) is nested in another layout container
(e.g. a [block]) instead of being a direct descendant of the page, relative
widths become relative to the container:

```example
#block(
  width: 100pt,
  fill: aqua,
  rect(width: 50%),
)
```

# Scripting
You can multiply relative lengths by [ratios]($ratio), [integers]($int), and
[floats]($float).

A relative length has the following fields:
- `length`: Its length component.
- `ratio`: Its ratio component.

```example
#(100% - 50pt).length \
#(100% - 50pt).ratio
```


# Selector

A filter for selecting elements within the document.

You can construct a selector in the following ways:
- you can use an element [function]
- you can filter for an element function with
  [specific fields]($function.where)
- you can use a [string]($str) or [regular expression]($regex)
- you can use a [`{<label>}`]($label)
- you can use a [`location`]
- call the [`selector`] constructor to convert any of the above types into a
  selector value and use the methods below to refine it

Selectors are used to [apply styling rules]($styling/#show-rules) to
elements. You can also use selectors to [query] the document for certain
types of elements.

Furthermore, you can pass a selector to several of Typst's built-in
functions to configure their behaviour. One such example is the [outline]
where it can be used to change which elements are listed within the outline.

Multiple selectors can be combined using the methods shown below. However,
not all kinds of selectors are supported in all places, at the moment.

# Example
```example
#context query(
  heading.where(level: 1)
    .or(heading.where(level: 2))
)

= This will be found
== So will this
=== But this will not.
```

## Constructor

### `selector`

Turns a value into a selector. The following values are accepted:
- An element function like a `heading` or `figure`.
- A `{<label>}`.
- A more complex selector like `{heading.where(level: 1)}`.


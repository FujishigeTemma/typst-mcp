# Outline

## `outline`

A table of contents, figures, or other elements.

This function generates a list of all occurrences of an element in the
document, up to a given [`depth`]($outline.depth). The element's numbering
and page number will be displayed in the outline alongside its title or
caption.

# Example
```example
#set heading(numbering: "1.")
#outline()

= Introduction
#lorem(5)

= Methods
== Setup
#lorem(10)
```

# Alternative outlines
In its default configuration, this function generates a table of contents.
By setting the `target` parameter, the outline can be used to generate a
list of other kinds of elements than headings.

In the example below, we list all figures containing images by setting
`target` to `{figure.where(kind: image)}`. Just the same, we could have set
it to `{figure.where(kind: table)}` to generate a list of tables.

We could also set it to just `figure`, without using a [`where`]($function.where)
selector, but then the list would contain _all_ figures, be it ones
containing images, tables, or other material.

```example
#outline(
  title: [List of Figures],
  target: figure.where(kind: image),
)

#figure(
  image("tiger.jpg"),
  caption: [A nice figure!],
)
```

# Styling the outline
At the most basic level, you can style the outline by setting properties on
it and its entries. This way, you can customize the outline's
[title]($outline.title), how outline entries are
[indented]($outline.indent), and how the space between an entry's text and
its page number should be [filled]($outline.entry.fill).

Richer customization is possible through configuration of the outline's
[entries]($outline.entry). The outline generates one entry for each outlined
element.

## Spacing the entries { #entry-spacing }
Outline entries are [blocks]($block), so you can adjust the spacing between
them with normal block-spacing rules:

```example
#show outline.entry.where(
  level: 1
): set block(above: 1.2em)

#outline()

= About ACME Corp.
== History
=== Origins
= Products
== ACME Tools
```

## Building an outline entry from its parts { #building-an-entry }
For full control, you can also write a transformational show rule on
`outline.entry`. However, the logic for properly formatting and indenting
outline entries is quite complex and the outline entry itself only contains
two fields: The level and the outlined element.

For this reason, various helper functions are provided. You can mix and
match these to compose an entry from just the parts you like.

The default show rule for an outline entry looks like this[^1]:
```typ
#show outline.entry: it => link(
  it.element.location(),
  it.indented(it.prefix(), it.inner()),
)
```

- The [`indented`]($outline.entry.indented) function takes an optional
  prefix and inner content and automatically applies the proper indentation
  to it, such that different entries align nicely and long headings wrap
  properly.

- The [`prefix`]($outline.entry.prefix) function formats the element's
  numbering (if any). It also appends a supplement for certain elements.

- The [`inner`]($outline.entry.inner) function combines the element's
  [`body`]($outline.entry.body), the filler, and the
  [`page` number]($outline.entry.page).

You can use these individual functions to format the outline entry in
different ways. Let's say, you'd like to fully remove the filler and page
numbers. To achieve this, you could write a show rule like this:

```example
#show outline.entry: it => link(
  it.element.location(),
  // Keep just the body, dropping
  // the fill and the page.
  it.indented(it.prefix(), it.body()),
)

#outline()

= About ACME Corp.
== History
```

[^1]: The outline of equations is the exception to this rule as it does not
      have a body and thus does not use indented layout.

## Parameters

### title 

The title of the outline.

- When set to `{auto}`, an appropriate title for the
  [text language]($text.lang) will be used.
- When set to `{none}`, the outline will not have a title.
- A custom title can be set by passing content.

The outline's heading will not be numbered by default, but you can
force it to be with a show-set rule:
`{show outline: set heading(numbering: "1.")}`

### target 

The type of element to include in the outline.

To list figures containing a specific kind of element, like an image or
a table, you can specify the desired kind in a [`where`]($function.where)
selector. See the section on [alternative outlines]($outline/#alternative-outlines)
for more details.



### depth 

The maximum level up to which elements are included in the outline. When
this argument is `{none}`, all elements are included.



### indent 

How to indent the outline's entries.

- `{auto}`: Indents the numbering/prefix of a nested entry with the
  title of its parent entry. If the entries are not numbered (e.g., via
  [heading numbering]($heading.numbering)), this instead simply inserts
  a fixed amount of `{1.2em}` indent per level.

- [Relative length]($relative): Indents the entry by the specified
  length per nesting level. Specifying `{2em}`, for instance, would
  indent top-level headings by `{0em}` (not nested), second level
  headings by `{2em}` (nested once), third-level headings by `{4em}`
  (nested twice) and so on.

- [Function]($function): You can further customize this setting with a
  function. That function receives the nesting level as a parameter
  (starting at 0 for top-level headings/elements) and should return a
  (relative) length. For example, `{n => n * 2em}` would be equivalent
  to just specifying `{2em}`.



## Returns

- content


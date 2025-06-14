# Heading

## `heading`

A section heading.

With headings, you can structure your document into sections. Each heading
has a _level,_ which starts at one and is unbounded upwards. This level
indicates the logical role of the following content (section, subsection,
etc.) A top-level heading indicates a top-level section of the document
(not the document's title).

Typst can automatically number your headings for you. To enable numbering,
specify how you want your headings to be numbered with a
[numbering pattern or function]($numbering).

Independently of the numbering, Typst can also automatically generate an
[outline] of all headings for you. To exclude one or more headings from this
outline, you can set the `outlined` parameter to `{false}`.

# Example
```example
#set heading(numbering: "1.a)")

= Introduction
In recent years, ...

== Preliminaries
To start, ...
```

# Syntax
Headings have dedicated syntax: They can be created by starting a line with
one or multiple equals signs, followed by a space. The number of equals
signs determines the heading's logical nesting depth. The `{offset}` field
can be set to configure the starting depth.

## Parameters

### level 

The absolute nesting depth of the heading, starting from one. If set
to `{auto}`, it is computed from `{offset + depth}`.

This is primarily useful for usage in [show rules]($styling/#show-rules)
(either with [`where`]($function.where) selectors or by accessing the
level directly on a shown heading).



### depth 

The relative nesting depth of the heading, starting from one. This is
combined with `{offset}` to compute the actual `{level}`.

This is set by the heading syntax, such that `[== Heading]` creates a
heading with logical depth of 2, but actual level `{offset + 2}`. If you
construct a heading manually, you should typically prefer this over
setting the absolute level.

### offset 

The starting offset of each heading's `{level}`, used to turn its
relative `{depth}` into its absolute `{level}`.



### numbering 

How to number the heading. Accepts a
[numbering pattern or function]($numbering).



### supplement 

A supplement for the heading.

For references to headings, this is added before the referenced number.

If a function is specified, it is passed the referenced heading and
should return content.



### outlined 

Whether the heading should appear in the [outline].

Note that this property, if set to `{true}`, ensures the heading is also
shown as a bookmark in the exported PDF's outline (when exporting to
PDF). To change that behavior, use the `bookmarked` property.



### bookmarked 

Whether the heading should appear as a bookmark in the exported PDF's
outline. Doesn't affect other export formats, such as PNG.

The default value of `{auto}` indicates that the heading will only
appear in the exported PDF's outline if its `outlined` property is set
to `{true}`, that is, if it would also be listed in Typst's [outline].
Setting this property to either `{true}` (bookmark) or `{false}` (don't
bookmark) bypasses that behavior.



### hanging-indent 

The indent all but the first line of a heading should have.

The default value of `{auto}` indicates that the subsequent heading
lines will be indented based on the width of the numbering.



### body *(required)*

The heading's title.

## Returns

- content


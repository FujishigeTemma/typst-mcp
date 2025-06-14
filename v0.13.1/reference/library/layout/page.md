# Page

## `page`

Layouts its child onto one or multiple pages.

Although this function is primarily used in set rules to affect page
properties, it can also be used to explicitly render its argument onto
a set of pages of its own.

Pages can be set to use `{auto}` as their width or height. In this case, the
pages will grow to fit their content on the respective axis.

The [Guide for Page Setup]($guides/page-setup-guide) explains how to use
this and related functions to set up a document with many examples.

# Example
```example
>>> #set page(margin: auto)
#set page("us-letter")

There you go, US friends!
```

## Parameters

### paper 

A standard paper size to set width and height.

This is just a shorthand for setting `width` and `height` and, as such,
cannot be retrieved in a context expression.

### width 

The width of the page.



### height 

The height of the page.

If this is set to `{auto}`, page breaks can only be triggered manually
by inserting a [page break]($pagebreak) or by adding another non-empty
page set rule. Most examples throughout this documentation use `{auto}`
for the height of the page to dynamically grow and shrink to fit their
content.

### flipped 

Whether the page is flipped into landscape orientation.



### margin 

The page's margins.

- `{auto}`: The margins are set automatically to 2.5/21 times the smaller
  dimension of the page. This results in 2.5cm margins for an A4 page.
- A single length: The same margin on all sides.
- A dictionary: With a dictionary, the margins can be set individually.
  The dictionary can contain the following keys in order of precedence:
  - `top`: The top margin.
  - `right`: The right margin.
  - `bottom`: The bottom margin.
  - `left`: The left margin.
  - `inside`: The margin at the inner side of the page (where the
    [binding]($page.binding) is).
  - `outside`: The margin at the outer side of the page (opposite to the
    [binding]($page.binding)).
  - `x`: The horizontal margins.
  - `y`: The vertical margins.
  - `rest`: The margins on all sides except those for which the
    dictionary explicitly sets a size.

The values for `left` and `right` are mutually exclusive with
the values for `inside` and `outside`.



### binding 

On which side the pages will be bound.

- `{auto}`: Equivalent to `left` if the [text direction]($text.dir)
  is left-to-right and `right` if it is right-to-left.
- `left`: Bound on the left side.
- `right`: Bound on the right side.

This affects the meaning of the `inside` and `outside` options for
margins.

### columns 

How many columns the page has.

If you need to insert columns into a page or other container, you can
also use the [`columns` function]($columns).



### fill 

The page's background fill.

Setting this to something non-transparent instructs the printer to color
the complete page. If you are considering larger production runs, it may
be more environmentally friendly and cost-effective to source pre-dyed
pages and not set this property.

When set to `{none}`, the background becomes transparent. Note that PDF
pages will still appear with a (usually white) background in viewers,
but they are actually transparent. (If you print them, no color is used
for the background.)

The default of `{auto}` results in `{none}` for PDF output, and
`{white}` for PNG and SVG.



### numbering 

How to [number]($numbering) the pages.

If an explicit `footer` (or `header` for top-aligned numbering) is
given, the numbering is ignored.



### supplement 

A supplement for the pages.

For page references, this is added before the page number.



### number-align 

The alignment of the page numbering.

If the vertical component is `top`, the numbering is placed into the
header and if it is `bottom`, it is placed in the footer. Horizon
alignment is forbidden. If an explicit matching `header` or `footer` is
given, the numbering is ignored.



### header 

The page's header. Fills the top margin of each page.

- Content: Shows the content as the header.
- `{auto}`: Shows the page number if a `numbering` is set and
  `number-align` is `top`.
- `{none}`: Suppresses the header.



### header-ascent 

The amount the header is raised into the top margin.

### footer 

The page's footer. Fills the bottom margin of each page.

- Content: Shows the content as the footer.
- `{auto}`: Shows the page number if a `numbering` is set and
  `number-align` is `bottom`.
- `{none}`: Suppresses the footer.

For just a page number, the `numbering` property typically suffices. If
you want to create a custom footer but still display the page number,
you can directly access the [page counter]($counter).



### footer-descent 

The amount the footer is lowered into the bottom margin.

### background 

Content in the page's background.

This content will be placed behind the page's body. It can be
used to place a background image or a watermark.



### foreground 

Content in the page's foreground.

This content will overlay the page's body.



### body *(required)*

The contents of the page(s).

Multiple pages will be created if the content does not fit on a single
page. A new page with the page properties prior to the function invocation
will be created after the body has been typeset.

## Returns

- content


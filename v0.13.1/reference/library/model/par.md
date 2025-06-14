# Paragraph

## `par`

A logical subdivison of textual content.

Typst automatically collects _inline-level_ elements into paragraphs.
Inline-level elements include [text], [horizontal spacing]($h),
[boxes]($box), and [inline equations]($math.equation).

To separate paragraphs, use a blank line (or an explicit [`parbreak`]).
Paragraphs are also automatically interrupted by any block-level element
(like [`block`], [`place`], or anything that shows itself as one of these).

The `par` element is primarily used in set rules to affect paragraph
properties, but it can also be used to explicitly display its argument as a
paragraph of its own. Then, the paragraph's body may not contain any
block-level content.

# Boxes and blocks
As explained above, usually paragraphs only contain inline-level content.
However, you can integrate any kind of block-level content into a paragraph
by wrapping it in a [`box`].

Conversely, you can separate inline-level content from a paragraph by
wrapping it in a [`block`]. In this case, it will not become part of any
paragraph at all. Read the following section for an explanation of why that
matters and how it differs from just adding paragraph breaks around the
content.

# What becomes a paragraph?
When you add inline-level content to your document, Typst will automatically
wrap it in paragraphs. However, a typical document also contains some text
that is not semantically part of a paragraph, for example in a heading or
caption.

The rules for when Typst wraps inline-level content in a paragraph are as
follows:

- All text at the root of a document is wrapped in paragraphs.

- Text in a container (like a `block`) is only wrapped in a paragraph if the
  container holds any block-level content. If all of the contents are
  inline-level, no paragraph is created.

In the laid-out document, it's not immediately visible whether text became
part of a paragraph. However, it is still important for various reasons:

- Certain paragraph styling like `first-line-indent` will only apply to
  proper paragraphs, not any text. Similarly, `par` show rules of course
  only trigger on paragraphs.

- A proper distinction between paragraphs and other text helps people who
  rely on assistive technologies (such as screen readers) navigate and
  understand the document properly. Currently, this only applies to HTML
  export since Typst does not yet output accessible PDFs, but support for
  this is planned for the near future.

- HTML export will generate a `<p>` tag only for paragraphs.

When creating custom reusable components, you can and should take charge
over whether Typst creates paragraphs. By wrapping text in a [`block`]
instead of just adding paragraph breaks around it, you can force the absence
of a paragraph. Conversely, by adding a [`parbreak`] after some content in a
container, you can force it to become a paragraph even if it's just one
word. This is, for example, what [non-`tight`]($list.tight) lists do to
force their items to become paragraphs.

# Example
```example
#set par(
  first-line-indent: 1em,
  spacing: 0.65em,
  justify: true,
)

We proceed by contradiction.
Suppose that there exists a set
of positive integers $a$, $b$, and
$c$ that satisfies the equation
$a^n + b^n = c^n$ for some
integer value of $n > 2$.

Without loss of generality,
let $a$ be the smallest of the
three integers. Then, we ...
```

## Parameters

### leading 

The spacing between lines.

Leading defines the spacing between the [bottom edge]($text.bottom-edge)
of one line and the [top edge]($text.top-edge) of the following line. By
default, these two properties are up to the font, but they can also be
configured manually with a text set rule.

By setting top edge, bottom edge, and leading, you can also configure a
consistent baseline-to-baseline distance. You could, for instance, set
the leading to `{1em}`, the top-edge to `{0.8em}`, and the bottom-edge
to `{-0.2em}` to get a baseline gap of exactly `{2em}`. The exact
distribution of the top- and bottom-edge values affects the bounds of
the first and last line.

### spacing 

The spacing between paragraphs.

Just like leading, this defines the spacing between the bottom edge of a
paragraph's last line and the top edge of the next paragraph's first
line.

When a paragraph is adjacent to a [`block`] that is not a paragraph,
that block's [`above`]($block.above) or [`below`]($block.below) property
takes precedence over the paragraph spacing. Headings, for instance,
reduce the spacing below them by default for a better look.

### justify 

Whether to justify text in its line.

Hyphenation will be enabled for justified paragraphs if the
[text function's `hyphenate` property]($text.hyphenate) is set to
`{auto}` and the current language is known.

Note that the current [alignment]($align.alignment) still has an effect
on the placement of the last line except if it ends with a
[justified line break]($linebreak.justify).

### linebreaks 

How to determine line breaks.

When this property is set to `{auto}`, its default value, optimized line
breaks will be used for justified paragraphs. Enabling optimized line
breaks for ragged paragraphs may also be worthwhile to improve the
appearance of the text.



### first-line-indent 

The indent the first line of a paragraph should have.

By default, only the first line of a consecutive paragraph will be
indented (not the first one in the document or container, and not
paragraphs immediately following other block-level elements).

If you want to indent all paragraphs instead, you can pass a dictionary
containing the `amount` of indent as a length and the pair
`{all: true}`. When `all` is omitted from the dictionary, it defaults to
`{false}`.

By typographic convention, paragraph breaks are indicated either by some
space between paragraphs or by indented first lines. Consider
- reducing the [paragraph `spacing`]($par.spacing) to the
  [`leading`]($par.leading) using `{set par(spacing: 0.65em)}`
- increasing the [block `spacing`]($block.spacing) (which inherits the
  paragraph spacing by default) to the original paragraph spacing using
  `{set block(spacing: 1.2em)}`



### hanging-indent 

The indent that all but the first line of a paragraph should have.



### body *(required)*

The contents of the paragraph.

## Returns

- content


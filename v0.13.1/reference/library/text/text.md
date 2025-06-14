# Text

## `text`

Customizes the look and layout of text in a variety of ways.

This function is used frequently, both with set rules and directly. While
the set rule is often the simpler choice, calling the `text` function
directly can be useful when passing text as an argument to another function.

# Example
```example
#set text(18pt)
With a set rule.

#emph(text(blue)[
  With a function call.
])
```

## Parameters

### font 

A font family descriptor or priority list of font family descriptor.

A font family descriptor can be a plain string representing the family
name or a dictionary with the following keys:

- `name` (required): The font family name.
- `covers` (optional): Defines the Unicode codepoints for which the
  family shall be used. This can be:
  - A predefined coverage set:
    - `{"latin-in-cjk"}` covers all codepoints except for those which
      exist in Latin fonts, but should preferrably be taken from CJK
      fonts.
  - A [regular expression]($regex) that defines exactly which codepoints
    shall be covered. Accepts only the subset of regular expressions
    which consist of exactly one dot, letter, or character class.

When processing text, Typst tries all specified font families in order
until it finds a font that has the necessary glyphs. In the example
below, the font `Inria Serif` is preferred, but since it does not
contain Arabic glyphs, the arabic text uses `Noto Sans Arabic` instead.

The collection of available fonts differs by platform:

- In the web app, you can see the list of available fonts by clicking on
  the "Ag" button. You can provide additional fonts by uploading `.ttf`
  or `.otf` files into your project. They will be discovered
  automatically. The priority is: project fonts > server fonts.

- Locally, Typst uses your installed system fonts or embedded fonts in
  the CLI, which are `Libertinus Serif`, `New Computer Modern`,
  `New Computer Modern Math`, and `DejaVu Sans Mono`. In addition, you
  can use the `--font-path` argument or `TYPST_FONT_PATHS` environment
  variable to add directories that should be scanned for fonts. The
  priority is: `--font-paths` > system fonts > embedded fonts. Run
  `typst fonts` to see the fonts that Typst has discovered on your
  system. Note that you can pass the `--ignore-system-fonts` parameter
  to the CLI to ensure Typst won't search for system fonts.



### fallback 

Whether to allow last resort font fallback when the primary font list
contains no match. This lets Typst search through all available fonts
for the most similar one that has the necessary glyphs.

_Note:_ Currently, there are no warnings when fallback is disabled and
no glyphs are found. Instead, your text shows up in the form of "tofus":
Small boxes that indicate the lack of an appropriate glyph. In the
future, you will be able to instruct Typst to issue warnings so you know
something is up.



### style 

The desired font style.

When an italic style is requested and only an oblique one is available,
it is used. Similarly, the other way around, an italic style can stand
in for an oblique one.  When neither an italic nor an oblique style is
available, Typst selects the normal style. Since most fonts are only
available either in an italic or oblique style, the difference between
italic and oblique style is rarely observable.

If you want to emphasize your text, you should do so using the [emph]
function instead. This makes it easy to adapt the style later if you
change your mind about how to signify the emphasis.



### weight 

The desired thickness of the font's glyphs. Accepts an integer between
`{100}` and `{900}` or one of the predefined weight names. When the
desired weight is not available, Typst selects the font from the family
that is closest in weight.

If you want to strongly emphasize your text, you should do so using the
[strong] function instead. This makes it easy to adapt the style later
if you change your mind about how to signify the strong emphasis.



### stretch 

The desired width of the glyphs. Accepts a ratio between `{50%}` and
`{200%}`. When the desired width is not available, Typst selects the
font from the family that is closest in stretch. This will only stretch
the text if a condensed or expanded version of the font is available.

If you want to adjust the amount of space between characters instead of
stretching the glyphs itself, use the [`tracking`]($text.tracking)
property instead.



### size 

The size of the glyphs. This value forms the basis of the `em` unit:
`{1em}` is equivalent to the font size.

You can also give the font size itself in `em` units. Then, it is
relative to the previous font size.



### fill 

The glyph fill paint.



### stroke 

How to stroke the text.



### tracking 

The amount of space that should be added between characters.



### spacing 

The amount of space between words.

Can be given as an absolute length, but also relative to the width of
the space character in the font.

If you want to adjust the amount of space between characters rather than
words, use the [`tracking`]($text.tracking) property instead.



### cjk-latin-spacing 

Whether to automatically insert spacing between CJK and Latin characters.



### baseline 

An amount to shift the text baseline by.



### overhang 

Whether certain glyphs can hang over into the margin in justified text.
This can make justification visually more pleasing.



### top-edge 

The top end of the conceptual frame around the text used for layout and
positioning. This affects the size of containers that hold text.



### bottom-edge 

The bottom end of the conceptual frame around the text used for layout
and positioning. This affects the size of containers that hold text.



### lang 

An [ISO 639-1/2/3 language code.](https://en.wikipedia.org/wiki/ISO_639)

Setting the correct language affects various parts of Typst:

- The text processing pipeline can make more informed choices.
- Hyphenation will use the correct patterns for the language.
- [Smart quotes]($smartquote) turns into the correct quotes for the
  language.
- And all other things which are language-aware.



### region 

An [ISO 3166-1 alpha-2 region code.](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

This lets the text processing pipeline make more informed choices.

### script 

The OpenType writing script.

The combination of `{lang}` and `{script}` determine how font features,
such as glyph substitution, are implemented. Frequently the value is a
modified (all-lowercase) ISO 15924 script identifier, and the `math`
writing script is used for features appropriate for mathematical
symbols.

When set to `{auto}`, the default and recommended setting, an
appropriate script is chosen for each block of characters sharing a
common Unicode script property.



### dir 

The dominant direction for text and inline objects. Possible values are:

- `{auto}`: Automatically infer the direction from the `lang` property.
- `{ltr}`: Layout text from left to right.
- `{rtl}`: Layout text from right to left.

When writing in right-to-left scripts like Arabic or Hebrew, you should
set the [text language]($text.lang) or direction. While individual runs
of text are automatically layouted in the correct direction, setting the
dominant direction gives the bidirectional reordering algorithm the
necessary information to correctly place punctuation and inline objects.
Furthermore, setting the direction affects the alignment values `start`
and `end`, which are equivalent to `left` and `right` in `ltr` text and
the other way around in `rtl` text.

If you set this to `rtl` and experience bugs or in some way bad looking
output, please get in touch with us through the
[Forum](https://forum.typst.app/),
[Discord server](https://discord.gg/2uDybryKPe),
or our [contact form](https://typst.app/contact).



### hyphenate 

Whether to hyphenate text to improve line breaking. When `{auto}`, text
will be hyphenated if and only if justification is enabled.

Setting the [text language]($text.lang) ensures that the correct
hyphenation patterns are used.



### costs 

The "cost" of various choices when laying out text. A higher cost means
the layout engine will make the choice less often. Costs are specified
as a ratio of the default cost, so `{50%}` will make text layout twice
as eager to make a given choice, while `{200%}` will make it half as
eager.

Currently, the following costs can be customized:
- `hyphenation`: splitting a word across multiple lines
- `runt`: ending a paragraph with a line with a single word
- `widow`: leaving a single line of paragraph on the next page
- `orphan`: leaving single line of paragraph on the previous page

Hyphenation is generally avoided by placing the whole word on the next
line, so a higher hyphenation cost can result in awkward justification
spacing. Note: Hyphenation costs will only be applied when the
[`linebreaks`]($par.linebreaks) are set to "optimized". (For example
by default implied by [`justify`]($par.justify).)

Runts are avoided by placing more or fewer words on previous lines, so a
higher runt cost can result in more awkward in justification spacing.

Text layout prevents widows and orphans by default because they are
generally discouraged by style guides. However, in some contexts they
are allowed because the prevention method, which moves a line to the
next page, can result in an uneven number of lines between pages. The
`widow` and `orphan` costs allow disabling these modifications.
(Currently, `{0%}` allows widows/orphans; anything else, including the
default of `{100%}`, prevents them. More nuanced cost specification for
these modifications is planned for the future.)



### kerning 

Whether to apply kerning.

When enabled, specific letter pairings move closer together or further
apart for a more visually pleasing result. The example below
demonstrates how decreasing the gap between the "T" and "o" results in a
more natural look. Setting this to `{false}` disables kerning by turning
off the OpenType `kern` font feature.



### alternates 

Whether to apply stylistic alternates.

Sometimes fonts contain alternative glyphs for the same codepoint.
Setting this to `{true}` switches to these by enabling the OpenType
`salt` font feature.



### stylistic-set 

Which stylistic sets to apply. Font designers can categorize alternative
glyphs forms into stylistic sets. As this value is highly font-specific,
you need to consult your font to know which sets are available.

This can be set to an integer or an array of integers, all
of which must be between `{1}` and `{20}`, enabling the
corresponding OpenType feature(s) from `ss01` to `ss20`.
Setting this to `{none}` will disable all stylistic sets.



### ligatures 

Whether standard ligatures are active.

Certain letter combinations like "fi" are often displayed as a single
merged glyph called a _ligature._ Setting this to `{false}` disables
these ligatures by turning off the OpenType `liga` and `clig` font
features.



### discretionary-ligatures 

Whether ligatures that should be used sparingly are active. Setting this
to `{true}` enables the OpenType `dlig` font feature.

### historical-ligatures 

Whether historical ligatures are active. Setting this to `{true}`
enables the OpenType `hlig` font feature.

### number-type 

Which kind of numbers / figures to select. When set to `{auto}`, the
default numbers for the font are used.



### number-width 

The width of numbers / figures. When set to `{auto}`, the default
numbers for the font are used.



### slashed-zero 

Whether to have a slash through the zero glyph. Setting this to `{true}`
enables the OpenType `zero` font feature.



### fractions 

Whether to turn numbers into fractions. Setting this to `{true}`
enables the OpenType `frac` font feature.

It is not advisable to enable this property globally as it will mess
with all appearances of numbers after a slash (e.g., in URLs). Instead,
enable it locally when you want a fraction.



### features 

Raw OpenType features to apply.

- If given an array of strings, sets the features identified by the
  strings to `{1}`.
- If given a dictionary mapping to numbers, sets the features
  identified by the keys to the values.



### body *(required)*

Content in which all text is styled according to the other arguments.

### text *(required)*

The text.

## Returns

- content


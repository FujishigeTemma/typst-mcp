# Raw Text / Code

## `raw`

Raw text with optional syntax highlighting.

Displays the text verbatim and in a monospace font. This is typically used
to embed computer code into your document.

# Example
````example
Adding `rbx` to `rcx` gives
the desired result.

What is ```rust fn main()``` in Rust
would be ```c int main()``` in C.

```rust
fn main() {
    println!("Hello World!");
}
```

This has ``` `backticks` ``` in it
(but the spaces are trimmed). And
``` here``` the leading space is
also trimmed.
````

You can also construct a [`raw`] element programmatically from a string (and
provide the language tag via the optional [`lang`]($raw.lang) argument).
```example
#raw("fn " + "main() {}", lang: "rust")
```

# Syntax
This function also has dedicated syntax. You can enclose text in 1 or 3+
backticks (`` ` ``) to make it raw. Two backticks produce empty raw text.
This works both in markup and code.

When you use three or more backticks, you can additionally specify a
language tag for syntax highlighting directly after the opening backticks.
Within raw blocks, everything (except for the language tag, if applicable)
is rendered as is, in particular, there are no escape sequences.

The language tag is an identifier that directly follows the opening
backticks only if there are three or more backticks. If your text starts
with something that looks like an identifier, but no syntax highlighting is
needed, start the text with a single space (which will be trimmed) or use
the single backtick syntax. If your text should start or end with a
backtick, put a space before or after it (it will be trimmed).

## Parameters

### text *(required)*

The raw text.

You can also use raw blocks creatively to create custom syntaxes for
your automations.



### block 

Whether the raw text is displayed as a separate block.

In markup mode, using one-backtick notation makes this `{false}`.
Using three-backtick notation makes it `{true}` if the enclosed content
contains at least one line break.



### lang 

The language to syntax-highlight in.

Apart from typical language tags known from Markdown, this supports the
`{"typ"}`, `{"typc"}`, and `{"typm"}` tags for
[Typst markup]($reference/syntax/#markup),
[Typst code]($reference/syntax/#code), and
[Typst math]($reference/syntax/#math), respectively.



### align 

The horizontal alignment that each line in a raw block should have.
This option is ignored if this is not a raw block (if specified
`block: false` or single backticks were used in markup mode).

By default, this is set to `{start}`, meaning that raw text is
aligned towards the start of the text direction inside the block
by default, regardless of the current context's alignment (allowing
you to center the raw block itself without centering the text inside
it, for example).



### syntaxes 

Additional syntax definitions to load. The syntax definitions should be
in the [`sublime-syntax` file format](https://www.sublimetext.com/docs/syntax.html).

You can pass any of the following values:

- A path string to load a syntax file from the given path. For more
  details about paths, see the [Paths section]($syntax/#paths).
- Raw bytes from which the syntax should be decoded.
- An array where each item is one of the above.



### theme 

The theme to use for syntax highlighting. Themes should be in the
[`tmTheme` file format](https://www.sublimetext.com/docs/color_schemes_tmtheme.html).

You can pass any of the following values:

- `{none}`: Disables syntax highlighting.
- `{auto}`: Highlights with Typst's default theme.
- A path string to load a theme file from the given path. For more
  details about paths, see the [Paths section]($syntax/#paths).
- Raw bytes from which the theme should be decoded.

Applying a theme only affects the color of specifically highlighted
text. It does not consider the theme's foreground and background
properties, so that you retain control over the color of raw text. You
can apply the foreground color yourself with the [`text`] function and
the background with a [filled block]($block.fill). You could also use
the [`xml`] function to extract these properties from the theme.



### tab-size 

The size for a tab stop in spaces. A tab is replaced with enough spaces to
align with the next multiple of the size.



## Returns

- content


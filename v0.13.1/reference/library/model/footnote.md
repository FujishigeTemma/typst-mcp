# Footnote

## `footnote`

A footnote.

Includes additional remarks and references on the same page with footnotes.
A footnote will insert a superscript number that links to the note at the
bottom of the page. Notes are numbered sequentially throughout your document
and can break across multiple pages.

To customize the appearance of the entry in the footnote listing, see
[`footnote.entry`]($footnote.entry). The footnote itself is realized as a
normal superscript, so you can use a set rule on the [`super`] function to
customize it. You can also apply a show rule to customize only the footnote
marker (superscript number) in the running text.

# Example
```example
Check the docs for more details.
#footnote[https://typst.app/docs]
```

The footnote automatically attaches itself to the preceding word, even if
there is a space before it in the markup. To force space, you can use the
string `[#" "]` or explicit [horizontal spacing]($h).

By giving a label to a footnote, you can have multiple references to it.

```example
You can edit Typst documents online.
#footnote[https://typst.app/app] <fn>
Checkout Typst's website. @fn
And the online app. #footnote(<fn>)
```

_Note:_ Set and show rules in the scope where `footnote` is called may not
apply to the footnote's content. See [here][issue] for more information.

[issue]: https://github.com/typst/typst/issues/1467#issuecomment-1588799440

## Parameters

### numbering 

How to number footnotes.

By default, the footnote numbering continues throughout your document.
If you prefer per-page footnote numbering, you can reset the footnote
[counter] in the page [header]($page.header). In the future, there might
be a simpler way to achieve this.



### body *(required)*

The content to put into the footnote. Can also be the label of another
footnote this one should point to.

## Returns

- content


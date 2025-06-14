# Elem

## `elem`

An HTML element that can contain Typst content.

Typst's HTML export automatically generates the appropriate tags for most
elements. However, sometimes, it is desirable to retain more control. For
example, when using Typst to generate your blog, you could use this function
to wrap each article in an `<article>` tag.

Typst is aware of what is valid HTML. A tag and its attributes must form
syntactically valid HTML. Some tags, like `meta` do not accept content.
Hence, you must not provide a body for them. We may add more checks in the
future, so be sure that you are generating valid HTML when using this
function.

Normally, Typst will generate `html`, `head`, and `body` tags for you. If
you instead create them with this function, Typst will omit its own tags.

```typ
#html.elem("div", attrs: (style: "background: aqua"))[
  A div with _Typst content_ inside!
]
```

## Parameters

### tag *(required)*

The element's tag.

### attrs 

The element's HTML attributes.

### body 

The contents of the HTML element.

The body can be arbitrary Typst content.

## Returns

- content


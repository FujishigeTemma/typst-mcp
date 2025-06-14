# Link

## `link`

Links to a URL or a location in the document.

By default, links do not look any different from normal text. However,
you can easily apply a style of your choice with a show rule.

# Example
```example
#show link: underline

https://example.com \

#link("https://example.com") \
#link("https://example.com")[
  See example.com
]
```

# Hyphenation
If you enable hyphenation or justification, by default, it will not apply to
links to prevent unwanted hyphenation in URLs. You can opt out of this
default via `{show link: set text(hyphenate: true)}`.

# Syntax
This function also has dedicated syntax: Text that starts with `http://` or
`https://` is automatically turned into a link.

## Parameters

### dest *(required)*

The destination the link points to.

- To link to web pages, `dest` should be a valid URL string. If the URL
  is in the `mailto:` or `tel:` scheme and the `body` parameter is
  omitted, the email address or phone number will be the link's body,
  without the scheme.

- To link to another part of the document, `dest` can take one of three
  forms:
  - A [label] attached to an element. If you also want automatic text
    for the link based on the element, consider using a
    [reference]($ref) instead.

  - A [`location`] (typically retrieved from [`here`], [`locate`] or
    [`query`]).

  - A dictionary with a `page` key of type [integer]($int) and `x` and
    `y` coordinates of type [length]. Pages are counted from one, and
    the coordinates are relative to the page's top left corner.



### body *(required)*

The content that should become a link.

If `dest` is an URL string, the parameter can be omitted. In this case,
the URL will be shown as the link.

## Returns

- content


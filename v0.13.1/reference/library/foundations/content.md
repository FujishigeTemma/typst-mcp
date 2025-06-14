# Content

A piece of document content.

This type is at the heart of Typst. All markup you write and most
[functions]($function) you call produce content values. You can create a
content value by enclosing markup in square brackets. This is also how you
pass content to functions.

# Example
```example
Type of *Hello!* is
#type([*Hello!*])
```

Content can be added with the `+` operator,
[joined together]($scripting/#blocks) and multiplied with integers. Wherever
content is expected, you can also pass a [string]($str) or `{none}`.

# Representation
Content consists of elements with fields. When constructing an element with
its _element function,_ you provide these fields as arguments and when you
have a content value, you can access its fields with [field access
syntax]($scripting/#field-access).

Some fields are required: These must be provided when constructing an
element and as a consequence, they are always available through field access
on content of that type. Required fields are marked as such in the
documentation.

Most fields are optional: Like required fields, they can be passed to the
element function to configure them for a single element. However, these can
also be configured with [set rules]($styling/#set-rules) to apply them to
all elements within a scope. Optional fields are only available with field
access syntax when they were explicitly passed to the element function, not
when they result from a set rule.

Each element has a default appearance. However, you can also completely
customize its appearance with a [show rule]($styling/#show-rules). The show
rule is passed the element. It can access the element's field and produce
arbitrary content from it.

In the web app, you can hover over a content variable to see exactly which
elements the content is composed of and what fields they have.
Alternatively, you can inspect the output of the [`repr`] function.


# Function

A mapping from argument values to a return value.

You can call a function by writing a comma-separated list of function
_arguments_ enclosed in parentheses directly after the function name.
Additionally, you can pass any number of trailing content blocks arguments
to a function _after_ the normal argument list. If the normal argument list
would become empty, it can be omitted. Typst supports positional and named
arguments. The former are identified by position and type, while the latter
are written as `name: value`.

Within math mode, function calls have special behaviour. See the
[math documentation]($category/math) for more details.

# Example
```example
// Call a function.
#list([A], [B])

// Named arguments and trailing
// content blocks.
#enum(start: 2)[A][B]

// Version without parentheses.
#list[A][B]
```

Functions are a fundamental building block of Typst. Typst provides
functions for a variety of typesetting tasks. Moreover, the markup you write
is backed by functions and all styling happens through functions. This
reference lists all available functions and how you can use them. Please
also refer to the documentation about [set]($styling/#set-rules) and
[show]($styling/#show-rules) rules to learn about additional ways you can
work with functions in Typst.

# Element functions
Some functions are associated with _elements_ like [headings]($heading) or
[tables]($table). When called, these create an element of their respective
kind. In contrast to normal functions, they can further be used in [set
rules]($styling/#set-rules), [show rules]($styling/#show-rules), and
[selectors]($selector).

# Function scopes
Functions can hold related definitions in their own scope, similar to a
[module]($scripting/#modules). Examples of this are
[`assert.eq`]($assert.eq) or [`list.item`]($list.item). However, this
feature is currently only available for built-in functions.

# Defining functions
You can define your own function with a [let binding]($scripting/#bindings)
that has a parameter list after the binding's name. The parameter list can
contain mandatory positional parameters, named parameters with default
values and [argument sinks]($arguments).

The right-hand side of a function binding is the function body, which can be
a block or any other expression. It defines the function's return value and
can depend on the parameters. If the function body is a [code
block]($scripting/#blocks), the return value is the result of joining the
values of each expression in the block.

Within a function body, the `return` keyword can be used to exit early and
optionally specify a return value. If no explicit return value is given, the
body evaluates to the result of joining all expressions preceding the
`return`.

Functions that don't return any meaningful value return [`none`] instead.
The return type of such functions is not explicitly specified in the
documentation. (An example of this is [`array.push`]).

```example
#let alert(body, fill: red) = {
  set text(white)
  set align(center)
  rect(
    fill: fill,
    inset: 8pt,
    radius: 4pt,
    [*Warning:\ #body*],
  )
}

#alert[
  Danger is imminent!
]

#alert(fill: blue)[
  KEEP OFF TRACKS
]
```

# Importing functions
Functions can be imported from one file ([`module`]($scripting/#modules)) into
another using `{import}`. For example, assume that we have defined the `alert`
function from the previous example in a file called `foo.typ`. We can import
it into another file by writing `{import "foo.typ": alert}`.

# Unnamed functions { #unnamed }
You can also create an unnamed function without creating a binding by
specifying a parameter list followed by `=>` and the function body. If your
function has just one parameter, the parentheses around the parameter list
are optional. Unnamed functions are mainly useful for show rules, but also
for settable properties that take functions like the page function's
[`footer`]($page.footer) property.

```example
#show "once?": it => [#it #it]
once?
```

# Note on function purity
In Typst, all functions are _pure._ This means that for the same
arguments, they always return the same result. They cannot "remember" things to
produce another value when they are called a second time.

The only exception are built-in methods like
[`array.push(value)`]($array.push). These can modify the values they are
called on.


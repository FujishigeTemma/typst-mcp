# Page Break

## `pagebreak`

A manual page break.

Must not be used inside any containers.

# Example
```example
The next page contains
more details on compound theory.
#pagebreak()

== Compound Theory
In 1984, the first ...
```

## Parameters

### weak 

If `{true}`, the page break is skipped if the current page is already
empty.

### to 

If given, ensures that the next page will be an even/odd page, with an
empty page in between if necessary.



## Returns

- content


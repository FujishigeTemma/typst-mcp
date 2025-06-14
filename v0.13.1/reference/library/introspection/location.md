# Location

Identifies an element in the document.

A location uniquely identifies an element in the document and lets you
access its absolute position on the pages. You can retrieve the current
location with the [`here`] function and the location of a queried or shown
element with the [`location()`]($content.location) method on content.

# Locatable elements { #locatable }
Currently, only a subset of element functions is locatable. Aside from
headings and figures, this includes equations, references, quotes and all
elements with an explicit label. As a result, you _can_ query for e.g.
[`strong`] elements, but you will find only those that have an explicit
label attached to them. This limitation will be resolved in the future.


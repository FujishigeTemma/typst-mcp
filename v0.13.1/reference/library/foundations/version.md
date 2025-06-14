# Version

A version with an arbitrary number of components.

The first three components have names that can be used as fields: `major`,
`minor`, `patch`. All following components do not have names.

The list of components is semantically extended by an infinite list of
zeros. This means that, for example, `0.8` is the same as `0.8.0`. As a
special case, the empty version (that has no components at all) is the same
as `0`, `0.0`, `0.0.0`, and so on.

The current version of the Typst compiler is available as `sys.version`.

You can convert a version to an array of explicitly given components using
the [`array`] constructor.

## Constructor

### `version`

Creates a new version.

It can have any number of components (even zero).




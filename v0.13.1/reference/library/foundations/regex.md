# Regex

A regular expression.

Can be used as a [show rule selector]($styling/#show-rules) and with
[string methods]($str) like `find`, `split`, and `replace`.

[See here](https://docs.rs/regex/latest/regex/#syntax) for a specification
of the supported syntax.

# Example
```example
// Works with string methods.
#"a,b;c".split(regex("[,;]"))

// Works with show rules.
#show regex("\d+"): set text(red)

The numbers 1 to 10.
```

## Constructor

### `regex`

Create a regular expression from a string.


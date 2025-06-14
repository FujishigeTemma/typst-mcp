# Panic

## `panic`

Fails with an error.

Arguments are displayed to the user (not rendered in the document) as
strings, converting with `repr` if necessary.

# Example
The code below produces the error `panicked with: "this is wrong"`.
```typ
#panic("this is wrong")
```

## Parameters

### values *(required)*

The values to panic with and display to the user.


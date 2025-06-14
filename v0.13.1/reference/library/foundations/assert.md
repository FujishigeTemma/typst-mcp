# Assert

## `assert`

Ensures that a condition is fulfilled.

Fails with an error if the condition is not fulfilled. Does not
produce any output in the document.

If you wish to test equality between two values, see
[`assert.eq`]($assert.eq) and [`assert.ne`]($assert.ne).

# Example
```typ
#assert(1 < 2, message: "math broke")
```

## Parameters

### condition *(required)*

The condition that must be true for the assertion to pass.

### message 

The error message when the assertion fails.


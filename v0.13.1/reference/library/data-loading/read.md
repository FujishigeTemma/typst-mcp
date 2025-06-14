# Read

## `read`

Reads plain text or data from a file.

By default, the file will be read as UTF-8 and returned as a [string]($str).

If you specify `{encoding: none}`, this returns raw [bytes] instead.

# Example
```example
An example for a HTML file: \
#let text = read("example.html")
#raw(text, lang: "html")

Raw bytes:
#read("tiger.jpg", encoding: none)
```

## Parameters

### path *(required)*

Path to a file.

For more details, see the [Paths section]($syntax/#paths).

### encoding 

The encoding to read the file with.

If set to `{none}`, this function returns raw bytes.

## Returns

- str, bytes


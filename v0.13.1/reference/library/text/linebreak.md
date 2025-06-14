# Line Break

## `linebreak`

Inserts a line break.

Advances the paragraph to the next line. A single trailing line break at the
end of a paragraph is ignored, but more than one creates additional empty
lines.

# Example
```example
*Date:* 26.12.2022 \
*Topic:* Infrastructure Test \
*Severity:* High \
```

# Syntax
This function also has dedicated syntax: To insert a line break, simply write
a backslash followed by whitespace. This always creates an unjustified
break.

## Parameters

### justify 

Whether to justify the line before the break.

This is useful if you found a better line break opportunity in your
justified text than Typst did.



## Returns

- content


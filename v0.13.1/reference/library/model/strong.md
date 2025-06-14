# Strong Emphasis

## `strong`

Strongly emphasizes content by increasing the font weight.

Increases the current font weight by a given `delta`.

# Example
```example
This is *strong.* \
This is #strong[too.] \

#show strong: set text(red)
And this is *evermore.*
```

# Syntax
This function also has dedicated syntax: To strongly emphasize content,
simply enclose it in stars/asterisks (`*`). Note that this only works at
word boundaries. To strongly emphasize part of a word, you have to use the
function.

## Parameters

### delta 

The delta to apply on the font weight.



### body *(required)*

The content to strongly emphasize.

## Returns

- content


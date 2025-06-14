# Dictionary

A map from string keys to values.

You can construct a dictionary by enclosing comma-separated `key: value`
pairs in parentheses. The values do not have to be of the same type. Since
empty parentheses already yield an empty array, you have to use the special
`(:)` syntax to create an empty dictionary.

A dictionary is conceptually similar to an array, but it is indexed by
strings instead of integers. You can access and create dictionary entries
with the `.at()` method. If you know the key statically, you can
alternatively use [field access notation]($scripting/#fields) (`.key`) to
access the value. Dictionaries can be added with the `+` operator and
[joined together]($scripting/#blocks). To check whether a key is present in
the dictionary, use the `in` keyword.

You can iterate over the pairs in a dictionary using a [for
loop]($scripting/#loops). This will iterate in the order the pairs were
inserted / declared.

# Example
```example
#let dict = (
  name: "Typst",
  born: 2019,
)

#dict.name \
#(dict.launch = 20)
#dict.len() \
#dict.keys() \
#dict.values() \
#dict.at("born") \
#dict.insert("city", "Berlin ")
#("name" in dict)
```

## Constructor

### `dictionary`

Converts a value into a dictionary.

Note that this function is only intended for conversion of a
dictionary-like value to a dictionary, not for creation of a dictionary
from individual pairs. Use the dictionary syntax `(key: value)` instead.




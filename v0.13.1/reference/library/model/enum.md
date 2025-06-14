# Numbered List

## `enum`

A numbered list.

Displays a sequence of items vertically and numbers them consecutively.

# Example
```example
Automatically numbered:
+ Preparations
+ Analysis
+ Conclusions

Manually numbered:
2. What is the first step?
5. I am confused.
+  Moving on ...

Multiple lines:
+ This enum item has multiple
  lines because the next line
  is indented.

Function call.
#enum[First][Second]
```

You can easily switch all your enumerations to a different numbering style
with a set rule.
```example
#set enum(numbering: "a)")

+ Starting off ...
+ Don't forget step two
```

You can also use [`enum.item`]($enum.item) to programmatically customize the
number of each item in the enumeration:

```example
#enum(
  enum.item(1)[First step],
  enum.item(5)[Fifth step],
  enum.item(10)[Tenth step]
)
```

# Syntax
This functions also has dedicated syntax:

- Starting a line with a plus sign creates an automatically numbered
  enumeration item.
- Starting a line with a number followed by a dot creates an explicitly
  numbered enumeration item.

Enumeration items can contain multiple paragraphs and other block-level
content. All content that is indented more than an item's marker becomes
part of that item.

## Parameters

### tight 

Defines the default [spacing]($enum.spacing) of the enumeration. If it
is `{false}`, the items are spaced apart with
[paragraph spacing]($par.spacing). If it is `{true}`, they use
[paragraph leading]($par.leading) instead. This makes the list more
compact, which can look better if the items are short.

In markup mode, the value of this parameter is determined based on
whether items are separated with a blank line. If items directly follow
each other, this is set to `{true}`; if items are separated by a blank
line, this is set to `{false}`. The markup-defined tightness cannot be
overridden with set rules.



### numbering 

How to number the enumeration. Accepts a
[numbering pattern or function]($numbering).

If the numbering pattern contains multiple counting symbols, they apply
to nested enums. If given a function, the function receives one argument
if `full` is `{false}` and multiple arguments if `full` is `{true}`.



### start 

Which number to start the enumeration with.



### full 

Whether to display the full numbering, including the numbers of
all parent enumerations.




### reversed 

Whether to reverse the numbering for this enumeration.



### indent 

The indentation of each item.

### body-indent 

The space between the numbering and the body of each item.

### spacing 

The spacing between the items of the enumeration.

If set to `{auto}`, uses paragraph [`leading`]($par.leading) for tight
enumerations and paragraph [`spacing`]($par.spacing) for wide
(non-tight) enumerations.

### number-align 

The alignment that enum numbers should have.

By default, this is set to `{end + top}`, which aligns enum numbers
towards end of the current text direction (in left-to-right script,
for example, this is the same as `{right}`) and at the top of the line.
The choice of `{end}` for horizontal alignment of enum numbers is
usually preferred over `{start}`, as numbers then grow away from the
text instead of towards it, avoiding certain visual issues. This option
lets you override this behaviour, however. (Also to note is that the
[unordered list]($list) uses a different method for this, by giving the
`marker` content an alignment directly.).



### children *(required)*

The numbered list's items.

When using the enum syntax, adjacent items are automatically collected
into enumerations, even through constructs like for loops.



## Returns

- content


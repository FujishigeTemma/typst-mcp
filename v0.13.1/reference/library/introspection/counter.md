# Counter

Counts through pages, elements, and more.

With the counter function, you can access and modify counters for pages,
headings, figures, and more. Moreover, you can define custom counters for
other things you want to count.

Since counters change throughout the course of the document, their current
value is _contextual._ It is recommended to read the chapter on [context]
before continuing here.

# Accessing a counter { #accessing }
To access the raw value of a counter, we can use the [`get`]($counter.get)
function. This function returns an [array]: Counters can have multiple
levels (in the case of headings for sections, subsections, and so on), and
each item in the array corresponds to one level.

```example
#set heading(numbering: "1.")

= Introduction
Raw value of heading counter is
#context counter(heading).get()
```

# Displaying a counter { #displaying }
Often, we want to display the value of a counter in a more human-readable
way. To do that, we can call the [`display`]($counter.display) function on
the counter. This function retrieves the current counter value and formats
it either with a provided or with an automatically inferred [numbering].

```example
#set heading(numbering: "1.")

= Introduction
Some text here.

= Background
The current value is: #context {
  counter(heading).display()
}

Or in roman numerals: #context {
  counter(heading).display("I")
}
```

# Modifying a counter { #modifying }
To modify a counter, you can use the `step` and `update` methods:

- The `step` method increases the value of the counter by one. Because
  counters can have multiple levels , it optionally takes a `level`
  argument. If given, the counter steps at the given depth.

- The `update` method allows you to arbitrarily modify the counter. In its
  basic form, you give it an integer (or an array for multiple levels). For
  more flexibility, you can instead also give it a function that receives
  the current value and returns a new value.

The heading counter is stepped before the heading is displayed, so
`Analysis` gets the number seven even though the counter is at six after the
second update.

```example
#set heading(numbering: "1.")

= Introduction
#counter(heading).step()

= Background
#counter(heading).update(3)
#counter(heading).update(n => n * 2)

= Analysis
Let's skip 7.1.
#counter(heading).step(level: 2)

== Analysis
Still at #context {
  counter(heading).display()
}
```

# Page counter
The page counter is special. It is automatically stepped at each pagebreak.
But like other counters, you can also step it manually. For example, you
could have Roman page numbers for your preface, then switch to Arabic page
numbers for your main content and reset the page counter to one.

```example
>>> #set page(
>>>   height: 100pt,
>>>   margin: (bottom: 24pt, rest: 16pt),
>>> )
#set page(numbering: "(i)")

= Preface
The preface is numbered with
roman numerals.

#set page(numbering: "1 / 1")
#counter(page).update(1)

= Main text
Here, the counter is reset to one.
We also display both the current
page and total number of pages in
Arabic numbers.
```

# Custom counters
To define your own counter, call the `counter` function with a string as a
key. This key identifies the counter globally.

```example
#let mine = counter("mycounter")
#context mine.display() \
#mine.step()
#context mine.display() \
#mine.update(c => c * 3)
#context mine.display()
```

# How to step
When you define and use a custom counter, in general, you should first step
the counter and then display it. This way, the stepping behaviour of a
counter can depend on the element it is stepped for. If you were writing a
counter for, let's say, theorems, your theorem's definition would thus first
include the counter step and only then display the counter and the theorem's
contents.

```example
#let c = counter("theorem")
#let theorem(it) = block[
  #c.step()
  *Theorem #context c.display():*
  #it
]

#theorem[$1 = 1$]
#theorem[$2 < 3$]
```

The rationale behind this is best explained on the example of the heading
counter: An update to the heading counter depends on the heading's level. By
stepping directly before the heading, we can correctly step from `1` to
`1.1` when encountering a level 2 heading. If we were to step after the
heading, we wouldn't know what to step to.

Because counters should always be stepped before the elements they count,
they always start at zero. This way, they are at one for the first display
(which happens after the first step).

# Time travel
Counters can travel through time! You can find out the final value of the
counter before it is reached and even determine what the value was at any
particular location in the document.

```example
#let mine = counter("mycounter")

= Values
#context [
  Value here: #mine.get() \
  At intro: #mine.at(<intro>) \
  Final value: #mine.final()
]

#mine.update(n => n + 3)

= Introduction <intro>
#lorem(10)

#mine.step()
#mine.step()
```

# Other kinds of state { #other-state }
The `counter` type is closely related to [state] type. Read its
documentation for more details on state management in Typst and why it
doesn't just use normal variables for counters.

## Constructor

### `counter`

Create a new counter identified by a key.


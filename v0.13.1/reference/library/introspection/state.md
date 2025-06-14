# State

Manages stateful parts of your document.

Let's say you have some computations in your document and want to remember
the result of your last computation to use it in the next one. You might try
something similar to the code below and expect it to output 10, 13, 26, and
21. However this **does not work** in Typst. If you test this code, you will
see that Typst complains with the following error message: _Variables from
outside the function are read-only and cannot be modified._

```typ
// This doesn't work!
#let x = 0
#let compute(expr) = {
  x = eval(
    expr.replace("x", str(x))
  )
  [New value is #x. ]
}

#compute("10") \
#compute("x + 3") \
#compute("x * 2") \
#compute("x - 5")
```

# State and document markup { #state-and-markup }
Why does it do that? Because, in general, this kind of computation with side
effects is problematic in document markup and Typst is upfront about that.
For the results to make sense, the computation must proceed in the same
order in which the results will be laid out in the document. In our simple
example, that's the case, but in general it might not be.

Let's look at a slightly different, but similar kind of state: The heading
numbering. We want to increase the heading counter at each heading. Easy
enough, right? Just add one. Well, it's not that simple. Consider the
following example:

```example
#set heading(numbering: "1.")
#let template(body) = [
  = Outline
  ...
  #body
]

#show: template

= Introduction
...
```

Here, Typst first processes the body of the document after the show rule,
sees the `Introduction` heading, then passes the resulting content to the
`template` function and only then sees the `Outline`. Just counting up would
number the `Introduction` with `1` and the `Outline` with `2`.

# Managing state in Typst { #state-in-typst }
So what do we do instead? We use Typst's state management system. Calling
the `state` function with an identifying string key and an optional initial
value gives you a state value which exposes a few functions. The two most
important ones are `get` and `update`:

- The [`get`]($state.get) function retrieves the current value of the state.
  Because the value can vary over the course of the document, it is a
  _contextual_ function that can only be used when [context]($context) is
  available.

- The [`update`]($state.update) function modifies the state. You can give it
  any value. If given a non-function value, it sets the state to that value.
  If given a function, that function receives the previous state and has to
  return the new state.

Our initial example would now look like this:

```example
#let s = state("x", 0)
#let compute(expr) = [
  #s.update(x =>
    eval(expr.replace("x", str(x)))
  )
  New value is #context s.get().
]

#compute("10") \
#compute("x + 3") \
#compute("x * 2") \
#compute("x - 5")
```

State managed by Typst is always updated in layout order, not in evaluation
order. The `update` method returns content and its effect occurs at the
position where the returned content is inserted into the document.

As a result, we can now also store some of the computations in variables,
but they still show the correct results:

```example
>>> #let s = state("x", 0)
>>> #let compute(expr) = [
>>>   #s.update(x =>
>>>     eval(expr.replace("x", str(x)))
>>>   )
>>>   New value is #context s.get().
>>> ]
<<< ...

#let more = [
  #compute("x * 2") \
  #compute("x - 5")
]

#compute("10") \
#compute("x + 3") \
#more
```

This example is of course a bit silly, but in practice this is often exactly
what you want! A good example are heading counters, which is why Typst's
[counting system]($counter) is very similar to its state system.

# Time Travel
By using Typst's state management system you also get time travel
capabilities! We can find out what the value of the state will be at any
position in the document from anywhere else. In particular, the `at` method
gives us the value of the state at any particular location and the `final`
methods gives us the value of the state at the end of the document.

```example
>>> #let s = state("x", 0)
>>> #let compute(expr) = [
>>>   #s.update(x => {
>>>     eval(expr.replace("x", str(x)))
>>>   })
>>>   New value is #context s.get().
>>> ]
<<< ...

Value at `<here>` is
#context s.at(<here>)

#compute("10") \
#compute("x + 3") \
*Here.* <here> \
#compute("x * 2") \
#compute("x - 5")
```

# A word of caution { #caution }
To resolve the values of all states, Typst evaluates parts of your code
multiple times. However, there is no guarantee that your state manipulation
can actually be completely resolved.

For instance, if you generate state updates depending on the final value of
a state, the results might never converge. The example below illustrates
this. We initialize our state with `1` and then update it to its own final
value plus 1. So it should be `2`, but then its final value is `2`, so it
should be `3`, and so on. This example displays a finite value because Typst
simply gives up after a few attempts.

```example
// This is bad!
#let s = state("x", 1)
#context s.update(s.final() + 1)
#context s.get()
```

In general, you should try not to generate state updates from within context
expressions. If possible, try to express your updates as non-contextual
values or functions that compute the new value from the previous value.
Sometimes, it cannot be helped, but in those cases it is up to you to ensure
that the result converges.

## Constructor

### `state`

Create a new state identified by a key.


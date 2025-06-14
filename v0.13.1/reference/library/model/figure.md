# Figure

## `figure`

A figure with an optional caption.

Automatically detects its kind to select the correct counting track. For
example, figures containing images will be numbered separately from figures
containing tables.

# Examples
The example below shows a basic figure with an image:
```example
@glacier shows a glacier. Glaciers
are complex systems.

#figure(
  image("glacier.jpg", width: 80%),
  caption: [A curious figure.],
) <glacier>
```

You can also insert [tables]($table) into figures to give them a caption.
The figure will detect this and automatically use a separate counter.

```example
#figure(
  table(
    columns: 4,
    [t], [1], [2], [3],
    [y], [0.3s], [0.4s], [0.8s],
  ),
  caption: [Timing results],
)
```

This behaviour can be overridden by explicitly specifying the figure's
`kind`. All figures of the same kind share a common counter.

# Figure behaviour
By default, figures are placed within the flow of content. To make them
float to the top or bottom of the page, you can use the
[`placement`]($figure.placement) argument.

If your figure is too large and its contents are breakable across pages
(e.g. if it contains a large table), then you can make the figure itself
breakable across pages as well with this show rule:
```typ
#show figure: set block(breakable: true)
```

See the [block]($block.breakable) documentation for more information about
breakable and non-breakable blocks.

# Caption customization
You can modify the appearance of the figure's caption with its associated
[`caption`]($figure.caption) function. In the example below, we emphasize
all captions:

```example
#show figure.caption: emph

#figure(
  rect[Hello],
  caption: [I am emphasized!],
)
```

By using a [`where`]($function.where) selector, we can scope such rules to
specific kinds of figures. For example, to position the caption above
tables, but keep it below for all other kinds of figures, we could write the
following show-set rule:

```example
#show figure.where(
  kind: table
): set figure.caption(position: top)

#figure(
  table(columns: 2)[A][B][C][D],
  caption: [I'm up here],
)
```

## Parameters

### body *(required)*

The content of the figure. Often, an [image].

### placement 

The figure's placement on the page.

- `{none}`: The figure stays in-flow exactly where it was specified
  like other content.
- `{auto}`: The figure picks `{top}` or `{bottom}` depending on which
  is closer.
- `{top}`: The figure floats to the top of the page.
- `{bottom}`: The figure floats to the bottom of the page.

The gap between the main flow content and the floating figure is
controlled by the [`clearance`]($place.clearance) argument on the
`place` function.



### scope 

Relative to which containing scope the figure is placed.

Set this to `{"parent"}` to create a full-width figure in a two-column
document.

Has no effect if `placement` is `{none}`.



### caption 

The figure's caption.

### kind 

The kind of figure this is.

All figures of the same kind share a common counter.

If set to `{auto}`, the figure will try to automatically determine its
kind based on the type of its body. Automatically detected kinds are
[tables]($table) and [code]($raw). In other cases, the inferred kind is
that of an [image].

Setting this to something other than `{auto}` will override the
automatic detection. This can be useful if
- you wish to create a custom figure type that is not an
  [image], a [table] or [code]($raw),
- you want to force the figure to use a specific counter regardless of
  its content.

You can set the kind to be an element function or a string. If you set
it to an element function other than [`{table}`]($table), [`{raw}`](raw)
or [`{image}`](image), you will need to manually specify the figure's
supplement.



### supplement 

The figure's supplement.

If set to `{auto}`, the figure will try to automatically determine the
correct supplement based on the `kind` and the active
[text language]($text.lang). If you are using a custom figure type, you
will need to manually specify the supplement.

If a function is specified, it is passed the first descendant of the
specified `kind` (typically, the figure's body) and should return
content.



### numbering 

How to number the figure. Accepts a
[numbering pattern or function]($numbering).

### gap 

The vertical gap between the body and caption.

### outlined 

Whether the figure should appear in an [`outline`] of figures.

## Returns

- content


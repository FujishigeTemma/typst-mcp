# Polygon

## `polygon`

A closed polygon.

The polygon is defined by its corner points and is closed automatically.

# Example
```example
#polygon(
  fill: blue.lighten(80%),
  stroke: blue,
  (20%, 0pt),
  (60%, 0pt),
  (80%, 2cm),
  (0%,  2cm),
)
```

## Parameters

### fill 

How to fill the polygon.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.

### fill-rule 

The drawing rule used to fill the polygon.

See the [curve documentation]($curve.fill-rule) for an example.

### stroke 

How to [stroke] the polygon. This can be:

Can be set to  `{none}` to disable the stroke or to `{auto}` for a
stroke of `{1pt}` black if and if only if no fill is given.

### vertices *(required)*

The vertices of the polygon. Each point is specified as an array of two
[relative lengths]($relative).

## Returns

- content


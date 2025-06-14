# Path

## `path`

A path through a list of points, connected by Bézier curves.

# Example
```example
#path(
  fill: blue.lighten(80%),
  stroke: blue,
  closed: true,
  (0pt, 50pt),
  (100%, 50pt),
  ((50%, 0pt), (40pt, 0pt)),
)
```

## Parameters

### fill 

How to fill the path.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.

### fill-rule 

The drawing rule used to fill the path.



### stroke 

How to [stroke] the path. This can be:

Can be set to  `{none}` to disable the stroke or to `{auto}` for a
stroke of `{1pt}` black if and if only if no fill is given.

### closed 

Whether to close this path with one last Bézier curve. This curve will
take into account the adjacent control points. If you want to close
with a straight line, simply add one last point that's the same as the
start point.

### vertices *(required)*

The vertices of the path.

Each vertex can be defined in 3 ways:

- A regular point, as given to the [`line`] or [`polygon`] function.
- An array of two points, the first being the vertex and the second
  being the control point. The control point is expressed relative to
  the vertex and is mirrored to get the second control point. The given
  control point is the one that affects the curve coming _into_ this
  vertex (even for the first point). The mirrored control point affects
  the curve going out of this vertex.
- An array of three points, the first being the vertex and the next
  being the control points (control point for curves coming in and out,
  respectively).

## Returns

- content


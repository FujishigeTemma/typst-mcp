# Curve

## `curve`

A curve consisting of movements, lines, and Bézier segments.

At any point in time, there is a conceptual pen or cursor.
- Move elements move the cursor without drawing.
- Line/Quadratic/Cubic elements draw a segment from the cursor to a new
  position, potentially with control point for a Bézier curve.
- Close elements draw a straight or smooth line back to the start of the
  curve or the latest preceding move segment.

For layout purposes, the bounding box of the curve is a tight rectangle
containing all segments as well as the point `{(0pt, 0pt)}`.

Positions may be specified absolutely (i.e. relatively to `{(0pt, 0pt)}`),
or relative to the current pen/cursor position, that is, the position where
the previous segment ended.

Bézier curve control points can be skipped by passing `{none}` or
automatically mirrored from the preceding segment by passing `{auto}`.

# Example
```example
#curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(none, (90pt, 0pt), (50pt, 0pt)),
  curve.close(),
)
```

## Parameters

### fill 

How to fill the curve.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.

### fill-rule 

The drawing rule used to fill the curve.



### stroke 

How to [stroke] the curve. This can be:

Can be set to `{none}` to disable the stroke or to `{auto}` for a
stroke of `{1pt}` black if and if only if no fill is given.



### components *(required)*

The components of the curve, in the form of moves, line and Bézier
segment, and closes.

## Returns

- content


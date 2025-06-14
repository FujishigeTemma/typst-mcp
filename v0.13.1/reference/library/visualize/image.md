# Image

## `image`

A raster or vector graphic.

You can wrap the image in a [`figure`] to give it a number and caption.

Like most elements, images are _block-level_ by default and thus do not
integrate themselves into adjacent paragraphs. To force an image to become
inline, put it into a [`box`].

# Example
```example
#figure(
  image("molecular.jpg", width: 80%),
  caption: [
    A step in the molecular testing
    pipeline of our lab.
  ],
)
```

## Parameters

### source *(required)*

A [path]($syntax/#paths) to an image file or raw bytes making up an
image in one of the supported [formats]($image.format).

Bytes can be used to specify raw pixel data in a row-major,
left-to-right, top-to-bottom format.



### format 

The image's format.

By default, the format is detected automatically. Typically, you thus
only need to specify this when providing raw bytes as the
[`source`]($image.source) (even then, Typst will try to figure out the
format automatically, but that's not always possible).

Supported formats are `{"png"}`, `{"jpg"}`, `{"gif"}`, `{"svg"}`,
`{"webp"}` as well as raw pixel data. Embedding PDFs as images is
[not currently supported](https://github.com/typst/typst/issues/145).

When providing raw pixel data as the `source`, you must specify a
dictionary with the following keys as the `format`:
- `encoding` ([str]): The encoding of the pixel data. One of:
  - `{"rgb8"}` (three 8-bit channels: red, green, blue)
  - `{"rgba8"}` (four 8-bit channels: red, green, blue, alpha)
  - `{"luma8"}` (one 8-bit channel)
  - `{"lumaa8"}` (two 8-bit channels: luma and alpha)
- `width` ([int]): The pixel width of the image.
- `height` ([int]): The pixel height of the image.

The pixel width multiplied by the height multiplied by the channel count
for the specified encoding must then match the `source` data.



### width 

The width of the image.

### height 

The height of the image.

### alt 

A text describing the image.

### fit 

How the image should adjust itself to a given area (the area is defined
by the `width` and `height` fields). Note that `fit` doesn't visually
change anything if the area's aspect ratio is the same as the image's
one.



### scaling 

A hint to viewers how they should scale the image.

When set to `{auto}`, the default is left up to the viewer. For PNG
export, Typst will default to smooth scaling, like most PDF and SVG
viewers.

_Note:_ The exact look may differ across PDF viewers.

### icc 

An ICC profile for the image.

ICC profiles define how to interpret the colors in an image. When set
to `{auto}`, Typst will try to extract an ICC profile from the image.

## Returns

- content


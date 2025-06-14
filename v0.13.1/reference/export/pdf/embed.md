# Embed

## `embed`

A file that will be embedded into the output PDF.

This can be used to distribute additional files that are related to the PDF
within it. PDF readers will display the files in a file listing.

Some international standards use this mechanism to embed machine-readable
data (e.g., ZUGFeRD/Factur-X for invoices) that mirrors the visual content
of the PDF.

# Example
```typ
#pdf.embed(
  "experiment.csv",
  relationship: "supplement",
  mime-type: "text/csv",
  description: "Raw Oxygen readings from the Arctic experiment",
)
```

# Notes
- This element is ignored if exporting to a format other than PDF.
- File embeddings are not currently supported for PDF/A-2, even if the
  embedded file conforms to PDF/A-1 or PDF/A-2.

## Parameters

### path *(required)*

The [path]($syntax/#paths) of the file to be embedded.

Must always be specified, but is only read from if no data is provided
in the following argument.

### data *(required)*

Raw file data, optionally.

If omitted, the data is read from the specified path.

### relationship 

The relationship of the embedded file to the document.

Ignored if export doesn't target PDF/A-3.

### mime-type 

The MIME type of the embedded file.

### description 

A description for the embedded file.

## Returns

- content


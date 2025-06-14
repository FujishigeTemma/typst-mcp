# Direction

The four directions into which content can be laid out.

 Possible values are:
- `{ltr}`: Left to right.
- `{rtl}`: Right to left.
- `{ttb}`: Top to bottom.
- `{btt}`: Bottom to top.

These values are available globally and
also in the direction type's scope, so you can write either of the following
two:
```example
#stack(dir: rtl)[A][B][C]
#stack(dir: direction.rtl)[A][B][C]
```


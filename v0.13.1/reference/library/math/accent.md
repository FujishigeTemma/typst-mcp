# Accent

## `accent`

Attaches an accent to a base.

# Example
```example
$grave(a) = accent(a, `)$ \
$arrow(a) = accent(a, arrow)$ \
$tilde(a) = accent(a, \u{0303})$
```

## Parameters

### base *(required)*

The base to which the accent is applied. May consist of multiple
letters.



### accent *(required)*

The accent to apply to the base.

Supported accents include:

| Accent        | Name            | Codepoint |
| ------------- | --------------- | --------- |
| Grave         | `grave`         | <code>&DiacriticalGrave;</code> |
| Acute         | `acute`         | `´`       |
| Circumflex    | `hat`           | `^`       |
| Tilde         | `tilde`         | `~`       |
| Macron        | `macron`        | `¯`       |
| Dash          | `dash`          | `‾`       |
| Breve         | `breve`         | `˘`       |
| Dot           | `dot`           | `.`       |
| Double dot, Diaeresis | `dot.double`, `diaer` | `¨` |
| Triple dot    | `dot.triple`    | <code>&tdot;</code> |
| Quadruple dot | `dot.quad`      | <code>&DotDot;</code> |
| Circle        | `circle`        | `∘`       |
| Double acute  | `acute.double`  | `˝`       |
| Caron         | `caron`         | `ˇ`       |
| Right arrow   | `arrow`, `->`   | `→`       |
| Left arrow    | `arrow.l`, `<-` | `←`       |
| Left/Right arrow | `arrow.l.r`  | `↔`       |
| Right harpoon | `harpoon`       | `⇀`       |
| Left harpoon  | `harpoon.lt`    | `↼`       |

### size 

The size of the accent, relative to the width of the base.



### dotless 

Whether to remove the dot on top of lowercase i and j when adding a top
accent.

This enables the `dtls` OpenType feature.



## Returns

- content


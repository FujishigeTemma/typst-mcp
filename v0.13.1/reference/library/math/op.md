# Text Operator

## `op`

A text operator in an equation.

# Example
```example
$ tan x = (sin x)/(cos x) $
$ op("custom",
     limits: #true)_(n->oo) n $
```

# Predefined Operators { #predefined }
Typst predefines the operators `arccos`, `arcsin`, `arctan`, `arg`, `cos`,
`cosh`, `cot`, `coth`, `csc`, `csch`, `ctg`, `deg`, `det`, `dim`, `exp`,
`gcd`, `lcm`, `hom`, `id`, `im`, `inf`, `ker`, `lg`, `lim`, `liminf`,
`limsup`, `ln`, `log`, `max`, `min`, `mod`, `Pr`, `sec`, `sech`, `sin`,
`sinc`, `sinh`, `sup`, `tan`, `tanh`, `tg` and `tr`.

## Parameters

### text *(required)*

The operator's text.

### limits 

Whether the operator should show attachments as limits in display mode.

## Returns

- content


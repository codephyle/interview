## Formatting

No need for parentheses. Spacing implies the precedence
```go
    x<<8 + y<<16 
```

## Semicolon insertion rule

If the last token before a newline is an identifier (which includes words like int and float64), a basic literal such as a number or string constant, or one of the tokens
```go
    break continue fallthrough return ++ -- ) }
```
the lexer always inserts a semicolon after the token

## looping

```go
for { }

sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
```
looping over an array, slice, string, or map, or reading from a channel

```go
for k, v := range langs {

}

for k := range langs {
    
}
```
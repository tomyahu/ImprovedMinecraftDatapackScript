# Improved Minecraft Datapack Script

An extension for the minecraft datapack script language that
makes it easier to work with variables.

## Requirements

* Python 3

## How do I use this?

You can write your files using the syntax we created and
translate them to the vanilla minecraft datapack language
by running:

```
$ main.py <path_to_your_file> <export_path>
```

This will create a file in `<export_path>` with the code translated.

## Features
### Variable definition and operation

We can define a variable `a` with the value of `1` like this:

```var a 1```

We can also modify its values like this

```
op a += 3
op a -= 1
op a *= 5
```

We can add the value of another variable `b` to `a` like this:

```
op a += b
```

### If statements

Ok you may really like this:

```
if a < b
time set day
end
```

You can put any minecraft command you like inside the if
statement and all of them will be executed only if the
condition is satisfied.

## Features Planned
* For and While loops
* Functions with arguments

Check the example.imcfunction file to check how all the
new commands work and all the operations that exist.
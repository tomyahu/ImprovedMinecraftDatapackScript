# Improved Minecraft Datapack Script

An extension for the minecraft datapack script language that
makes it easier to work with variables.

## Requirements

* Python 3

## How do I use this?

You can write your datapack using the syntax we created and
by running:

```
$ main.py <path_to_your_file>
```

The software will translate the datapack to the vanilla
minecraft language and save it in a zip named
`<path_to_your_file>_out.zip`.

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

If statements syntax is as follows:

```
if a < b
	time set day
endif
```

You can put any minecraft command you like inside the if
statement and all of them will be executed only if the
condition is satisfied.

### While statements

While statements work the same as ifs. You put the
boolean experssion in the first line and you end
them with `endwhile`:

```
while a < b
	time set day
endwhile
```

# Future plans
Currently I'm working on an executable version so it is
easy to use it.

There are no more future plans for this repository. If there's
interest I may continue to develop it, but for now I'm
happy with how it turned out!

Check the example.mcfunction file to check how all the
new commands work and all the operations that exist.
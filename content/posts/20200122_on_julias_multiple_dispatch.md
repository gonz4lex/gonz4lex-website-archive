title: On Julia's Multiple Dispatch
date: 2020-1-22 11:03
category: data science
tags: julia
slug: on-julias-multiple-dispatch
author: Alex Gonzalez
summary: Multiple dispatch is one of the key features of Julia, and makes your code blazing fast thanks to its typed functions.
header_cover: images/pint-of-api.jpg
status: draft


### Code

```julia

function printf(x::String)
    println("Calling method for String for value $x")
end

function printf(x::Float64)
    println("Calling method for Float64 for value $x")
end

methods(f) 

printf("Julia")
printf(1.0)
```

You can also examine the methods of the `+` operator:

```
methods(+) # 166 methods for generic function "+": [...]
```

One use of this would be to enable the `+` operator to do string concatenation, much like in Python.

```julia
import Base.+

function +(x::String, y::String)
    println(x * y)
end
```

Note how the output returns `+ (generic function with 167 methods)`, and the new method has been added to our operator. You can also check it with `methods(+)`.

Now, the following code should work:

```

```
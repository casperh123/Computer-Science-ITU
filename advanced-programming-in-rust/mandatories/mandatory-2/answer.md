# Mandatory 1

## Exercise 1

### 1) 

A generic type parameter, is a type parameter that can be substituted with 
with concrete types, that satisfies the generic type parameters bounds.
It allows one to generalize functions and other constructs to a broader range of inputs.

### 2)

A trait defines shared functionality. Very similar to interfaces in other langugages, they
provide a contract for the consumer, such that one can be sure that a construct exposes certain functions and features. 

## Exercise 2

### 1)

Observe the following code:

```rust
fn most_frequent<T>(items: &[T]) -> &T {
    let mut best = &items[0];
    let mut best_count = 0;
    
    for a in items {
        let mut count = 0;
        
        for b in items {
            if a == b {
                count += 1;
            }
        }

        if count > best_count {
            best = a;
            best_count = count;
        }
    }
    best
}
```

The code does not compile, because the type parameter `T` does not provide a
acomparison operator `<, >`. It needs to implement the trait `PartialOrder`.

### 2)

Observe the fixed version implenting the PartialOrd:

```rust
fn most_frequent<T: PartialOrd>(items: &[T]) -> &T {
    let mut best = &items[0];
    let mut best_count = 0;
    
    for a in items {
        let mut count = 0;
        
        for b in items {
            if a == b {
                count += 1;
            }
        }   

        if count > best_count {
            best = a;
            best_count = count;
        }
    }
    best
}
``` 

## Exercise 3

### 1)

Observe the structs `Rectangle` and `Circle`. 

```rust
struct Rectangle {
    width: f64,
    height: f64
}

struct Circle {
    radius: f64,
}
``` 

### 2)

Observe the Area implementation for `Rectangle` and `Circle`:

```rust
impl Area for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

impl Area for Circle {
    fn area(&self) -> f64 {
        let circumference = 2.0 * self.radius;
        
        0.5 * (circumference * 3.14) * self.radius
    }
}
```

### 3)

Observe the function `print_area`:

```rust
fn print_area<T: Area>(shape: &T) {
    println!("Area: {}", shape.area())
}
```

The function works for both types, since it requires the parameters to implement the `Area` trait.

## Exercise 4

```rust
fn first_word<’a>(s: &’a str) -> &’a str {
    for (i, &b) in s.as_bytes().iter().enumerate() {
        if b == b’ ’ {
            return &s[..i];
        }
    }
    s
}
```

### 1)

`'a` here is the lifetime of the input and the output of the function. This means that the output has the same lifetime as the 
function argument.

### 2)

The output cannot outlive the lifetime of s, because they are the exact same lifetime. The parameter `s` will live exactly 
as long as the output of the function.

### 3)

A valid call:

```rust
fn main() {
    let text = "Hej Marco!";
    let first = first_word(&text);

    println!("{}", first);
}
```

A invalid call:
I tried something like this, but.....

```rust
fn main() {
    let input = "Hej Marco!";

    {
        let output = first_word(input);

        println!("{]", &output);
    }
}
```

that stille compiled and ran. So good question! Couldn't quite think of an invalid
scenario! :(

## Exercise 5

### 1)
#### 1.1)

Observe the following function:

```rust
fn pick(x: &str, y: &str) -> &str {
    if x.len() >= y.len() { x } else { y }
}
```
    
The borrow checker does not know the lifetime of the returned string, since
it can either be `x` or `y`. We need to add explicit lifetimes to the arguments and 
return type.

#### 1.2)

Observe the following function:

```rust
fn head(s: &str) -> &str {
    &s[..1]
}
```

This compiles fine. Since the argument is borrowed, the compiler can safely infer the liftime of s.

#### 1.3)

Observe the following function:

```rust
fn foo() -> &str {
    "hello"
}
```
This does not compile, since the compiler cant infer "hello"'s lifetime

### 2)

Observe the corrected pick:

```rust
fn pick<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() { x } else { y }
}
```

### 3)

Observe `head`:

```rust
fn head(s: &str) -> &str {
    &s[..1]
}
```

By rule one, `head` has one input parameter, and thus lifetime parameter `a`.
By rule two, 'head' has one input parameter, and thus the output parameter also has `a`.
Rule three is not applicable, since there is only one parameter. 

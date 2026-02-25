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

## Exercise 5

# Mandatory 3

## Exercise 1

Observe the following program:

```rust
fn main() {
    let suffix = String::from("!!!");
    
    let add_suffix = |s: &str| -> String {
        format!("{s}{suffix}")
    };
    
    let result = add_suffix("hello");
    println!("{result}");
}
```

### 1)

Observe the solution to the problem:

```rust
fn main() {
    let suffix = String::from("!!!");
    
    let result = add_suffix(&suffix, "hello");
    println!("{result}");
}

fn add_suffix(suffix: &str, s: &str) -> String {
    format!("{s}{suffix}")
}
```

### 2)

This works because closures can capture the variables from the scope that they are used in.

### 3)

The function must take additional parameters, because it can only reference variables within it's own scope.
Thus variables from outside the function must be passed in as arguments to the funtion.

### 4)

Main owns the string. Format creates a brand new string, and transfers ownership to the main method on return.

## Exercise 2

Observe the program:

```rust
fn main() {
    let threshold = 10;
    let numbers = vec![3, 7, 12, 18, 5];

    let count = numbers
        .iter()
        .filter(|x| **x > threshold)
        .count();

    println!("{count}");
}
```

### 1)

The program will not compile with a named function, since filter only passes the iterator as an argument to the function.
The named function would not have treshold in it's scope, and thus would declare it an unknown variable. HOWEVER, one
could use a named function inside the filter closure, and pass both x and threshold, but that would defeat the purpose 
for this length of function.

### 2)

The `Fn` trait allows this function to compile. Since it is not moving variables out of the environment, and does not mutate them,
it can be called multiple times.

The second property of closures that allow this to compile, is the fact that they an capture variables from their scope. Else
threshold wouldn't be accessible from within the closure. Same issue with our named function.

## Exercise 3

Observe the following program:
```rust
fn main() {
    let v = vec![1, 2, 3];
    
    v.iter()
        .map(|x| {
        println!("mapping {x}");
        x + 1
    });
    
    println!("done");
}
```

### 1)

The program outputs "done". It does this, since iterators are lazily evaluated. The result of v.iter() with the given function
will not take effect until it consumed which, in this case, it is not.

### 2)

```rust
fn main() {
    let v = vec![1, 2, 3];
    
    v.iter()
        .map(|x| {
        println!("mapping {x}");
        x + 1
    }).for_each(|_| {});
    
    println!("done");
}
```

`for_each` forces the evaluation of the iterator, since it consumes the iterator on each call.

## Exercise 4

Consider the following program: 

```rust


fn main() {
    let s = String::from("hello");
    let mut counter = 0;
    
    let c1 = || println!("{s}");
    let c2 = || counter += 1;
    let c3 = || drop(s);
}
```

### 1)

- `let c1 = || println!("{s}");` implements `Fn`. It does not mutate the captured value
and it does not move the captured value out of it's body.
- `let c2 = || counter += 1;` implements `FnMut`, since the captured variable counter is mutable.
- `let c3 = || drop(s);` implements `FnOnce` since the `drop` function can only be executed once
on the variabel `s`. s is moved out of the body of the closure.


### 2)

`let c1 = || println!("{s}");` can be passed to `unwrap_or_else`, since it implements the `FnOnce` 
trait.

`let c2 = || counter += 1;` can be passed to `sort_by_key` since it implements `FnMut`;

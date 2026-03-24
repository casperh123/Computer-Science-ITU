# Mandatory 4

Observe the following code:

```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    value: i32,
    edges: RefCell<Vec<Rc<Node>>>,
}
```

### 1)

Observe the following implementation:

```rust
impl Node {
    fn new(value: i32) -> Rc<Node> {
        let node = Node {
            value,
            edges: RefCell::new(vec![])
        };

        Rc::new(node)
    }

    fn connect(a: &Rc<Node>, b: &Rc<Node>) {
        let mut a_edges = a.edges.borrow_mut();
        let mut b_edges = b.edges.borrow_mut();
        
        a_edges.push(Rc::clone(&b));
        b_edges.push(Rc::clone(&a));
    }
}
```

### 2)

Observe the following program:

```rust
fn main() {
    let a = Node::new(0);
    let b = Node::new(1);
    let c = Node::new(2);
    let d = Node::new(3);

    Node::connect(&a, &b);
    Node::connect(&a, &c);
    Node::connect(&b, &c);
    Node::connect(&c, &d)
}
```

### 3)

```rust
fn main() {
    let a = Node::new(0);
    let b = Node::new(1);
    let c = Node::new(2);
    let d = Node::new(3);

    Node::connect(&a, &b);
    Node::connect(&a, &c);
    Node::connect(&b, &c);
    Node::connect(&c, &d);

    let mut visited: Vec<Rc<Node>> = vec![];
    let mut frontier: Vec<Rc<Node>> = vec![Rc::clone(&a)];

    while let Some(node) = frontier.pop() {
        if visited.iter().any(|n| Rc::ptr_eq(n, &node)) {
            continue;
        }

        println!("{}", &node.value);
        visited.push(Rc::clone(&node));

        for new_node in node.edges.borrow().iter() {
            frontier.push(Rc::clone(&new_node));
        }
    }  
}
```

### 4)

Observe the following print:

`value: 0, Strong reference count: 4
value: 2, Strong reference count: 5
value: 3, Strong reference count: 3
value: 1, Strong reference count: 5`

The strong reference count is the amount of pointers to that node.
In general, there is a reference in the original `let binding`, then one in the frontier,
one in visited, and then one in each connection.

### 5)

Observe the updated code:

```rust
fn main() {
    let a = Node::new(0);
    let b = Node::new(1);
    let c = Node::new(2);
    let d = Node::new(3); 

    Node::connect(&a, &b);
    Node::connect(&a, &c);
    Node::connect(&b, &c);
    Node::connect(&c, &d);
    Node::connect(&d, &b);

    let mut visited: Vec<Rc<Node>> = vec![];
    let mut frontier: Vec<Rc<Node>> = vec![Rc::clone(&a)];

    while let Some(node) = frontier.pop() {
        if visited.iter().any(|n| Rc::ptr_eq(n, &node)) {
            continue;
        }

        println!("value: {}, Strong reference count: {}", &node.value, Rc::strong_count(&node));
        visited.push(Rc::clone(&node));

        for new_node in node.edges.borrow().iter() {
            frontier.push(Rc::clone(&new_node));
        }
    }  
}
```

This introduces a cycle in the graph. Since the Rc counts references to the pointer, we will
never clean up the pointer when it is no longer in scope, since the Rc will never reach 0.
Even after the nodes go out of scope, other nodes might have references to the nodes in their edges.


### 6)

Observe the fix to the code:

```rust
fn main() {
    let a = Node::new(0);
    let b = Node::new(1);
    let c = Node::new(2);
    let d = Node::new(3); 

    Node::connect(&a, &b);
    Node::connect(&a, &c);
    Node::connect(&b, &c);
    Node::connect(&c, &d);
    Node::connect(&d, &b);

    let mut visited: Vec<Rc<Node>> = vec![];
    let mut frontier: Vec<Rc<Node>> = vec![Rc::clone(&a)];

    while let Some(node) = frontier.pop() {
        if visited.iter().any(|n| Rc::ptr_eq(n, &node)) {
            continue;
        }

        println!("value: {}, Strong reference count: {}", &node.value, Rc::strong_count(&node));
        visited.push(Rc::clone(&node));
        
        for new_node in node.edges.borrow().iter() {
            if let Some(strong_node) = new_node.upgrade() {
                frontier.push(Rc::clone(&strong_node));

            }
        }
    }  
}
```

Since the nodes only reference eachother by `Weak` references now, we don't have the memory leak.
The nodes themselves are owned in the scope by the let bindings at the top of the functions.

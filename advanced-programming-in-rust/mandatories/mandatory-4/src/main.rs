use std::rc::Rc;
use std::rc::Weak;
use std::cell::RefCell;

struct Node {
    value: i32,
    edges: RefCell<Vec<Weak<Node>>>,
}

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
        
        a_edges.push(Rc::downgrade(&b));
        b_edges.push(Rc::downgrade(&a));
    }
}

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
    Node::connect(&a, &Node::new(5));

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

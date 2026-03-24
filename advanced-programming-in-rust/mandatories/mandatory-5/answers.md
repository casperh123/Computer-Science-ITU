# Mandatory 5

Observe the given boilerplate code:

```rust
trait Protocol {}

struct Send<T, S: Protocol> {
    tx: std::sync::mpsc::Sender<T>,
    next: S,
}

struct Recv<T, S: Protocol> {
    rx: std::sync::mpsc::Receiver<T>,
    next: S,
}

struct End;

impl<T, S: Protocol> Protocol for Send<T, S> {}
impl<T, S: Protocol> Protocol for Recv<T, S> {}

impl Protocol for End {}
```

### Task 1 && 2

```rust
fn send <T, S: Protocol>(state: Send<T, S>, v: T) -> S {
    let _ = state.tx.send(v);

    state.next
}

fn recv<T, S: Protocol>(state: Recv<T, S>) -> (T, S) {
    let received = state.rx.recv().unwrap();

    (received, state.next)
}
```

## Part 3

Observe the following program:

```rust
fn main() {
    let (tx1, rx1) = mpsc::channel();
    let (tx2, rx2) = mpsc::channel::<i32>();

    let server_protocol =
        Recv {
            rx: rx1,
            next: Send {
                tx: tx2,
                next: End
            }
        };

    thread::spawn(move || {
        let next = recv(server_protocol);
        
        send(next.1, next.0);
    });

    let client_protocol =
        Send {
            tx: tx1,
            next: Recv {
                rx: rx2,
                next: End
            }
        };

    let next = send(client_protocol, 500);
    let received = recv(next);

    println!("{}", received.0);
}
```

## Part 3

Observe the following program that violates the protocol by recieves before sending:

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx1, rx1) = mpsc::channel();
    let (tx2, rx2) = mpsc::channel::<i32>();

    let server_protocol =
        Recv {
            rx: rx1,
            next: Send {
                tx: tx2,
                next: End
            }
        };

    thread::spawn(move || {
        let next = recv(server_protocol);
        
        send(next.1, next.0);
    });

    let client_protocol =
        Recv {
            rx: rx1,
            next: Send{
                tx: tx2,
                next: End
            }
        };

    let next = send(client_protocol, 500);
    let received = recv(next);

    println!("{}", received.0);
}
```

The compiler will refuse to compile, since the type of the parameter given to the send function is incorrect. 
By the `send` function's type definition `<T, S: Protocol>(state: Send<T, S>, v: T) -> S`, the state given to the
function must be a `Send<T, S>`. This also allows the continuation state to be a `Send<T, S>`, but it will not accept
a `Recv<T, S>` as the initial state. 

## Part 4, Task 1 && 2

Observe both the protocol and the implementation:

```rust
se std::sync::mpsc;
use std::thread;

fn main() {
    let (tx_int_server, rx_int_server) = mpsc::channel::<i32>();
    let (tx_int_client, rx_int_client) = mpsc::channel::<i32>();
    let (tx_string, rx_string) = mpsc::channel::<String>();
    let (tx_bool, rx_bool) = mpsc::channel::<bool>();

    let server_protocol =
        Recv {
            rx: rx_int_server,
            next: Recv {
                rx: rx_bool,
                next: Send {
                    tx: tx_string,
                    next: Send {
                        tx: tx_int_client,
                        next: End
                    }
                }
            }
        };

    thread::spawn(move || {
        let (number, first) = recv(server_protocol);
        let (_condition, second) = recv(first);

        let third = send(second, "Roger roger".to_string());
        let _ = send(third, number);
    });

    let client_protocol =
        Send {
            tx: tx_int_server,
            next: Send {
                tx: tx_bool,
                next: Recv {
                    rx: rx_string,
                    next: Recv{
                        rx: rx_int_client,
                        next: End
                    }
                }
            }
        };

    let first = send(client_protocol, 500);
    let second = send(first, true);
    let (string, third) = recv(second);
    let (number, _fourth) = recv(third);

    println!("Received: {}, {}", string, number);
}
```

use std::sync::mpsc;
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

fn send <T, S: Protocol>(state: Send<T, S>, v: T) -> S {
    let _ = state.tx.send(v);

    state.next
}

fn recv<T, S: Protocol>(state: Recv<T, S>) -> (T, S) {
    let received = state.rx.recv().unwrap();

    (received, state.next)
}

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

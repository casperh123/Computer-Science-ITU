use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number");
    println!("Please input your guess");

    let secret_number = rand::random_range(1..=100);
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read lines");

    println!("You guessed {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("{guess} is less than the answer "),
        Ordering::Greater => println!("Number is greater than {guess}"),
        Ordering::Equal => println!("You guessed correctly!"),
    }
        
}

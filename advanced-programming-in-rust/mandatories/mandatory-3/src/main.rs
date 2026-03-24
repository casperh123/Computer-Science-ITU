fn main() {
    let s = String::from("hello");
    let mut counter = 0;
    
    let c1 = || println!("{s}");
    let c2 = || counter += 1;
    let c3 = || drop(s);

    let c4 = c2;

    println!(format!("{}", c4));
}

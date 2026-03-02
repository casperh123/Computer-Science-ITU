fn main() {
    let input = "Hej Marco!";

    {
        let output = first_word(input);

        println!("{]", &output);
    }
}

fn first_word<'a>(s: &'a str) -> &'a str {
    for (i, &b) in s.as_bytes().iter().enumerate() {
        if b == b' ' {
            return &s[..i];
        }
    }
    s
}

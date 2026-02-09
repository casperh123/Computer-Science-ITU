fn main() {
    let data = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6];
    let longest_subsequence = longest_increasing_run_owned(&data);

    for number in longest_subsequence {
        println!("{}", number);
    }
}

fn longest_increasing_run_owned(data: &[i32]) -> &[i32] {
    let mut current_start = 0;
    let mut current_length = 1;
    let mut longest_start = 0;
    let mut longest_length = 1;

    for i in 1..data.len() {



        if data[i] > data[i - 1] {
            current_length += 1;
            
            if current_length > longest_length {
                longest_start = current_start;
                longest_length = current_length;
            }
        } else {
            current_start = i;
            current_length = 1;
        }
    }

    &data[longest_start..longest_start + longest_length]
}

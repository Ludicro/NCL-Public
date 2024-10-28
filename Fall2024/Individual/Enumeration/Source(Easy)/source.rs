use std::io;

fn check(input: &str) {
    let enc: Vec<u8> = input.as_bytes().iter().map(|byte| byte ^ 0x84).collect();
    let check: Vec<u8> = vec![ 215, 207, 221, 169, 199, 214, 197, 198, 169, 189, 178, 182, 181 ];

    if enc == check {
        println!("Your password is correct");
    } else {
        println!("Wrong password");
    }
}

fn main() -> Result<(), std::io::Error> {
    let mut input = String::new();

    println!("Please input your password");

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            check(&input);
        }
        Err(error) => println!("Error: {}", error)
    }

    Ok(())
}
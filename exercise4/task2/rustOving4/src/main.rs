#![allow(non_snake_case)]
use std::io;

// Rewrites the character &, < and >.
fn transform(x: &str) -> String{
    return x.replace("&", "&amp").replace("<", "&lt").replace(">", "&gt");
}


fn main() {
    let mut input = String::new();
    println!("Type a sentence:");
    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            println!("Output: {}", transform(&*input));
        }
        Err(e) => println!("Something went wrong: {}", e)
    }
}

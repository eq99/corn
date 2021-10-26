fn main() {
    let name = String::from("Rust");
    println!("before: {}", name);
    let greeting = hello(&name);
    println!("{}", greeting);
    println!("after: {}", name);
}

fn hello(name: &String) -> String {
    format!("Hello, {}", name)
}

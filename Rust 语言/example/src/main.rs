fn main() {
    let mut hello = String::from("你好");
    hello.push_str(", rust");
    println!("{:?}", hello); // "你好, rust"

    println!("{:?}", hello + ", 嗯mua"); // "你好, rust, 嗯mua"

    let mut result = String::new();
    result = format!("{} + {} = {}", 600, 66, 600 + 66);
    println!("{:?}", result); // "600 + 66 = 666"
}

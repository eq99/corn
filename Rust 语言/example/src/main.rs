fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.bytes().len() > y.bytes().len() {
        x
    } else {
        y
    }
}

fn main() {
    let alice = "Alice";
    let bob = "Bob";

    println!("{}", longest(alice, bob));
}

/*
#[derive(Debug)]
struct Point(i32, i32);

impl Point {
    fn create_point_ref(x: i32, y: i32) -> &Self {
        &Point(x, y)
    }
}
fn main() {
    let ref_p = Point::create_point_ref(1, 2);
    println!("{:?}", ref_p);
}
*/

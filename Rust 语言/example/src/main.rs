fn main() {
    print!(
        "{}, {}, {}",
        (1..9).fold(0, |acc, _| acc + 1),
        (1..9).fold(0, |acc, x| acc + x),
        (1..9).fold(1, |acc, x| acc * x),
    );
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

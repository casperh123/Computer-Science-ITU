fn main() {
    let circle = Circle{
        radius: 5.0,
    };

    let rectangle = Rectangle{
        width: 10.0,
        height: 30.0,
    };

    print_area(&circle);
    print_area(&rectangle);
}

fn print_area<T: Area>(shape: &T) {
    println!("Area: {}", shape.area())
}

struct Rectangle {
    width: f64,
    height: f64
}

impl Area for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

struct Circle {
    radius: f64,
}

impl Area for Circle {
    fn area(&self) -> f64 {
        let circumference = 2.0 * self.radius;
        
        0.5 * (circumference * 3.14) * self.radius
    }
}

trait Area {
    fn area(&self) -> f64;
}

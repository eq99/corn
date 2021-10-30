use std::error::Error;
use std::fs::File;
use std::io;
use std::io::Read;

fn read_config_from_file() -> Result<String, io::Error> {
    let mut f = File::open("config.toml")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn main() -> Result<(), Box<dyn Error>> {
    let hello = read_config_from_file()?;
    println!("{:?}", hello);
    Ok(())
}

use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn main() -> Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    part_one(reader)
}

fn part_one(reader: BufReader<File>) -> Result<()> {
    for line in reader.lines() {
        let line = line?;
        let mut characters = line.chars();

        println!("{}", line);

        let left_digit = characters.rfind(|c| c.is_digit(10));
        println!("{:?}", left_digit);

        // Add your logic here for processing left_num and right_num
    }

    Ok(())
}

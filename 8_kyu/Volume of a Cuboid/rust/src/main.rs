fn get_volume_of_cuboid(length: f32, width: f32, height: f32) -> f32 {
    length * width * height
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(get_volume_of_cuboid(1.0, 2.0, 2.0), 4.0);
        assert_eq!(get_volume_of_cuboid(6.3, 2.0, 5.0), 63.0);
    }
}

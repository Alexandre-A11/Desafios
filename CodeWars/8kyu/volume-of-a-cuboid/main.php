<?php
$kata = new class {
    public function get_volume_of_cuboid($length, $width, $height) {
        // Your code here
        return $length * $width * $height;
    }
};

const BR = '<br>';
// TEST CASES
echo $kata->get_volume_of_cuboid(2, 4, 6) . BR; // => 48
// echo $kata->get_volume_of_cuboid(5, 3, 2) . BR; // => 30
// echo $kata->get_volume_of_cuboid(5, 5, 5) . BR; // => 125

// Cuboid volume = length * width * height
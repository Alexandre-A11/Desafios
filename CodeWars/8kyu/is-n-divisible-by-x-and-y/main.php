<?php
function is_divisible($n, $x, $y) {
    return $n % $x === 0 && $n % $y === 0;
}

// Testes:
print(is_divisible(3, 3, 4) . "\n");
print(is_divisible(12, 3, 4) . "\n");

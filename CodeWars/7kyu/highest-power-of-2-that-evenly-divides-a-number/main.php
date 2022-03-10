<?php
function solution(int $n): int {
    $x = 0;
    $result = 0;
    for ($i = 1; $x < $n; $i++) {
        $x = 2 ** $i;
        if ($n % $x === 0) {
            $result = $x;
        }
    }
    return $result === 0 ? 1 : $result;
}

print(solution(123) . "\n"); // 1
print(solution(192) . "\n"); // 64
print(solution(132232) . "\n"); // 8
print(solution(64) . "\n"); // 64

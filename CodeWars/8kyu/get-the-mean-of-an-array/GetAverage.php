<?php declare(strict_types=1);

class GetAverage {
    function get_average(array $a): int {
        return (int) (array_sum($a) / count($a));
    }
}

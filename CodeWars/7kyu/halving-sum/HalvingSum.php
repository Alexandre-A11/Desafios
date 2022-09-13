<?php declare(strict_types=1);

class HalvingSum {
    public function halvingSum(int $n): int {
        $sum = 1;
        for ($i = 1; floor($n / $i) > 1; $i *= 2) {
            $sum += floor($n / $i);
        }
        return (int) $sum;
    }

    public function halvingSum_s2($n): int {
        // prettier-ignore
        if ($n <= 1) return 1;

        return (int) $n + $this->halvingSum_s2(floor($n / 2));
    }
}

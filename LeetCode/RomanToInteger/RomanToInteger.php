<?php declare(strict_types=1);

namespace LeetCode\RomanToInteger;

class RomanToInteger {
    /**
     * @param String $s
     * @return Integer
     */
    public function romanToInt($s) {
        $num = 0;
        $roman = [
            "I" => 1,
            "V" => 5,
            "X" => 10,
            "L" => 50,
            "C" => 100,
            "D" => 500,
            "M" => 1000,
        ];
        $excep = [
            "IV" => 4,
            "IX" => 9,
            "XL" => 40,
            "XC" => 90,
            "CD" => 400,
            "CM" => 900,
        ];

        foreach ($excep as $key => $val) {
            if (str_contains($s, $key)) {
                $num += $val;
                $s = str_replace($key, "", $s);
            }
        }

        foreach (str_split($s) as $e) {
            if ($e === "I" || $e === "X" || $e === "C") {
            }
            $num += $roman[$e];
        }

        return $num;
    }
}

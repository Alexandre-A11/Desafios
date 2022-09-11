<?php declare(strict_types=1);

class Rounders {
    public function rounders(int $value): int {
        $array = array_map("intval", str_split((string) $value));
        $plus = 0;
        for ($i = count($array) - 2; $i >= 0; $i--) {
            $plus = $array[$i + 1] < 5 ? 0 : 1;
            $array[$i] += $plus;
            $array[$i + 1] = 0;
        }

        $result = implode("", $array);
        return (int) $result;
    }

    public function rounders_s2(int $value): int {
        for ($i = 1; $i < strlen((string) $value); ++$i) {
            $value = round($value, (int) -$i);
        }

        return (int) $value;
    }
}

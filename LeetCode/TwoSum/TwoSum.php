<?php
namespace App\LeetCode\TwoSum;
class TwoSum {

    /*
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */

    // Solução 1 - My:
    function twoSum($nums, $target) {
        for ($i = 0; $i < count($nums); $i++){
            for ($j = 1; $j < count($nums); $j++){
                if ($i === $j) continue;
                if ($nums[$i] + $nums[$j] === $target) return [$i, $j];
            }
        }
    }

    // Solução 2:
    function twoSum2(array $nums, int $target): array {
        $numArr = [];
        foreach ($nums as $i => $num) {
            $needed = $target - $num;
            if (isset($numArr[$needed])) {
                return [$i, $numArr[$needed]];
            }
            $numArr[$num] = $i;
        }
        return [];
    }
}
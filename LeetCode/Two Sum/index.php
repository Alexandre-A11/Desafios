<?php
class Solution {

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
    function twoSum2($nums, $target) {
        $seen = [];
        $numberCount = count($nums);
        for ($i = 0; $i < $numberCount; $i++) {
            $numberNeeded = $target - $nums[$i];
            if (isset($seen[$numberNeeded])) {
                return [$i,$seen[$numberNeeded]];
            }
            $seen[$nums[$i]] = $i;   
        }
        return [];
    }
}
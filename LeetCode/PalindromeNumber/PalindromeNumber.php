<?php declare(strict_types=1);

namespace LeetCode\PalindromeNumber;

class PalindromeNumber {
    /**
     * @param Integer $x
     * @return Boolean
     */
    public function isPalindrome($x) {
        $s = (string) $x;
        return strrev($s) === $s;
    }
}

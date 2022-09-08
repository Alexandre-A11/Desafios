<?php declare(strict_types=1);

class ReverseLettersSentence {

    public static function ReverseLetters_s1(string $sentence) {
        $words = explode(" ", $sentence);
        foreach ($words as $i => $word){
            $words[$i] = strrev($word);
        }

        return implode(" ", $words);
    }
}
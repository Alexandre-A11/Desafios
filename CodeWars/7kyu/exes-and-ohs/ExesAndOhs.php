<?php declare(strict_types=1);

class ExesAndOhs {
    function ExesAndOhs_s1($s) {
        $string = strtolower($s);
        return substr_count($string, "x") === substr_count($string, "o");
      }
}
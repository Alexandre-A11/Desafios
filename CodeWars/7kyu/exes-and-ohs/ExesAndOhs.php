<?php declare(strict_types=1);
namespace CodeWars\kyu7\exes_and_ohs;

class ExesAndOhs {
    function ExesAndOhs_s1($s) {
        $string = strtolower($s);
        return substr_count($string, "x") === substr_count($string, "o");
      }
}
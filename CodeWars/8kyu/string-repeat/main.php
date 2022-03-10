<?php
function repeatStr($n, $str) {
    return str_repeat($str, $n);
}

// Testes:
print(repeatStr(6, "I")); // "IIIIII"
print(repeatStr(5, "Hello")); // "HelloHelloHelloHelloHello"
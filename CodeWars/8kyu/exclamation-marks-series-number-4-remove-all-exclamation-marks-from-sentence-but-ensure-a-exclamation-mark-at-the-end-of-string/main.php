<?php
function remove(string $s): string {
    return str_replace("!", "", $s) . "!";
}


// Testes:
print(remove("Hi!") . "\n"
    . remove("Hi!!!") . "\n"
    . remove("!Hi") . "\n");

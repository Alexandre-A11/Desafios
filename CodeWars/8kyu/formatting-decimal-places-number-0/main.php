<?php
function twoDecimalPlaces($n) {
    return round($n, 2);
    // return (float) number_format($n, 2);
    // return number_format($n, 2);
    // return number_format(number_format($n, 3), 2);
}

// Testes:
print(var_dump(twoDecimalPlaces(5.5589)) . "\n" .
    twoDecimalPlaces(3.3424) . "\n" .
    twoDecimalPlaces(4.659725356) . "\n");

print(4.6600000000000001 === 4.66);

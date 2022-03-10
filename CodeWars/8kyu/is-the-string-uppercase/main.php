<?php
function is_uppercase($str){
    return $str === strtoupper($str);
}

// Teste:
$teste1 = is_uppercase("c");
$teste2 = is_uppercase("hello I AM DONALD");
$teste3 = is_uppercase("ACSKLDFJSSKLDFJSKLDFJ");

print($teste3);

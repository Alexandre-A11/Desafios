<?php

function chromosomeCheck($sperm) {
    $boy = strpos($sperm, 'Y');
    if ($boy) {
        return "Congratulations! You're going to have a son.";
    }

    return "Congratulations! You're going to have a daughter.";
}

chromosomeCheck("X");

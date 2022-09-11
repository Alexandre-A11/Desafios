<?php declare(strict_types=1);

class GoingToTheCinema {
    public function movie($card, $ticket, $perc) {
        $systemA = $ticket;
        $systemB = $card;
        $n = 0;

        while ($systemA <= ceil($systemB)) {
            $n++;
            $systemA = $ticket * $n;
            $systemB += $ticket * $perc ** $n;
        }

        return $n;
    }

    public function movie_s2($card, $ticket, $perc) {
        $n = 0;
        do {
            $n++;
            $card += $ticket * $perc ** $n;
        } while (ceil($card) >= $ticket * $n);
        return $n;
    }
}

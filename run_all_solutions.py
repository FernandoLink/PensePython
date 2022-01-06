"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import os


def pipe(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


filenames = """
ackermann_memo.py        grid.py             pokerhand.py
ackermann.py             has_duplicates.py   pokerhandsoln.py
anagram_db.py            header.py           polygon.py
anagram_sets.py          inlist.py           reducible.py
analyze_book1.py         interlock.py        reverse_pair.py
analyze_book2.py         invert_dict.py      rotate_pairs.py
analyze_book3.py         koch.py             rotate.py
badkangaroo.py           letters.py          sed.py
birthday.py              map.py              spiral.py
card.py                  markov.py           structshape.py
cartalk1.py              markov.py           time1.py
cartalk2.py              metathesis.py       time1_soln.py
cartalk3.py              most_frequent.py    time2.py
do_four.py               pace_calc.py        time2_soln.py
                         palindrome_soln.py  typewriter.py
find_duplicates_copy.py  pie.py              unstable_sort.py
find_duplicates.py       pi.py               walk.py
flower.py                point1.py           wordlist.py
goodkangaroo.py          point1_soln.py      zipf.py
"""

slow_ones = """
spiral.py                typewriter.py       pie.py
flower.py                wordlist.py         polygon.py
koch.py                  letters.py          zipf.py
""".split()


for filename in filenames.split():
    print(filename)
    if filename in slow_ones:
        print("Skipping")
        continue

    res, stat = pipe("python " + filename)
    print(stat)
    print(res)

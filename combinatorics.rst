
Combinatorics
=============

**This chapter helps you to answer problems of the type: How many possible ... exist.**

----

Permutations
------------

When you have a sequence of *n* unique items, **permutations** are the possible rearrangements.
In a permutation, the order of the items is important.
Their number is given by the factorial:

.. math::

    permutations = n!


----

Combinations without replacement
--------------------------------

If, and you pick *k* items from a pool of *n* possible ones, this is called **combinations**.
In combinations, the order of the items does not matter.
If you can use every item only once, the number of combinations is given by the **binomial coefficient**:

.. math::
    
    combinations_{norepl} = \binom{n}{k} = \frac{n!}{k!(n-k)!}

----

Combinations with replacement
-----------------------------

If you can draw an item multiple times, this is called **combinations with replacement**,
but the upper number of the binomial coefficient changes:

.. math::

    combinations_{repl} = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}

----

Sequences
---------

The number of possible sequences like strings, DNA, musical notes of length *k* from an alphabet with the size *n* is given by a power function:

.. math::

   n^k

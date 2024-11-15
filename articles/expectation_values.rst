
Expectation Values
==================

Once you can calculate the probability of an event (using a plain relative requency, 
a probability tree, Bayes Theorem or a distribution functions),
you may need to account for the value of the possible outcomes.
This is called calculating an **expectation value**.

.. topic:: Example

   You roll a six-sided die.
   
   * if you roll a 6, you get 10 points
   * if you roll a 1, you lose 5 points
   * for any other number you lose 1 point

   How many points do you win or lose on average?

Generic Definition
------------------

The expectation value *E* of the event *X* is the sum of the rewards
of each possible outcome :math:`v_i` times their possibilities :math:`p(X_i)`:

.. math::

    E(X) = \sum _i v_i \cdot p(X_i)

Applied to the example above, we consider the outcomes *6*, *1* and *other*:

.. math::

    E(roll) = 10 \cdot p(six) - 5 \cdot p(one) - 1 \cdot p(two-to-five)

.. math::

    E(roll) = 10 \cdot \frac{1}{6} - 5 \cdot \frac{1}{6} - 1 \cdot \frac{4}{6}

.. math::

    E(roll) = \frac{10}{6} - \frac{5}{6} - \frac{4}{6} = \frac{1}{6}

**Conclusion:** On average, you win one-sixth of a point per roll.


Adding Normal Distributions
---------------------------

A frequent application of expectation values is when values are sampled from more than one normal distribution.
In this case, you need to **add the mean and standard deviation** to get the resulting distribution functions.

.. topic:: Example

   A Chinstrap and a Gentoo penguin jump on a balance.
   What is the probability that their combined weight is more than 8000 g?

   * the weight of Chinstrap penuins is normally distributed with a mean of 3700 g and a standard deviation of 380 g.
   * the weight of Gentoo penuins is normally distributed with a mean of 5000 g and a standard deviation of 500 g.

   The combined weight is also normally distributed, with a mean of 8700 g and a standard deviation of 880 g.

   Thus, the probability that the pair is heavier than 8000 g can be calculated in a spreadsheet with:

   ::

      =1 - NORM.DIST(8000, 8700, 880, TRUE)

   which should result in about 78%.


Subtracting Normal Distributions
--------------------------------

A similar rule applies to the difference of two distributions.
In this case, you would **subtract the means of both distributions but still add the standard deviations**.

.. topic:: Example

   What is the probability that the Gentoo penguin is 1000 g heavier than the Chinstrap penguin?

   Using the same distributions as above, the difference *Gentoo - Chinstrap* follows a normal distribution
   with a mean of 1300 g (5000 g - 3700 g) and a standard deviation of 880 g.

   The probability that the difference is 1000 g or higher can be calculated in a spreadsheet with:

   ::

      =1 - NORM.DIST(1000, 1300, 880, TRUE)

   which should result in about 63%.

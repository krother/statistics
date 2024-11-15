
Probability
===========

Random Event
------------

A random event is an event that can have different outcomes.
E.g. when randomly selecting a penguin from a larger group, the species of the chosen penguin is the outcome.

Random events are often denoted by capital letters:

.. math::

   p(A)

or by explicit labels:

.. math::

   p(Adelie)

The sum of the probabilities for all possible outcomes of a random event has to be 1.0.

.. math::

    \sum_i p(A_i) = 1.0

----

Conditional Probability
-----------------------

Often, the probability of an outcome depends on the outcome of a different random event. This is called a **conditional probability**.

For instance, if the probability of outcome A depends on outcome B, you can write:

.. math::

   p(A|B)

----

Prior
-----

In contrast to a conditional probability, the probability of an event without any additional information is called **prior probability** or **prior**.

----

Total Probability
-----------------

To calculate the prior probability :math:`p(A)` from a conditional probability :math:`p(A|B)`, you have to sum up the conditional probabilities for all possible outcomes of *B*.
This is called the **total probability**:

.. math::

   p(A) = \sum p(A|B_j) \cdot p(B_j)

----

Multiplication Rule
-------------------

If two events are consecutive and you want the probability of a combination, you need to multiply the probabilities with each other:

.. math::

   p(A \cap B) = p(A|B) \cdot p(B)

The :math:`\cap` symbol denotes the *intersection* of both outcomes.

----

Bayes Theorem
-------------

With **Bayes Theorem**, you can reverse the order of a conditional probability:

.. math::

   p(A|B) = \frac{p(B|A) \cdot p(A)}{p(B)}

Here, :math:`p(A)` is the **prior probability** (if we had no additional information about A).

----

Statistical Independence
------------------------

Two events are called **independent** if their conditional probabilities are equal to their respective priors:

.. math::

   p(A|B_i) = p(A)

for all :math:`B_i`.
From Bayes Theorem it follows that in this case the reverse is also true:

.. math::

   p(B|A_j) = p(B)

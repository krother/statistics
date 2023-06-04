
Correlation
===========

Correlation is an important metric from **bivariate statistics**.
It measures how strongly two variables are connected.

----

Definition
----------

The **correlation coefficient r** is calculated as:

.. math::

   r = m * \frac{std_x}{std_y}

Where :math:`std_x` and :math:`std_y` are the standard deviations of x and y, and *m* is the slope of the linear regression.
There exist a few alternative definitions but this is the simplest one.

Interpreting correlations
-------------------------

The correlation coefficient tells you **how much of the variance in x can be explained by y and vice versa**. In particular:

============ =========================================================================
coefficient  meaning
============ =========================================================================
1.0          there is a perfect positive correlation between the two variables
-1.0         there is a perfect negative correlation between the two variables
0.0          the two variables are perfectly independent
============ =========================================================================

----

Confounding
-----------

A particularly nasty trap in bivariate statistics is **confounding** or **confounding factors**.
It means that there is a third variable that is more important than the two variables you are analyzing.
For instance, there could be multiple subgroups in the data, each having a different correlation.

When there is a confounding factor it makes correlation coefficients meaningless.
It is even possible that the correlation coefficient when the confounding categories are considered independently. This is called **Simpsons Paradox**.

The problem is nasty because you cannot find out which is the confounding factor by looking at the numbers. Ultimately, you need *domain expertise* to interpret the data correctly.

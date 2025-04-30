
Centrality and Dispersion
=========================

Measures of Centrality
++++++++++++++++++++++

**With metrics of centrality or central tendency, we want to calculate a single number that represents a typical value for a statistical variable.**

----

Arithmetic Mean
---------------

The arithmetic mean is the sum of all values divided by the number of values:

.. math::

   \bar{x} = \frac{\sum_{i=1}^n x_i}{n}

The arithmetic mean is *susceptible to outliers*.

----

Median
------

The median is calculated by sorting all values and then taking the mean or the 1-2 values in the middle (depends if there is an odd or even number).

The median is very robust.
Outliers do not affect it much, but it does not take all observations into account.

----

Mode
----

The mode is the value that occurs most frequently in your data.
It can be calculated only if your data is *discrete*.

There can be one or several modes.
Data with one mode is called **unimodal**, with two modes it is called **bimodal**.
If your sample is bimodal, calculating the mean or median is often not a good idea.

----

Measures of Dispersion
++++++++++++++++++++++

These group of statistics try to measure the degree of variability in the data,
i.e. how much the data fluctuates.
If the dispersion is large,  It's important to think about variability,
because it's much more difficult to accurately predict the value of a new
observation when the dispersion is large.

----

Range
-----

The range is the difference between the biggest and the smallest value:

.. math::

  R_x = max(x) - min(x)

The range is simple to calculate, but affected a lot by outliers.

----

Standard Deviation
------------------

The most commonly used dispersion metric is the standard deviation.
It is calculated from the sum of squared differences from the mean: 

.. math::

  \sigma = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n}}

It is typically used to describe that the majority of your data is found up to one standard deviation from the mean.
If your data follows a normal distribution, you will find 68.3% of the data in that range.
Like the mean, the standard deviation is susceptible to outliers.

.. hint::

   There are two versions of the equation.
   One divides by `n` (for populations), the other by `n-1` (for samples).
   For large samples, they do not differ much.
   In this course, we will treat them the same.

----

Variance
--------

The square of the standard deviation is called variance.
It is not that important for reporting,

.. math::

  var = \sigma^2

----

Quartiles 
---------

Quartiles (:math:`x_{0.25}, x_{0.5}, x_{0.75}`) are the intervals in which you find:

* the lowest 25% of the data (first quartile)
* the next 25% of the data up to the median (second quartile)
* the 25% of the data above the median (third quartile)
* the top 25% of the data (fourth quartile)

----

IQR (Inter Quartile Range)
--------------------------

The IQR is the range of the two middle quartiles.
In a **box plot**, it is the size of the box.

.. math::

  IQR_x = x_{0.75} - x_{0.25}


Frequencies and Pivots
======================

Absolute Frequency
------------------

The **absolute frequency** is simply the number of rows (observations) in your dataset.
Often it is used to describe how your data divides into subgroups.

Relative Frequency
------------------

If you have multiple subgroups, you often want to know what proportion of your entire dataset belongs to a subgroup.
That is what a relative frequency is good for.
It maps your count to a number between 0.0 (nothing) and 1.0 (everything).
It is defined as:

.. math::

    p_{group} = \frac{n_{group}}{n}

Where :math:`n_{group}` is the absolute frequency for a group and :math:`n` is the total number of observations in your dataset.

.. hint::

   Relative frequencies can be interpreted nicely as probabilities.

Percentage
----------

A percentage is the same as a relative frequency multiplied by 100.
Make sure to include the ``%`` sign so that the two cannot be mixed up.

Pivots
------

A **pivot table** is a useful summary of a dataset, because it shows you three variables at a time.
To create a pivot table, you need:

1. a column variable (a categorical variable that defines which columns the pivot will have)
2. a row variable (a categorical variable that defines which rows the pivot will have)
3. the data column (a numerical variable that is used to calculate the values in the table
4. an aggregation function (how the values in the table are calculated)

Typical aggregation functions are: count, mean, median, standard deviation.


Normalizing pivot tables
------------------------

If you have a pivot table with absolute frequencies, you can calculate relative frequencies in mutiple ways:

* divide by the total number for each row (so that rows sum up to 1.0)
* divide by the total number for each column (so that columns sum up to 1.0)
* divide by the total sum (so that everything sums up to 1.0)

Which is better depends on what you actually want to show.
A good practice is to include an extra row or column in the table that contains the respective sum.

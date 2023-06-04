
Linear Regression
=================

Linear regression is a method from **bivariate statistics**.
It helps us to interpret relationships between **two variables**.

A simple linear regression fits a straight line into the scatterplot of all datapoints for two variables *x* and *y*:

.. math::

   y = mx + b

Where *m* is called the **slope** of the line and *b* the **intercept** (the position where the line crosses the y-axis).

----

Finding the optimal regression line
-----------------------------------

The optimal regression line minimizes the **mean squared error (MSE)** between the actual y-value and the *predicted* value :math:`\hat y`:

.. math::

   MSE = \frac{1}{n}\sum_i^n (y - \hat y)^2

It follows that the regression line is somewhat sensitive to outliers.  


There is a lot of theory behind why the mean squared error is used.
It can be proven that this is the most probable line (see: *maximum likelihood principle*).

----

Interpretation
--------------

Once you have done a linear regression, you can use the slope to formulate statements like:

::

    on average, 1 mm of beak length means the penguin is 200 g heavier.

If you want to communicate the error of a regression, the **mean absolute error** is very useful, because it has the same unit:

.. math::

   MAE = \frac{1}{n}\sum_i^n | y - \hat y |

It can be stated like:

::
    
    the linear model has a mean abosolute error of 150 g.

----

Assumptions
-----------

There are a few important assumptions that have to be met for linear regression to work:

* there is a linear relationship between the variables X and Y to start with
* the data points are a random sample from the population
* the values in X are different
* the mean of the error is zero. It does not depend on X (i.e. higher x-values do not mean higher errors)
* the variance of the error is the same over all values of X (i.e. higher x-values do not mean higher variation of the error; homoscedasticity)

Together, these five assumptions support the **Gauss-Markov Theorem**.
If they are met, your regression line is guaranteed to give you the best possible linear fit through the data.


.. note::

   Another name for Linear Regression is **Ordinary Least Squares**.

   Linear Regression is a powerful Machine Learning method that works as well
   for more than two variables. This is not covered here though.
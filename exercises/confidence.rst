
Session 7: Confidence
=====================

Exercise 1: Sample
------------------

Create a list of 10 countries.

What other ways of generating a representative sample could you think of?

Exercise 2: Key concepts
------------------------

Clarify the concepts:

* sample
* population
* representative sample
* sample mean
* population mean
* Central Limit Theorem

Exercise 3: Sample mean
-----------------------

Calculate the mean life expectancy :math:`\overline{x}` of the 10 countries from the table in :download:`countries2015.csv`.

In Python, you can use the following expression on a `pd.DataFrame` to select multiple rows by the index:

.. code:: python3

    countries = ["name1", "name2", ...]
    sample = df.loc[countries]

Exercise 4: Population mean
---------------------------

Calculate the mean life expectancy :math:`\mu` of the population.

Exercise 5: Multiple samples
----------------------------

Collect multiple samples of the same size using:

.. code:: python3

    df.sample(10)

Calculate the mean life expectancy of each sample.
Compare the distribution against the population mean.
What do you notice?

Exercise 6: Standard Error
--------------------------

Calculate the standard error of the sample mean using the equation:

.. math::

    stderr = \frac{\sigma}{\sqrt{n}}

where :math:`\sigma` is the **standard deviation** of the population.

Compare the standard error against the standard deviation of the population.
Is it larger or smaller?

Exercise 7: Confidence interval
-------------------------------

Calculate a confidence interval of the sample mean, so that:

.. math::

    \overline{x} \pm c \frac{stderr}{\sqrt{n}}

Use the following procedure:

1. set a confidence threshold (e.g. 90%, 95% or 99%)
2. calculate the value **z** of a standard normal distribution that gives **half** that probability. This is your confidence interval in a standard normal distribution
3. convert **z** into the unit you are interested in using the equation

.. math::

    z = \frac{x - \mu}{\sigma^2}

assuming that :math:`\overline{x}` is a good estimate of the mean and the variance of the sample can be used to approximate the standard deviation of the population:

.. math::

    stderr = \frac{\sigma}{\sqrt{n}}

Exercise 8: Number of people
----------------------------

Now estimate the mean number of people for the countries with data.
Do we need to take anything new into account?

Exercise 9: Confidence
----------------------

Calculate a 95% confidence interval for the number of people in a country from a sample.

To normalize the number of people you can use:

.. code:: python3

   import numpy as np

   df["logpop"] = np.log(df["..."])

and to convert it back:

.. code:: python3

   np.exp(values)


Exercise 10: Adding distributions
---------------------------------

What is the probability that two random countries have more than 100 million people?


Exercise 11: Difference of two distributions
--------------------------------------------

What is the probability that one random country is 10 million people bigger than another?

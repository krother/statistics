Descriptive Statistics
======================

**Descriptive statistics** aims to describe a given data set visually and through
metrics. There is no uncertainty in descriptive statistics! It is a crucial step
in every exploratory analysis as we get a better feeling for the data, its characteristics
and relationships.

In descriptinve statistics, we do:

* observe data
* apply models and metrics to the data
* describe and explain the outcome

There is also **inferential statistics** where you would **predict** values using a statistical model.

----

Random Variables
----------------

In statistics, a **random variable** or **variable** represents the input or output data of a
statistical model.
In practice, each column of a data set can be regarded as the observed values of a
random variable.

A variable can be described by a probability distribution function, even if that function is not known.
In practice this means that you can talk and write about a variable even if you have not collected any data yet.

.. hint::

   If you want to avoid ambiguity with the very different concept of variables in programming, 
   use the term *random variable*.

----

Observation
-----------

An observation is an instance of data that you have.
E.g. a row in a table.

----

Population
----------

A **population** contains every subject that is of interest in order to answer a certain question.
In practice, if you know the population, it means that you have collected all data that exists (good).

----

Sample
------

A **sample** consists of one or more observations. 
It is a random or non-random subset of a population.
In practice having a sample means you are working with incomplete data.

----

Types of Variables
==================

Categorical
-----------

Categorical variables (also called **nominal** variables) have values or labels that do not follow a natural ordering.

Sometimes we **encode** the labels of categorical variables as numbers.
Although, in that case, the **data type** of these variables is ``int`` or ``float``, mathematical operations
(addition, multiplicaton, ...) shouldn't be applied to it.

Examples:

* Location (Berlin, Johannesburg, ...)
* Nationality
* Postal Codes (54296, 50679, ...)

----

Ordinal
-------

Ordinal or **ranked** variables have values that follow a natural order.
However, the difference between the values is not measurable.
As with categorical variables we often encode this kind of data with numeric values.

Examples:

* Movie Ratings (5 Stars, ..., 1 Star)
* Evaluation ('Very Good', 'Good', ..., 'Awful')
* Month of the year (1, 2, 3, ..., 12)

----

Numerical
---------

Numerical (scalar) variables have values with a natural ordering and the
distance between two values is interpretable.
Hence, we can say *"this value is twice as large as the other value"*.
Numerical variables can be both integer numbers or floating point numbers.

Examples:

* Height in cm (186, 150)
* Age in years
* Price in $

----

Discrete Variables
------------------

Discrete variables have a finite number of possible values.
Ordinal and categorical variables are always discrete.
Note, that metric variables can often be modeled as either discrete or continuous.

Examples:

* Number of books delivered by Amazon each day
* Number of rainy days per year
* Movie Ratings (5 Stars, ..., 1 Star)

----

Continuous Variables
--------------------

Continuous variables have a theoretically infinite number of possible values.

Examples:

* distance between two cities
* Height (in cm)
* Age (in years)

----

A few more types
----------------

Here are some extra types of variables. To many of these, special rules apply

* binary numbers
* dates and times (depends on how exactly the time is encoded)
* time series (a value over time)
* angles, longitude and latitude (they are circular)
* text
* images
* hashes

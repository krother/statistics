Session 2: Frequency, Plots and Pivots
======================================

|image0|

Exercise 1: Histogram of beak sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read the penguin data from the file ``penguins.csv`` using Python. Use
your local Python installation or go to
`jupyter.org/try-jupyter/lab/ <https://jupyter.org/try-jupyter/lab/>`__
and click the top-left symbol to start a notebook. Complete the
following code:

::

   import pandas as pd

   df = pd.read_csv(...)
   print(df.head())

Inspect the column names

::

   print(df.columns)

Plot a histogram of beak sizes:

::

   df[...].hist(bins=30)

What do you observe?

Exercise 2: Good and bad plots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look at the twelve plots. Which of them are good or bad and why?

Exercise 3: Group by a category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Count the penguins by species using the ``df.groupby()`` function:

::

   groups = df.groupby('species')['bill_length_mm'].count()
   print(groups)

Replace the ``.count()`` function by ``.mean()``.

This does the same as the ``value_counts()`` but we will extend it
further.

Exercise 4: Plot by a category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now plot the groups as a bar plot:

::

   groups.plot.bar()

Also try this for the grouped means.

Exercise 5: Histogram by category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of aggregating the groups to a single number, create three
histograms:

::

   df.groupby('species')['bill_length_mm'].hist()

The plot is not very clear however. A better alternative is using the
``seaborn`` library:

::

   import seaborn as sns

   sns.histplot(data=df, x='bill_length_mm', hue='species', kde=True)

A boxplot is also very illustrative:

::

   sns.boxplot(data=df, x='species', y='bill_length_mm')

Exercise 6: Group by two categories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also group by two categorical variables.

::

   groups = df.groupby(['species', 'sex'])['bill_length_mm'].count()
   print(groups)

A more pleasant way to read the data is to place one categorical
variable in the rows and the other in the columns of the table. This is
called a **crosstable** or **pivot table**:

::

   pivot = groups.unstack()
   print(pivot)

Exercise 7: Plot the pivot table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One way to plot a pivot table is to create a grouped bar plot:

::

   pivot.plot.bar()

Also try the transposed version:

::

   pivot.transpose().plot.bar()

Alternatively, you could go for a heatmap:

::

   import seaborn as sns

   sns.heatmap(data=pivot, annot=True)

Exercise 8: Pivot average
~~~~~~~~~~~~~~~~~~~~~~~~~

Calculate a pivot table showing the **average beak size** for every
combination of species/gender.

Exercise 9: Normalized counts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the pivot table of penguin count by species/gender. We will
normalize the data.

First, normalize by one axis:

::

   norm1 = pivot / pivot.sum(axis=0)
   print(norm1)

Second, normalize by the other axis:

::

   norm2 = pivot.T / pivot.sum(axis=1)
   print(norm2.T)

Third, normalize by the overall sum:

::

   norm3 = pivot / pivot.sum()
   print(norm3)

What do the numbers mean?

Exercise 10: Normalize by min/max
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A different way to normalize data is to **scale** the data. We will use
the min and max to scale the original data.

::

   beaks = df['bill_length_mm']
   scaled = (beaks - beaks.min()) / (beaks.max() - beaks.min())
   print(scaled)

You can also plot the result to get an impression:

::

   scaled.hist(bins=30)

What do the numbers mean?

Exercise 11: z-Score
~~~~~~~~~~~~~~~~~~~~

The last type of normalization in this section is to take the mean and
standard deviation into account. This is calld **standard scaling** or
**z-score**:

::

   zscore = (beaks - beaks.mean()) / beaks.sdev()
   print(zscores)

and

::

   zscore.hist(bins=30)

What do the numbers mean?

Exercise 12: Penguin Beak Report
--------------------------------

Examine the penguin data in the table ``penguins.csv``. Solve the
following tasks to examine the **beak length** variable:

Write down 3-5 sentences describing the beaks of the penguins in the
data. Use the mean, median and standard deviation and the knowledge
gained from the above exercises.

--------------

License
-------

(c) 2023 Dr. Kristian Rother

Available under the conditions of the Creative Commons Attribution
Share-alike License 4.0 (CC-BY-SA 4.0). See creativecommons.org for
details.

.. |image0| image:: penguin_heads.png


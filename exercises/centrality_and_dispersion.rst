Centrality and Dispersion
=========================

Exercise 1: What is statistics?
-------------------------------

Discuss in a small group:

-  what is statistics?
-  why is it important?
-  find an example of a statistical outcome (a number, a statement, a
   picture or diagram) and post it in the channel


Exerxise 2: Plotting
--------------------

Use your local Python installation or go to
`jupyter.org/try-jupyter/lab/ <https://jupyter.org/try-jupyter/lab/>`__
and click the top-left symbol to start a notebook. 
Put the spreadsheet into the same folder as your Python notebook.
Execute the following piece of Python code:

.. code:: python3

   import pandas as pd
   from matplotlib import pyplot as plt

   df = pd.read_excel("penguins.xlsx")
   print(df.head())

   count = df["..."].value_counts()
   print(count)

   count.plot.bar()

You should see a plot with several bars.

Exercise 3: Centrality
----------------------

Now calculate the mean number of characters in our names.
The following Python code contains 3 bugs. Find and fix them.

.. code:: python3

   import pandas as pd

   pd.read_excel("students.xlsx"

   mean = df[chars_in_name].mean()
   print(f"average number of characters : {mean:4.2f}")

Exercise 4: Median and Mode
---------------------------

Replace the ``mean()`` function by ``median()`` and ``mode()``. To print
the mode you need to leave away the ``:4.2f``.

Examine the result.

Exercise 5: Outliers
--------------------

Modify one the first entry to a very high number:

.. code:: python3

   df.loc[0, "chars_in_name"] = 100
   print(df.head())

Repeat the calculation of the mean and median. How do the metrics
change?

Exercise 6: Spread
------------------

Use the functions ``std()``, ``min()``, ``max()`` and ``describe()`` to
examine the spread of the variable.

Examine the effect of adding the outlier on these numbers as well.

Exercise 7: Box Plot
---------------------

Draw a box plot showing the distribution of characters for different
transportation modes.

.. code:: python3

   df["chars_in_name"].plot.box()

If you have a local Python installation (with Anaconda), you can create
a nicer plot with:

.. code:: python3

   import seaborn as sns
   import pandas as pd

   df = pd.read_excel("students.xlsx")
   sns.boxplot(data=df, y="chars_in_name", hue="transportation")

Exercise 8: Histogram
----------------------

Draw a histogram using the previously loaded data and libraries:

df[“chars_in_name”].hist(bins=10)

If you have a local Python installation (with Anaconda), you can create
a nicer plot with:

.. code:: python3

   sns.histplot(
       data=df,
       x="chars_in_name",
       bins=10,
   )

Try out different numbers for ``bins`` and see how the result changes.
Also try setting ``kde=True``.

Exercise 9: Summary
--------------------

Examine the student table further, plotting or calculating metrics from
other columns. Write a tweet-length news headline summarizing your
findings and post it in the course channel.

--------------

Challenge: Penguins
-------------------

Examine the penguin data in the spreadsheet :download:`penguins.xlsx`.
Solve the following tasks to examine the **beak length** variable:

-  calculate the mean beak length
-  calculate the median beak length
-  calculate the standard deviation of the beak length
-  draw a bar plot showing the frequencies of all three species
-  draw a histogram of the beak length
-  draw a box plot of the beak length

How would you interpret the result?

Centrality and Dispersion
=========================

Exercise 1: Set up Python
-------------------------

Make sure you have a Python installation that allows you to create and execute Jupyter Notebooks.
You find instructions on `www.academis.eu/pandas_go_to_space/preparations/README.html <https://www.academis.eu/pandas_go_to_space/preparations/README.html>`__


Exercise 2: Plotting
--------------------

For the following exercises you will need a spreadsheet with student data that you created in class.

Put the spreadsheet into the same folder as your Python notebook.
Execute the following piece of Python code:

.. code:: python3

   import pandas as pd
   from matplotlib import pyplot as plt

   df = pd.read_excel("students.xlsx")
   df.head()

If that works, also insert a column name in the next piece of code:

.. code:: python3

   count = df["..."].value_counts()
   count

Finally, create a plot with several bars:

.. code:: python3

   count.plot.bar()


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

Exercise 6: Dispersion
----------------------

Use the functions ``std()``, ``min()``, ``max()`` and ``describe()`` to
examine the dispersion of the variable.

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

Examine the student data further.
Write a news headline summarizing your findings and post it in the course channel.

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

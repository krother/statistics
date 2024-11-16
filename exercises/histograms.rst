
Histograms
==========

Read the penguin data from the file :download:`penguins.csv` using Python.
Use your local Python installation or go to
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

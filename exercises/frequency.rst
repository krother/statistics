
Session 2: Frequencies and Pivots
=================================

|image0|

Exercise 1: Read data
---------------------

Read the penguin data from the file ``penguins.csv`` into a spreadsheet.

Exercise 2: Group by a category
-------------------------------

Count the penguins by species using the ``COUNTIF`` function, e.g.:

===== ========= ========== ==================================
   id species   labels     count
===== ========= ========== ==================================
    1 Adelie    Adelie     =COUNTIF(B$2:B$333,C$2:C$4)
    2 Adelie    Gentoo     ...
    3 Adelie    Chinstrap  ...
    4 Gentoo
    5 Gentoo
    6 ...
===== ========= ========== ==================================
  

Exercise 3: Group means
-----------------------

Calculate the mean beak size for each species.

Exercise 4: Plot by a category
------------------------------

Plot the group counts as a bar plot.

Also try this for the grouped means.


Exercise 5: Group by two categories
-----------------------------------

You can also group by two categorical variables.
To make the data easy to read, place one categorical
variable in the rows and the other in the columns of the table. This is
called a **crosstable** or **pivot table**.

Create a pivot table grouping the penguin count for each gender and species.


Exercise 6: Plot the pivot table
--------------------------------

Plot the pivot table as a grouped bar plot.

Exercise 7: Pivot average
-------------------------

Calculate a pivot table showing the **average beak size** for every
combination of species/gender.


Exercise 8: Normalized counts
-----------------------------

Normalize the pivot table of penguin count by species/gender,
so that each cell contains *relative frequencies*.

What options for normalization do you have?

Exercise 9: Normalize by min/max
---------------------------------

A different way to normalize data is to **scale** the data. We will use
the min and max to scale the original data.

Try the equation:

    scaled = (value - min) / (max - min)


Exercise 10: z-Score
--------------------

The last type of normalization in this section is to take the mean and
standard deviation into account. This is calld **standard scaling** or
**z-score**:

Use the equation:

    zscore = (beaks - mean) / std_dev


What do the numbers mean?

Exercise 11: Penguin Beak Report
--------------------------------

Examine the penguin data in the table ``penguins.csv``. Solve the
following tasks to examine the **beak length** variable:

Write down 3-5 sentences describing the beaks of the penguins in the
data. Use the mean, median and standard deviation and the knowledge
gained from the above exercises.


.. |image0| image:: penguin_heads.png


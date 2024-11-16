Linear Relationships
====================

Exercise 1: Causation
---------------------

Take a look at the website `Spurious Correlations <https://tylervigen.com/spurious-correlations>`__

How do you think was the website created?


Exercise 2: Scatter Plot
------------------------

Draw a scatter plot of the penguins in `penguins.csv`.
Plot the **flipper length** vs the **body mass** of all penguins.

In Python, you can use the following code:

.. code:: python3

    import seaborn as sns

    df = sns.load_dataset('penguins')
    sns.scatterplot(data=df, x="...", y="...")


Exercise 3: Linear Regression
-----------------------------

Fit a straight line into the data (also called **Ordinary Least Squares**).

In Python, a quality library for OLS models is **statsmodels**.
Use the following code:

.. code:: python3

    from statsmodels.regression.linear_model import OLS
    from statsmodels import api as sm

    df = df.dropna(inplace=True)    
    X = df[...]
    X = sm.add_constant(X)
    y = df[...]

    model = OLS(y, X).fit()
    model.summary()

Discuss the meaning of some elements in the output.


Exercise 4: Draw the line of fit
--------------------------------

Calculate a line of best fit between a minimum and maximum x value:

.. code:: python3

    xpred = [..., ...]
    xpred = sm.add_constant(xpred)
    ypred = model.predict(xpred)

Inspect the values, then plot the line:

.. code:: python3

    sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g')
    plt.plot(x, yline, color="red")


Exercise 5: Error
-----------------

Write code to calculate the **mean squared error (MSE)** for the penguins:

.. code:: python3

    ypred = model.predict(X)
    diff = y - ypred
    ...


Exercise 6: Anscombes Quartet
-----------------------------

Examine the **Anscombe Quartet** data.
It is an artificial dataset consisting of four separate groups.
Start by examining the mean and standard deviation of each group:

.. code:: python3

    a = sns.load_dataset('anscombe')

    a.groupby('dataset').agg(['mean', 'std'])


Consider creating a linear fit for each of these groups.
What would you have to take into account?


Exercise 7: Correlations
------------------------

Play a few rounds of `Guess the Correlation <https://www.guessthecorrelation.com/>`__


Exercise 8: Correlation Coefficients
------------------------------------

Calculate the correlation coefficients of the penguin dataset:

.. code:: python3

    df.corr()


Exercise 9: Heatmap
--------------------

Plot the correlation coefficients as a **heatmap**:

.. code:: python3

    sns.heatmap(df.corr(), annot=True)


Exercise 10: Add Categories
---------------------------

Add extra columns for the species, converting them to integer columns.
This is called **dummy encoding** or **one-hot-encoding**:

.. code:: python3

    import pandas as pd

    binary = pd.get_dummies(df['species'])
    df2 = pd.concat([df, binary], axis=1)

Calculate correlation coefficients for the new columns as well.


Exercise 11: Scatterplot Matrix
-------------------------------

Here is a particularly useful way to examine pairs of variables:

.. code:: python3

    sns.pairplot(df, hue="species")


Exercise 12: Confounding Factors
--------------------------------

Examine the relationship of **beak length** vs **beak depth**.
Could you construct a linear model for these as well?

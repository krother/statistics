
Time Series Data
================

In this chapter, we will use a few statistical tools to describe **Time Series Data**.

Exercise 1: Read Bitcoin Data
-----------------------------

Load the data in :download:`bitcoin.csv` into Excel.
Create a line plot, so that the time is on the x-axis and the price in EUR is on the y-axis.

Exercise 2: Good and Bad Plots
------------------------------

Examine the plots in :download:`good_bad_plots2.zip` . 
Discuss which of them are good, which are bad and why.

Exercise 3: Difference
----------------------

Create a new column that contains the difference between a value and the previous one.
Create a line plot of the difference.

Exercise 4: Log-Transform
-------------------------

Create a new column that contains the logarithm of the price.
Create a line plot as well.

Exercise 5: Trend
-----------------

Which of the columns you have (raw, diff, log) comes closest to a linear function?
Calculate a linear fit on the data.
Determine the slope and the intercept.

Exercise 6: Remove the trend
----------------------------

Calculate the residuals: The difference between the data and a linear model.

Exercise 7: Moving average
--------------------------

Now smooth the de-trended data using a moving average.
Create a new column where you calculate the arithmetic mean over 14 consecutive days.
Plot the moving average and the raw data in the same plot.

Exercise 8: Lags
----------------

Create a new column that is a copy of the de-trended data but shifted down by one rows.
Calculate a correlation coefficient between the *lag column* and the original one.

Exercise 9: Autocorrelation
---------------------------

Create more lag columns (about 10).
Calculate a correlation coefficient for each of them.

Plot the correlation coefficients for each lag as a bar chart,
so that the .

Exercise 10: Resampling
-----------------------

Find out how you can **resample** the data, so that you have one value for each month.

Exercise 11: Seasonality
------------------------

Do you observe any seasonal patterns that occur during specific months? 

Exercise 12: Forecasting
------------------------

Discuss the results.
How could the statistical tools above help you create a forecast?

How could you determine the accuracy of that forecast?


.. topic:: Getting your own data

   If you would like to get the most recent data or examine other cryptocurrencies, do the following:

   1. Visit `coingecko public API <https://www.coingecko.com/en/api/documentation>`__
   2. Click on the ``/coins/{id}/market_chart`` section
   3. Press the **Try it out** button
   4. Fill in the form and submit it
   5. Download the **reponse body**

   The raw data contains **Unix Timestamps** in the left column.
   You might want to convert the dates to a more readable date format.

   .. literalinclude:: read_history.py

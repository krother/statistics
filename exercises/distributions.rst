Session 4: Distributions
========================

Exercise 1: Dice Rolls
----------------------

The penguins play a dice game: They take turns rolling a 6-sided die.
Whoever rolls a 6 wins.

Create random numbers for 100 dice rolls. Plot a histogram of the
results.

You can use the following code:

::

   import numpy as np
   import pandas as pd

   dice = np.random.randint(1, 7, size=(100))
   pd.Series(dice).hist()

Exercise 2: More numbers
------------------------

The game becomes very popular among the penguins.

Create random numbers for 10000 dice rolls. Plot a histogram of the
results.

What has changed?

Exercise 3: Adding Dice
-----------------------

After some time the game becomes boring so the penguins change the
rules. Now they roll 2 dice and add the numbers together.

Plot the histogram for 10000 rolls.

Then repeat the calculation for 3, 4 and 10 dice.

To sum dice, try:

::

   dice = np.random.randint(1, 7, size=(100, 2))
   added = dice.sum(axis=1)

Exercise 4: Coins
-----------------

The penguins invented a game where they toss a coin 3 times. If they
flip heads 3 times, they win.

Randomly create 100 x 3 coin flips and count the number of “heads” in
each series. Plot a histogram that shows how many heads were flipped.

You can use the following code:

::

   import numpy as np
   import pandas as pd

   coins = np.random.binomial(n=3, p=0.5, size=(100))
   pd.Series(coins).hist()

Exercise 5: More Coins
----------------------

In a short time, the coin game goes viral!

Create random numbers for 10000 series of coin tosses. Plot a histogram
of the results.

Exercise 6: More Tosses
-----------------------

The penguins get bored with the intial game, so they make each series
consist of more coin tosses.

Plot histograms for 4, 5 and 10 consecutive coin tosses.

Exercise 7: Cheating
--------------------

How do the histograms look like if the coin is not “fair”?

Exercise 8: Race
----------------

The penguins are having a race. They start running along a circular race
course. After every lap, there is a 50% chance that a penguin is
exhausted and stops.

Create random data for how many laps each of 100 penguins finishes.

::

   import numpy as np
   import pandas as pd

   laps = np.random.geometric(p=0.5, size=(100))
   pd.Series(laps).hist()

Exercise 9: More penguins
-------------------------

The race becomes super popular.

Create a random result for 10000 penguins and plot them as a histogram.

Exercise 10: Training
---------------------

Next season, the penguins train well for their race. The probability of
exhaustion drops to 10%.

Plot the histogram again.

Also plot the results of the penguin kids race, where 90% of the
penguins get finish after each lap.

Exercise 11: Dating
-------------------

The portal **“Hot on Ice”**, a dating website for penguins has the
following slogan:

::

   Every 11 minutes two penuins find a match on HoI!

How many couples fall in love within an hour? Create random numbers for
100 hours. Plot the results as a histogram.

You can use the following code:

::

   import numpy as np
   import pandas as pd

   couples_per_hour = 60 / 11    
   couples = np.random.poisson(couples_per_hour, size=100)
   pd.Series(couples).hist()

Exercise 12: Scale
------------------

**“Hot on Ice”** runs for a long time as a stable business without a lot
of changes. Repeat the calculation for 10000 hours.

Plot the histogram again.

Exercise 13: Mating Season
--------------------------

It is mating season! **“Hot on Ice”** becomes hugely popular. Now, 5
couples find each other every 11 minutes.

Plot the histogram for the mating season.

However, after the mating season, the penguins don’t need the portal any
more. The match rate drops to 1 penguin per hour. Plot that histogram
again.

Exercise 14: Conversion Rate
----------------------------

On a shopping website, a visitor who places an item in the shopping
basket, there is a 0.2 probability that they will proceed to the
checkout and buy something.

If 10 visitors place an item in the basket, what is the probability that
exactly one will make a purchase?

What is the probability that at least one will make a purchase?

Exercise 15: Emergency Calls
----------------------------

The phone line of the emergency service receives on average 11.2 calls
per hour.

Calculate the probability that there will be exactly 6 incoming calls
within one hour.

Calculate the probability that there will be 14 or more calls.

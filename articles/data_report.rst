
Exploratory Data Analysis
=========================

The goal of this project is to characterize a dataset on 5-10 pages.
You have explored the data and would like to share your initial findings.
Assume your readers know nothing about the data yet

.. topic:: What makes a good data report?

   A data report summarizes a body of data so that other people can understand what is in the data.
   A good report is **focused**: it answers a few questions accurately, but not more.
   It is **concise**: the report cuts out unnecessary detail.
   It is **objective**: it describes observations sticking close to the facts, but does not judge or come to conclusions that are not supported by the facts.
   A good report is 90% stating what is undebatable and 10% offering possible interpretations.

   Here, you find a structure and recipe for a data report.

Title
-----

Pick an interesting title. This is completely up to you.

Structure
---------

Use the following section headings:

* Abstract
* Introduction
* Data and Methods
* Results
* Conclusions
* References

Abstract
--------

Summarize the goal and main outcome(s) in up to 150 words.

Introduction
------------

*(about 10% of the text)*

In the Introduction, provide a short motivation for the study.
Cover the following points:

* What is the topic?
* Why is the topic important?
* What is the main goal?
* Enumerate 3-6 questions that the report will answer.
* What have other people done (in a thesis, this is a major part, here you can keep it to a minimum)

Example:

::

    Which penguin species has the longest beaks?

----

Data and Methods
----------------

*(up to 10% of the text)*

* you **must** reference the source of the data here. Provide the full URL and/or doi.
* what is the format of the data?
* how many tables / rows / columns does the data consist of?
* which columns exist in the data?
* what do the columns contain (in a few words)
* are there missing values?


Briefly enumerate the tools you used (anything that goes beyond MS Office).


Results
-------

*(at least 50% of the text)*

Most of the results is about describing the data using standard statistical tools.
90% of the text is describing what you can directly observe. 
Use your observations to answer the questions from the Introduction.

A good Results section consists of many simple sentences like:

::

    The mean beak size of Adelie penguins is 38.79 cm.

The remaining 10% is adding your own explanation and interpretation.
Make sure it is recognizable as such, e.g.:

::

    One possible explanation is that a long beak
    helps the penguin catch fish.

Characterize categorical columns
++++++++++++++++++++++++++++++++

For each categorical column, cover the following:

* how many unique values are there?
* what are the most frequent values?
* how are the values distributed?
* are there any major subgroups?

Characterize numerical columns
++++++++++++++++++++++++++++++

For each numerical column, cover the following:

* describe dispersion and spread
* are there any outliers?
* what is the distribution of the data?
* are there any major subgroups?

Relationships between columns
+++++++++++++++++++++++++++++

Examine relationships between two or more columns using a few of:

* are the columns correlated or statistically independent?
* calculate correlation coefficients
* calculate a linear fit
* calculate conditional probabilities
* show time dependency if there is a time axis
* do particularly strong correlations exist among subgroups?

Here you can also apply advanced statistical tools (clustering, ANOVA, hypothesis tests, PCA, ML models). This is completely optional since they were not covered in the course.

Answer the questions
++++++++++++++++++++

Directly answer the initial questions. Ideally answer one question per subsection:

::

    The beaks of Chinstrap penguins are longer
    than those of Gentoo penguins
    and much longer than those of Adelie penguins.

Discussion
----------

You may include a brief discussion, where you compare your results to other existing work.
You can interpret your results here, adding domain expertise.
Also this is a good place to mention ideas for further work.


Figures
-------

Include around 5 plots in the report (mostly in the Results section).
It is sufficient to choose from the following:

* bar plot
* line plot
* histogram
* box plot
* scatterplot
* heatmap

Make sure every plot has labeled axes and a caption.

Having a few well-prepared plots is better than many so-so ones.
A part of the assignment is to decide which plots you want to share.
Showing 20 plots instead of 5 does not make the report better.

Tables
------

Use tables if they help you to explain the data (mostly in the Results section).
Examples:

* columns in the dataset
* example entries
* measures of centrality and dispersion for different groups

Make sure the tables are not too large.
In a short report you rather would not want to have tables that span 1 page or more.

Conclusions
-----------

*(5% of the text or less)*

At the end of the report, summarize everything.
Briefly answer each of the questions from the Introduction.
E.g.:

::

    Of all penguins examined, Chinstrap penguins have the longest beaks.

Point out limitations of the work, ideas for further work.
This is also where you can place what you believe but cannot prove.

The Conclusions may repeat things that are also written in the Abstract.

References
----------

At the end of the report, list external sources. 
This list **must** contain a reference to the data source.
It may contain links to articles, papers, web pages and other sources of information.
When available, include the **DOI (digital object identifier)** in the citation. 

Use **scientific citation style**.


Assessment Criteria
-------------------

Working through the points above systematically and carefully will give you a good grade.
Here are the exact criteria I will use for evaluation:

* concise: 5-10 pages
* focus on main questions
* informative title
* abstract (up to 150 words)
* introduction
* data and methods
* objective: describes observations sticking close to the facts
* characterize categorical columns
* characterize numerical columns
* relationships between columns are described
* figures: ~5 plots (bar, line, histo, scatter, box, heatmap)
* conclusions
* references
* other excellent material (an advanced statistical method, infographic, animation, online dashboard, video or similar; up to 2 points)


.. seealso::

   `the 2022 PyConDE talk by Paula Gonzales <https://www.youtube.com/watch?v=_XvD83yhe3E>`__ for some inspiration.


.. hint::

   You can use a very similar structure to develop a BSc or MSc thesis.

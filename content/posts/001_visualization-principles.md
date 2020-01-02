title: Data visualization principles
date: 2020-1-1 20:05
category:
tags:
slug: data-visualization-principles
author: Alex Gonzalez
summary: Conveying meaning through data visualization is not an easy task. Here is how you might get started.
header_cover: images/data-visualization/data-viz.jpeg
status: published



When designing a visualization, there are usually four main topics that the author would want to highlight:

#### Comparison

These are used to compare the magnitude of values to each other and to easily identify the lowest or highest values in the data.

If you want to compare values over time, line or bar charts are often the best option and their choice depends on the number of periods you would like to analyze.
However, for comparisons among items, bar or column charts are preferred. Line charts provide a sense of continuity that might not be meaningful for categories. Faceted charts are also a good option when dealing with many categories.
You can use pie charts for comparison as well, although the length of a column or bar is usually better at displaying differences in your data than the angle of a pie chart.

#### Composition

Composition charts are used to see how a part of your data compares to the whole, and can show relative and absolute values. They can be used to accurately represent both static and time-series data.

For static data, a pie chart can do the job. However, there also other options that can tell the same story, such as a stacked bar chart, a waterfall chart or a tree map.
For time-based data, the number of periods is again a decisive factor when choosing your chart. You can visualize composition over many periods with area charts, which are very similar to line charts, and stacked bar or column charts when you have a reduced amount of periods.
It is important to consider that time-based visualization should be ordered chronologically as a general rule, and not by highest value, for example.

#### Distribution

When studying how quantitative values are located along an axis, distribution charts are the way to go. By looking at the shape of the data, the user can identify features such as value range, central tendency and outliers.

With this charts, the interest is in the full picture of the data and this can lead to having many data points (note: not categories!). In these cases, it's often better to use a line histogram, while column histograms are great for few data points.
In any case, when analyzing distribution for two variables at once, a scatter plot allows to compare between the full picture of two dimensions.

#### Relationship

Relationship charts have a constrained set of options as normally scatter plots are the only adequate way of presenting the data. They are used to find correlations, outliers, and clusters in your data.

While the human eye can only appreciate three dimensions together, you can visualize additional variables by mapping them to the size, color or shape of your data points.

<!-- 
See the image below for reference:

![Visualization Best Principles](../images/data-visualization/chart-viz.png) -->


> As a bonus tool, if you run into issues trying to find the best set of colors for your report or chart, make sure to check out [ColorHex](https://www.colorhexa.com/). This is a web app that provides color scales, palettes and blends based on the color of your choice.
>
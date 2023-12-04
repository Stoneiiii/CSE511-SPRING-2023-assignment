# Introduction & Background

In the first phase of this project, you learned to run multiple spatial queries on the large geo-database of the taxi firm that hired you. Now, the firm has contacted you again to extend the solution. Your team now needs to perform further analysis for them by locating passenger hot spots. There is also a Bonus opportunity of 20% grade points in this phase of the project as well.

# Problem Description

In this phase of the project, you are required to do spatial hot spot analysis. In particular, you need to complete two different hot spot analysis tasks.

- Hot zone analysis: This task will need to perform a range join operation on a rectangle datasets and a point dataset. For each rectangle, the number of points located within the rectangle will be obtained. The hotter rectangle means that it includes more points. So this task is to calculate the hotness of all the rectangles.
- Hot cell analysis : This task will focus on applying spatial statistics to spatio-temporal big
data in order to identify statistically significant spatial hot spots using Apache Spark.

The topic of this project phase is inspired from ACM SIGSPATIAL GISCUP 2016. Though we have special requirements in this assignments which are different from the GIS Cup. Please find the following references on the problem description:

- A detailed problem definition is available [here](http://sigspatial2016.sigspatial.org/giscup2016/problem)
- Evaluation Instructions are available [here](http://sigspatial2016.sigspatial.org/giscup2016/submit)

# Problem Statement

As stated in the Problem Definition page, in this task, you are asked to implement a Spark program to calculate the Getis-Ord statistic of NYC Taxi Trip datasets. We call it "Hot cell analysis". To reduce the computation power need, we made the following changes:

- The input will be a monthly taxi trip dataset from 2009 - 2012. For example, yellow_tripdata_2009-01_point.csv , yellow_tripdata_2010-02_point.csv 
- Each cell unit size is 0.01 * 0.01 in terms of latitude and longitude degrees.
- You should use 1 day as the Time Step size. The first day of a month is step 1. Every month has 31 days.
- You only need to consider Pick-up Location.
- We don't use Jaccard similarity to check your answer. However, you don't need to worry about how to decide the cell coordinates because the code template generated cell coordinates. You just need to write the rest of the task.
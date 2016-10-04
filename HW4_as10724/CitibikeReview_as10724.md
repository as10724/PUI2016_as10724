##HW4 Assignment 1

Reviewer: Avikal Somvanshi (as10724)

Date: 10/02/2016

#a) Verify the formulation of the Null and alternative hypotheses

    Both the NULL and alternative hypotheses are correctly formulated.

#b) Verify that the data supports the project

    The project aims to compare trip durations of older riders (75 percentiles and above of total ridership) with the rest of the ridership therefore it is critical scan the data for clerical errors and abnormalities. The description of the data notes that the age of the oldest rider is 116 years, which a quick google search reveals that there are only three people (interestingly all are women) in world of that are 116 years old right now and they live in Japan, Italy and Jamaica respectively. It is highly unlikely any of these ladies travelled across seas to NYC last year and took a ride on Citi Bike. For instance, in my own project which was based on gender noted that 5,695 entries in the data set had no gender assigned even after removing NaN. Thus, it would be helpful to the analysis if a further clean the data for anomalies by assuming an upper cut off age. 
    
    Visualisation of the data can be improved by normalising the data set and plotting overlapping histograms, instead of two separate histograms. 

#c) Recommendation for an appropriate test to test the NULL hypothesis

    The project compares two independent groups on same variable (trip durations) therefore it would be best to use t-test for testing validity of the NULL hypothesis.

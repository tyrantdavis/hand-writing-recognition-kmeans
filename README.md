# Building a K-Means Model - Hand Writing Recognition

## Introduction
Since 1999, the U.S. Postal Service has been at the forefront of utilizing machine learning and scanning technologies. With the immense task of processing around half a billion pieces of mail daily, they have invested significant effort into researching and creating highly effective algorithms that can accurately read and interpret addresses. This innovation isn't limited to the postal service alone; various other applications have emerged in different sectors.

For instance, ATMs have been designed to recognize handwritten bank checks, making transactions smoother for users. Similarly, Evernote has developed the capability to identify handwritten task lists, helping individuals keep track of their to-dos more efficiently. Expensify also employs this technology to recognize handwritten receipts, streamlining expense reporting for users. These advancements showcase the versatility of machine learning in everyday applications.

So, how do these systems achieve such remarkable feats? This project delves into K-means clustering, the algorithm that powers this impressive technology. By using scikit-learn, there is an opportunity to cluster images of handwritten digits, gaining insight into the underlying processes that enable these applications to function effectively.

This project will scope, analyze, prepare, plot data, and seek to explain the findings from the analysis.

**Data Sources:**

- [Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits)


## Project Goals
The aim of this project is to group images of handwritten numbers together using a kmeans model.



#### Why use a multiivariate forecasting algorithm to predict future energy output?
K-means clustering is a technique used in unsupervised machine learning that organizes similar data points into clusters, helping to uncover underlying patterns within the dataset, which aligns well with the objectives of this project. 

## Data
A digits dataset containing 1797 records that can be used to train the machine-learning model has been found. 


## Conclusions
- Label 3 has the highest count.
  
The model struggled with accurately identifying handwritten digits, suggesting that there is potential for enhancing its predictive abilities. It seems that the challenges lie more with the handwritten data itself rather than the model's performance. Recall that the model was developed using handwritten digits collected from 30 different individuals in Turkey.
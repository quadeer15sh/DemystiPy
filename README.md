# DemystiPy

This is a python module created for the purpose of visualizing and demystifying the statistical and machine learning concepts and algorithms used in the day to day life. For internalizing what is happening behind the scenes in these tools it is important to visualize them. The current version of the DemystiPy module offers the evaluation and visualization of the probability distribution functions which runs on top of the scipy python module to evaluate and visualize the Binomial and Gaussian probability distributions. 

## Installation

Run the following to install:

'''
pip install DemystiPy
'''

## Requirements

Numpy
Scipy
Matplotlib

## Usage

from DemystiPy.pdistributions import Binomial, Gaussian

b = Binomial()
g = Gaussian()

## Calculate probability mass function and cumulative density function for a binomial distribution
### e.g. P( X = 8) where no. of trials n = 15 and probability p = 0.35
b.pmf(8,15,0.35) 

e.g. P( X < 7) where no. of trials n = 15 and probability p = 0.35
b.cdf(6,15,0.35)

### e.g. P( X > 9) where no. of trials n = 15 and probability p = 0.35
b.cdf(9,15,0.35,upper=True)

### e.g. P( 5 < X < 10) where no. of trials n = 15 and probability p = 0.35
b.cdf2([5,9],15,0.35)

## Calculate cumulative density function and percentile point function for a gaussian/normal distribution
### e.g. P( X = 40 ) mean = 30 std_dev = 4
g.cdf(40,30,4)

### e.g. P( X > 21 ) mean = 30 std_dev = 4
g.cdf(21,30,4,lower=True)

### e.g. P( 30 < X < 35 ) mean = 30 std_dev = 4
g.cdf2([30,35],30,4)

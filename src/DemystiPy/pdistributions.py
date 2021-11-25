from scipy.stats import binom, norm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,6)
plt.rcParams.update({'font.size': 12})

class Binomial:

    """
    A class to represent the Binomial Distribution.

    ...

    Attributes
    ----------
    probabilities : list
        List of probabilities for each bernoulli trial
    mean : float
        Average number of occurences based on the binomial distribution
    var : float
        Variance of the binomial probability distribution

    Methods
    -------
    pmf(x,n,p,visualize,fill_color):
        Returns the probability mass function of the distribution
    cdf(x,n,p,visualize=True,fill_color,upper):
        Returns the cumulative density function for the number within the number of trials in the distribution
    cdf2(x,n,p,visualize=True,fill_color):
        Returns the cumulative density function for the interval within the number of trials in the distribution
    """
    
    def __init__(self):
        self.probabilities = None
        self.mean = None 
        self.var = None 
        
    def pmf(self,x,n,p,visualize=True,fill_color='orange'):

        '''
        Return the Probability Mass Function for a given number of trials

            Parameters:
                    x (int): Binomial discrete value
                    n (int): Number of trials
                    p (float): Probability of the occurence of an event
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): color of the mass function

            Returns:
                    pmf (float): Returns the probability mass function for a given number for the specified number of bernoulli trials

        '''

        r_values = list(range(n + 1))
        self.mean, self.var = binom.stats(n, p)

        self.probabilities = [binom.pmf(r, n, p) for r in r_values]

        prob_x = binom.pmf(x, n, p)
        
        if visualize:
            bars = plt.bar(r_values, self.probabilities)
            bars[x].set_color(fill_color)
            plt.xticks(r_values)
            plt.xlabel('x')
            plt.ylabel('Probability')
            plt.title("Probability Mass Function")
            plt.show()

        return prob_x
    
    def cdf(self,x,n,p,visualize=True,fill_color='orange',upper=False):

        '''
        Returns the Cumulative Density Function for a given number of trials

            Parameters:
                    x (int): Binomial discrete value
                    n (int): Number of trials
                    p (float): Probability of the occurence of an event
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): color of the mass function
                    upper (bool): Boolean variable to indicate upper half of the function

            Returns:
                    cdf (float): Returns the cumulative density function for a given number for the specified number of bernoulli trials

        '''

        r_values = list(range(n + 1))
        self.mean, self.var = binom.stats(n, p)

        self.probabilities = [binom.cdf(r, n, p) for r in r_values]

        prob_x = binom.cdf(x, n, p) if not upper else 1-binom.cdf(x, n, p)

        if visualize:
            bars = plt.bar(r_values, self.probabilities)
            if not upper:
                for i in range(x+1):
                    bars[i].set_color(fill_color)
            else:
                for i in range(x+1,n+1):
                    bars[i].set_color(fill_color)
            plt.xticks(r_values)
            plt.ylabel('x')
            plt.ylabel('Probability')
            plt.title("Cumulative Density Function")
            plt.show()

        return prob_x
    
    def cdf2(self,x,n,p,visualize=True,fill_color='orange'):

        '''
        Returns the Cumulative Density Function for a given number of trials between two specified values

            Parameters:
                    x (list): interval between which the cdf needs to be calculated e.g. 3<x<=8 [4,8]
                    n (int): Number of trials
                    p (float): Probability of the occurence of an event
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): color of the mass function
                    upper (bool): Boolean variable to indicate upper half of the function

            Returns:
                    cdf2 (float): Returns the cumulative density function for the given interval for the specified number of bernoulli trials

        '''

        r_values = list(range(n + 1))
        self.mean, self.var = binom.stats(n, p)

        self.probabilities = [binom.cdf(r, n, p) for r in r_values]
        
        try:
            prob_x = binom.cdf(x[1], n, p) - binom.cdf(x[0], n, p)

            if visualize:
                bars = plt.bar(r_values, self.probabilities)
                for i in range(x[0],x[1]+1):
                    bars[i].set_color(fill_color)
                plt.xticks(r_values)
                plt.xlabel('x')
                plt.ylabel('Probability')
                plt.title("Cumulative Density Function")
                plt.show()

            return prob_x
        
        except TypeError:
            raise TypeError("Input Parameter must be a list")


class Gaussian:

    """
    A class to represent the Gaussian/Normal Distribution.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    cdf(x,n,p,visualize=True,fill_color,upper):
        Returns the cumulative density function for the area under the curve of a normal distribution
    cdf2(x,n,p,visualize=True,fill_color):
        Returns the cumulative density function for the area under the curve within the interval of the normal distribution
    ppf(self,prob,mu,sigma,visualize,fill_color):
        Returns the percent point function or the inverse of the cdf
    """
    
    def __init__(self):
        pass

    def cdf(self,x,mu,sigma,visualize=True,fill_color='lightblue',upper=False):

        '''
        Returns the Cumulative Density Function for a given continous variable

            Parameters:
                    x (float): continous value
                    mu (float): Mean of the Gaussian Distribution
                    sigma (float): standard deviation of the Gaussian Distribution
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): Shaded color of the area under the curve
                    upper (bool): Boolean variable to indicate upper half of the function

            Returns:
                    cdf (float): Returns the cumulative density function for the area under the curve for a given continous variable 

        '''

        prob = norm.cdf(x, mu, sigma) if not upper else 1-norm.cdf(x, mu, sigma)

        if visualize:
            s = np.random.normal(mu, sigma, 1000)
            s.sort()
            x = np.arange(s[0], x, 0.01) if not upper else np.arange(x, s[-1], 0.01)
            plt.plot(s, norm.pdf(s, mu, sigma))
            plt.xlabel('x')
            plt.ylabel('Probability')
            plt.title("Cumulative Density Function")
            plt.fill_between(x, norm.pdf(x, mu, sigma),color=fill_color)
            plt.show()

        return prob

    def cdf2(self,x,mu,sigma,visualize=True,fill_color='lightblue'):

        '''
        Returns the Cumulative Density Function for the interval between two continous variables

            Parameters:
                    x (list): A list of two continous values
                    mu (float): Mean of the Gaussian Distribution
                    sigma (float): standard deviation of the Gaussian Distribution
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): Shaded color of the area under the curve

            Returns:
                    cdf2 (float): Returns the cumulative density function for the area under the curve for a given interval of continous variables

        '''


        prob1 = norm.cdf(x[0], mu, sigma)
        prob2 = norm.cdf(x[1], mu, sigma)
        prob = prob2 - prob1


        if visualize:
            s = np.random.normal(mu, sigma, 1000)
            s.sort()
            x = np.arange(x[0], x[1], 0.01)
            plt.plot(s, norm.pdf(s, mu, sigma))
            plt.xlabel('x')
            plt.ylabel('Probability')
            plt.title("Cumulative Density Function")
            plt.fill_between(x, norm.pdf(x, mu, sigma),color=fill_color)
            plt.show()

        return prob
    
    def ppf(self,prob,mu,sigma,visualize=True,fill_color='lightblue'):

        '''
        Returns the Percent Point Function or the Inverse CDF

            Parameters:
                    x (float): probability value
                    mu (float): Mean of the Gaussian Distribution
                    sigma (float): standard deviation of the Gaussian Distribution
                    visualize (bool): Boolean variable to visualize the distribution plot
                    fill_color (str): Shaded color of the area under the curve

            Returns:
                    ppf (float): Returns the percent point function or the inverse cdf

        '''
    
        val = norm.ppf(prob, mu, sigma)

        if visualize:
            s = np.random.normal(mu, sigma, 1000)
            s.sort()
            x = np.arange(s[0], val, 0.01)
            plt.plot(s, norm.pdf(s, mu, sigma))
            plt.xlabel('x')
            plt.ylabel('Probability')
            plt.title("Percent Point Function")
            plt.fill_between(x, norm.pdf(x, mu, sigma),color=fill_color)

        return val
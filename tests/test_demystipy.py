from DemystiPy.pdistributions import Binomial, Gaussian

b = Binomial()
g = Gaussian()

b.pmf(4,6,0.83,visualize=False)

b.cdf(4,6,0.83,visualize=False)

b.cdf2([2,5],6,0.83,visualize=False)

g.cdf(512,520,112,visualize=False)

g.cdf2([512,530],520,112,visualize=False)

g.ppf(0.43,520,112,visualize=False)
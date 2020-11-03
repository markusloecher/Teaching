#get a quantile:
stats.t.ppf(0.975,10)

#reproduce p-value:
n1 = len(firsts.prglngth.values)
n2 = len(others.prglngth.values)
pVal = 2*(1-stats.t.cdf(1.3802,n1+n2-2))
pVal
#n1+n2
mu0=30
empirical_mean = np.mean(cars4.mpg)
#assume the claim is true !!
shift = mu0-empirical_mean
print(shift)
cars4Shifted= cars4.mpg+shift
bs_mean_mpg = draw_bs_reps(cars4Shifted,np.mean,10000)
#The test statistic
TS = bs_mean_mpg-mu0

plt.hist(TS)
pVal = np.mean( TS < -shift)
#np.percentile(bs_mean_mpg,5)
print("pValue =", pVal)
#p value is simply the left tail beyond xBar
#np.mean(bs_mean_mpg < empirical_mean)
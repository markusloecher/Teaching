# Construct arrays of data: campaigns A and B
clickthroughA = np.array([True] * 45 + [False] * (500-45))
clickthroughB = np.array([True] * 67 + [False] * (500-67))

obsDiff = np.mean(clickthroughB)-np.mean(clickthroughA)

# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(clickthroughB, clickthroughA, diff_of_means, 10000)

plt.hist(perm_replicates)
#how do I add the vertical line again ?

#p-value:
np.mean(perm_replicates >obsDiff)

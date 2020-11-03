Women1 = WomenOnly[WomenOnly["pclass"]==1].survived
Women2 = WomenOnly[WomenOnly["pclass"]==2].survived

obsDiff = np.mean(Women1)-np.mean(Women2)

# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(Women1, Women2, diff_of_means, 10000)

#p-value:
np.mean(perm_replicates >obsDiff)
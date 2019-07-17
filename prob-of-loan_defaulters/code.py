# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=(df[df['fico']>=700]).count().sum()/df.count().sum()
print(p_a)

p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

df1=(df[df['purpose']== 'debt_consolidation'])

p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(path)
prob_lp=(df[df['paid.back.loan']== 'Yes']).count().sum()/df.count().sum()
print(prob_lp)

prob_cs = df[df['credit.policy']== 'Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df=(df[df['paid.back.loan']== 'Yes'])

prob_pd_cs = new_df[new_df['credit.policy']== 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)





# code ends here


# --------------
# code starts here
purpose=df['purpose']
plt.bar(purpose, height=purpose.count().sum())
plt.show()

df1=(df[df['paid.back.loan']== 'No'])

plt.bar(purpose, height=df1.count().sum())
plt.show()

# code ends here


# --------------
# code starts here
inst_median=np.median(df.installment)
inst_mean=np.mean(df.installment)

plt.hist(df.installment, bins=50)
plt.show()



# code ends here



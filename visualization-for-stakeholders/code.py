# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here
data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
plt.figure(figsize=[14,8])

plt.xlabel("loan status")
plt.ylabel("no of people ")

# title the plot
plt.title("loan_status(y/n)")

# build and show the plot
loan_status.plot(kind='bar')



# --------------
#Code starts here
data.count()
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
ig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']


#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')


#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_2.set(title='Coapplicant Income')


#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_3.set(title='Total Income')


#Code ends here



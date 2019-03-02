import pickle

f = open(r"e:\classroom\ds\jan21\loan_model.pkl","rb")
model = pickle.load(f)

# take input from user
amount = int  (input("Enter Loan Amount         : "))
income = int  (input("Enter Applicant Income    : "))
cincome = int (input("Enter Co.Applicant Income : "))
term  = int   (input("Enter Loan Term           : "))

X_test = [[income,cincome,amount, term]]

y = model.predict(X_test)

if  y[0] == 'Y':
   print("Yessssss")
else:
   print("Noooooooooo")




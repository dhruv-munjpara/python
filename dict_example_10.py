# compriansive
# dict1={1:0,2:0,3:0,4:0}
# dict2={k:k**2 for k in dict1.keys()}
# print(dict2)


# state_capital={"gujrat":"gandhinagar","rajastan":"jaipur","maharstra":"mumbai","orrisa":"bhuneshwar"}
# state_capital_len={k:len(k) for k,v in state_capital.items()}
# print(state_capital_len)
# state_capita_upper={k:v.upper() for k,v in state_capital.items()}
# print(state_capita_upper)






# state_capital={"gujrat":"gandhinagar","rajastan":"jaipur","maharstra":"mumbai","orrisa":"bhuneshwar"}
# state_capital_upper={k:v.upper() for k,v in state_capital.items() if len(k)>7}
# print(state_capital_upper)



# state_capital={"gujrat":"gandhinagar","rajastan":"jaipur","maharstra":"mumbai","orrisa":"bhuneshwar"}
# state_capital_upper_or_lower={k:v.upper() if len(v)>7  else v.lower() for k,v in state_capital.items() }
# print(state_capital_upper_or_lower)



dict1={1:"",2:"",3:"",4:""}
dict2={k:"even" if k%2==0 else "odd" for k,v in dict1.items()}
print(dict2)

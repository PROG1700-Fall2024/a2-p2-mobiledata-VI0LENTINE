#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: W0516070     
#Student Name: Valentine Byrnes

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #INPUT - Data Usage
    usage = int(input("Enter data usage: "))

    #CALCULATE + OUTPUT: Calculate rate of charge and output total charge
    if usage <= 200:
        flat_rate = 20
        print("Total charge is: ${0:.2f}".format(flat_rate))
    
    elif usage > 200 and usage <= 500:
        per_Mb = usage * 0.105
        print("Total charge is: $ {0:.2f}".format(per_Mb))

    elif usage > 500 and usage <= 1000:
        per_Mb = usage * 0.110
        print("Total charge is: ${0:.2f}".format(per_Mb))

    else:
        flat_rate = 118
        print("Total charge is: ${0:.2f}".format(flat_rate))

    # YOUR CODE ENDS HERE

main()
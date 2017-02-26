#Last semester you wrote a Python program to determine whether a medication order for acetaminophen was appropriate.
#..,In this assignment, you'll need to modify that program to include the following:
#-(done) A function that accepts a patient's age, dose, frequency, and weight (or None by default) and returns true if the dose is acceptable and false if the dose is not.
#-(done) A loop to continue asking for dose input until the user enters "STOP."
#-(done) A dictionary that contains elements for the input age, dose, frequency, and weight
#-(done) A list that captures the dictionary within each loop iteration

#intialize patient dictionary with 'None' default values
patientDict={}
patientDict.setdefault('patientAge', None)
patientDict.setdefault('patientDose', None)
patientDict.setdefault('patientFreq', None)
patientDict.setdefault('patientWeight', None)

#intialize patient List, which will then capture the patient dictionaries
patientList=[]

####function to take in patient's age, dose, freq, and weight (in Kg)
def acetaminophen2(age, dose, freq, weight):
    patientDict['patientAge']=age
    patientDict['patientDose']=dose
    patientDict['patientFreq']=freq
    patientDict['patientWeight']=weight
    # recall: the input function is a string. Enter STOP. and not "STOP." in the Shell to not throw an error or loop infinitely!
    if dose!="STOP.":
    #conditional statements to return True if dose acceptable and False if dose not acceptable
        #check patient's age; if less than twelve, get dose as mg/kg
        if int(age) < 12:
            currDose=int(dose)/int(weight)
            if currDose <40: #dose is in mg/kg
                return False
            elif currDose>90:
                return False
            else:
                return True
        elif int(age) >= 12:
            if int(dose) <1300: #dose is in mg
                return False
            elif int(dose)>3250:
                return False
            else:
                return True
    else:
        print("STOP!")
    '''
    If dose=="STOP." from input, then print stop. Input the weight and dose,
    then the program will finish executing. Check the 'patientDict' and 'patientList'
    variables by entering them into the shell. Should work!
    '''
    
####Calling the function inside a while loop to keep asking for input until
#loop to update the patient dictionary and capture it in a list
while True:
    #if the input for dose is not to stop, keep asking for info and appending the dictionary
    if patientDict['patientDose']!="STOP.":
        y=acetaminophen2(input(), input(), input(), input())
        patientList.append(patientDict)
    #if the input for dose is "STOP.", then stop!
    elif patientDict['patientDose']=="STOP.":
        break

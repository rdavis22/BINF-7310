#Last semester you wrote a Python program to determine whether a medication order for acetaminophen was appropriate.
#..,In this assignment, you'll need to modify that program to include the following:
#-(done) A function that accepts a patient's age, dose, frequency, and weight (or None by default) and returns true if the dose is acceptable and false if the dose is not.
#- A loop to continue asking for dose input until the user enters "STOP."
#- A dictionary that contains elements for the input age, dose, frequency, and weight
#- A list that captures the dictionary within each loop iteration

####function to take in patient's age, dose, freq, and weight (in Kg)
def acetaminophen2(age, dose, freq, weight):
#conditional statements to return True if dose acceptable and False if dose not acceptable
    #check patient's age; if less than twelve, get dose as mg/kg
    if age < 12:
        currDose=dose/weight
        if currDose <40: #dose is in mg/kg
            return False
        elif currDose>90:
            return False
        else:
            return True
    elif age >= 12:
        if dose <1300: #dose is in mg
            return False
        elif dose>3250:
            return False
        else:
            return True

####Calling the function to meet the parameters of the project
#initialize patient list
patientList=[]
#initialize a dictionary to capture patient data
patientDict={}
#set default values to None
patientDict.setdefault('patientAge', None)
patientDict.setdefault('patientDose', None)
patientDict.setdefault('patientFreq', None)
patientDict.setdefault('patientWeight', None)

while patientDict['patientDose']!="STOP.":
    acetaminophen2(input(), input(), input(), input())
    #assign the value for 'patient" keys as the input values of the function
    patientDict['patientAge']=age
    patientDict['patientDose']=dose
    patientDict['patientFreq']=freq
    patientDict['patientWeight']=weight

    #append each dictionary to the patient list
    patientList.append(patientDict)

import numpy as np

#Write a function that accepts a numpy array and returns a new numpy array
#With just the odd values from the first array
def get_odd_values(some_array):
    solution = [num for num in some_array if num % 2 == 1]
    return np.array(solution) #Return a numpy array

#Write a function that accepts two numpy arrays
#and returns the common values in them as another numpy array
def find_common_values(np1, np2):
    return np.intersect1d(np1, np2)

#Write a function called F_to_C that accepts as a parameter a numpy array 
#and converts all the elements from Fahrenheit to Centigrade
#Then returns that converted array
def F_to_C(array_of_temperatures):
    #Iterate over the individual elements in the array
    #add try/except logic around the loop and return some 'flag' value in the case of an error
    try:
        for i in range(0, len(array_of_temperatures)):
        #Convert the element at index i to Centigrade
            array_of_temperatures[i] = (array_of_temperatures[i] - 32) * (5/9)
        return array_of_temperatures
    except:
        #There was an exception, we caught it, now we need to
        #Return a 'flag' value to indicate there was a problem
        return np.array([np.NaN]) #NaN = Not a Number
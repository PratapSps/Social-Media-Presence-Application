'''
Created on Jul 9, 2017

@author: pratap
'''
from sps import AppVariables

class BackEndProcess():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def googleUrl(self):
        '''
        Method which search google.com based on input provided by the user
        It creates dynamic link based on user input.
        '''
        AppVariables.FirstLast=AppVariables.First_Name_data +"+" +AppVariables.Last_Name_data
        if AppVariables.Middle_Name_data != "" :
            AppVariables.FirstMiddleLast=AppVariables.First_Name_data+"+"+AppVariables.Middle_Name_data+"+"+AppVariables.Last_Name_data
        
        if AppVariables.Country_data != "" :
            AppVariables.FirstLastCoun=AppVariables.FirstLast+"+"+AppVariables.Country_data
        
        if AppVariables.State_data != "" :
            AppVariables.FirstLastState=AppVariables.FirstLast+"+"+AppVariables.State_data
        
        if AppVariables.City_data != "" :
            AppVariables.FirstLastCity=AppVariables.FirstLast+"+"+AppVariables.City_data
            
        if AppVariables.School_Name_data != "" :
            AppVariables.FirstLastSchool=AppVariables.FirstLast+"+"+AppVariables.School_Name_data
        
        UniqueSearchURl=[]
        url1=""
        url2=""
        url3=""
        url4=""
        url5=""
        url6=""
        url1=AppVariables.googleBaseUrl+AppVariables.FirstLast
        if AppVariables.FirstMiddleLast!="":
            url2=AppVariables.googleBaseUrl+AppVariables.FirstMiddleLast
            
        if AppVariables.FirstLastCoun!="":
            url3=AppVariables.googleBaseUrl+AppVariables.FirstLastCoun  
            
        if AppVariables.FirstLastState!="":
            url4=AppVariables.googleBaseUrl+AppVariables.FirstLastState
            
        if AppVariables.FirstLastCity!="":
            url5=AppVariables.googleBaseUrl+AppVariables.FirstLastCity

        if AppVariables.FirstLastSchool!="":
            url6=AppVariables.googleBaseUrl+AppVariables.FirstLastSchool
        
        UniqueSearchURl.append(url1)
        if url2 != "":
          UniqueSearchURl.append(url2)
          
        if url3 != "":
          UniqueSearchURl.append(url3)

        if url4 != "":
          UniqueSearchURl.append(url4)
          
        if url5 != "":
          UniqueSearchURl.append(url5)
          
        if url6 != "":
          UniqueSearchURl.append(url6)  
        
        
        
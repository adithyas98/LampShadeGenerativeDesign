#!/usr/bin/env python3
import csv

class UserInput:
    '''
    Class will define methods to accept user input
    '''
    def __init__(self,qdict,intro):
        '''
        Input:
            - dictionary: A dictionary of inputs to ask the user
                - The dictionary should take the following form
                    Variable Code(code to access the answer)
                       (Create a sub dictionary)
                        - question: The Question to ask
                        - convert: pass in the conversion function
                                    pointer
            - intro: What you would like to start the questioning with
        '''
        self.intro = intro
        self.qdict = qdict
        self.fullDict = qdict  #Used once we have our answers

    def askQuestions(self):
        '''
        This method will ask the questions defined in the qdata
        Output:
            - the qdata dictionary with a data label containing the data
            as follows:
                    Variable Code(code to access the answer)
                       (Create a sub dictionary)
                        - question: The Question to ask
                        - convert: pass in the conversion function
                                    pointer
                        - data: Contains the data
        '''
        #Print out the intro paragraph
        print("{}\n".format(self.intro))
        #iterate through the keys and ask the questions
        for key in self.qdict.keys():
            #find the conversion function
            convert = self.qdict[key]['convert']
            ans = input("{}\n".format(self.qdict[key]["question"]))#ask the question
            #Now we need to convert the data then add it to the dict
            try:
                self.fullDict[key]['data'] = convert(ans)
            except:
                print("Something was wrong in the input you provided\n")
                print("Please try again by restarting the script")
                return 1

        #once we have done this for everything, we can return fullData
        return self.fullDict

    def outputQuestions(self,filename):
        '''
        This method will output the questions asked as a csv file
        Input:
            - filename: the name of the file to save the questions in
        Output:
            - A Saved CSV
        '''
        with open(filename,'w') as f:
            writer = csv.writer(f,delimiter=',')
            #write the csv header
            writer.writerow(['ID','Question','Input'])
            #iterate through all of the keys and add it to the csv file
            for key in self.qdict.keys():
                row = []
                row.append(key)
                row.append(self.qdict[key]['question'])
                row.append(" ")
                writer.writerow(row)
        #The file should now be saved
        return "Filed Saved to: {}".format(filename)



    def inputCSV(self,filename):
        '''
        This will retrieve the data from a user inputed csv file
        Input:
            - filename: fulle file path and filename of the csv input
        Output:
            - None.
            - Data will be stored in qdict
        '''
        #iterate through each of the rows and use the id to find where to store data
        with open(filename,'r') as f:
            reader = csv.reader(f,delimiter=',')
            next(reader)#Skip the row
            for row in reader:
                ID = row[0] #retrieve the ID
                try:
                    convert = self.qdict[ID]['convert']
                    self.fullDict[ID]['data'] = convert(row[2])
                #retrieve and store the data
                except:
                    print("Something was wrong in the input you provided\n")
                    print("Please try again by restarting the script")
                    return 1



        return self.fullDict







        

        

        

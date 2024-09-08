#Input and output:
#interslice(<text.file>) Takes a data or txt file as input 
#X_train, y_train, X_test, y_test = interslice(<text.file>)
#Outputs to 4 arrays^

import numpy as np
import random


#MODE can either be random or linear.  Linear splits 20% of the data off the end for testing.  Random randomly selects 20% of the data for testing. This will eventually be an argument.
MODE = "random"
input_file = "iris.data"

def interslice(input_file):
    data_file = np.loadtxt(input_file, dtype=str, delimiter=",")
    number_of_rows = int(data_file.shape[0])
    number_of_columns = int(data_file.shape[1])
    #print(data_file)
    #print(number_of_rows)
    #print(number_of_columns)
    rand_rows = []
    one_fifth_of_rows = int(0.20 * number_of_rows)
    i = 0
    while i < one_fifth_of_rows:
        rand_number = random.randint(0,number_of_rows)
        nope = 0
        for j in rand_rows:
            if rand_number == j:
                nope = 1
        if nope == 0:
            rand_rows.append(rand_number)
            i += 1
    print(rand_rows)
    i = 0
    #train = np.empty([120, 5])
    #test = np.empty([30, 5])
    X_train = np.zeros(shape = (int(number_of_rows - (number_of_rows * 0.2)), (number_of_columns - 1)), dtype=float)
    X_test = np.zeros(shape = (int(number_of_rows - (number_of_rows * 0.8)), (number_of_columns - 1)), dtype=float)
    y_train = np.loadtxt(input_file, dtype=str, delimiter=",")
    y_test = np.loadtxt(input_file, dtype=str, delimiter=",")
    y_train_list = []
    y_test_list = []
    
    #print(y_test[0,(number_of_columns -1)])
    #iprint(X_train.shape)
    #print(X_test.shape)
    test_iter = 0
    train_iter = 0
    while i < number_of_rows:
        for r in rand_rows:
            if (i == r and test_iter < 30):
                X_test[test_iter] = data_file[[r],0:(number_of_columns - 1)]
                y_test_list.append(y_test[rand_rows[test_iter], (number_of_columns - 1)])
                test_iter += 1
                #print(test_iter)
        if i != r:
            if train_iter < (number_of_rows - (number_of_rows * 0.2)):
                X_train[train_iter] = data_file[[i],0:(number_of_columns - 1)]
                y_train_list.append(y_train[train_iter, (number_of_columns - 1)])
                train_iter += 1
        i += 1

    #print(data_file[[0], :])
    #print(rand_rows)
    #print("****************************TRAIN************************")    
    print(X_train)
    print(y_train_list)
    #print(len(y_train_list))
    #print(y_train)
    #print("****************************TEST************************")    
    print(X_test)
    #print(y_test)
    print(y_test_list)
    #print(y_train_list)
interslice("iris.data")

        






import numpy as np
import pandas as pd

grades_file = pd.read_csv('/Users/urvijoshi/Desktop/UB/Sem 2/PFA/grades.csv')

# replace null or missing values with 0
grades_file = grades_file.replace(np.nan, 0)

# save the modified DataFrame back to a CSV file
grades_file.to_csv('grades.csv', index=False)

def gradeInfo(filename, numExams, hwWeight):

    # (a) calculate average score for HW1
    ansA = grades_file['HW1'].mean()

    # (b) sort grades for HW2 in descending order

    ansB = grades_file[['ID', 'HW2']].sort_values('HW2', ascending=False).to_numpy()

    # (c) find students who scored 90 or above on both HW1 and HW3
    hw1_90 = grades_file[grades_file['HW1'] >= 90]['ID']
    hw3_90 = grades_file[grades_file['HW3'] >= 90]['ID']
    ansC = np.intersect1d(hw1_90, hw3_90)

    # (d) count number of students who scored 80 or below on HW1 and 90 or above on HW2
    ansD = grades_file[(grades_file['HW1'] <= 80) & (grades_file['HW2'] >= 90)].shape[0]

    # (e) calculate each student's weighted average score
    hw_weights = np.array([1.0] + [hwWeight] * (numExams-1))
    scores = grades_file.iloc[:, 1:].to_numpy()
    weighted_scores = np.round(np.sum(scores * hw_weights, axis=1), 1)
    id_scores = np.hstack([grades_file['ID'].to_numpy().reshape(-1, 1), weighted_scores.reshape(-1, 1)])

    return hw1_avg, hw2_desc, hw1_hw3_90, hw1_80_hw2_90, id_scores

print('a:')
print(ansA)

print('b:')
print(ansB)

print('c:')
print(ansC)

print('d:')
print(ansD)

print('e:')
print(ansE)

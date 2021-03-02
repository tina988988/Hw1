# hw1
(1)It creates an empty list space(data) to save the input data and another(target_data) for the target IDs which are chosen.
First, we add a csv file(108061216.csv for example) as an input and the code turns the information into a list.
Second, we choose the IDs(C0A880, C0F9A0, C0G640, C0R190, C0X260 for example) that we want to analize.
Then, it removes all '-99.000' & '-999.000' in 'WDSD' 
and finds out the maximum range in WDSD from target ID.
If the range is successfully found, the answer will be shown.
If failed, 'None' will be shown.
Briefly, we give it a csv file and choose the target ID we want, then the result(include ID) will be shown on the screen. 

(2)results:[['C0A880', 2.4], ['C0F9A0', 2.1], ['C0G640', 3.2], ['C0R190', 2.8], ['C0X260', 4.0]]

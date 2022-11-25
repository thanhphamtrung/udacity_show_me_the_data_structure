Because we do not know how deepth the directory is
so I think using recursion is the solution for this problem.
The solution is just loop recursively through the directory
till the path equal None
In each loop I check if we found the file with suffix, then append it to file_list
else get deeper in directory

Because this method traversing the input data recursively, this only visit each node once
- Time complexity: O(n)
- Space complexity: O(n^m) 
n: number of folder to file
m: number of directory in same folder


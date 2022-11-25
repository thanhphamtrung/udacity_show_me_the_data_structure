Because we do not know how deepth the directory is
so I think using recursion is the solution for this problem.
The solution is just loop recursively through the directory
till the path equal None
In each loop I check if we found the file with suffix, then append it to file_list
else get deeper in directory

Time complexity: O(n^2) because we need to loop over the all directory parts of the file 
then loop through all directory in same folder
ex: a/b/c/d.exe => we need to loop through a,b,c,d

- Time complexity: O(n^2)
- Space complexity: O(n^m) 
n: number of folder to file
m: number of directory in same folder


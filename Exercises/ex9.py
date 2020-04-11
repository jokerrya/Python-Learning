"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date)
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

exam_st_date = (11, 12, 2014)
print("%i / %i / %i"%exam_st_date)


str_date = str(exam_st_date)
new_str_date = str_date.replace(","," /")
a = new_str_date.replace("(","")
b = a.replace(")","")
print(b)
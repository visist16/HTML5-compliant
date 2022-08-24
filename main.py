from jinja2 import Template
import sys
import matplotlib.pyplot as plt

arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Template for student info
STemplate = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Student Data</title>
    </head>
    <body>
        <h1>Student Details</h1>
        <table border=1> 
            <tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
            {% for l1 in l %}
            <tr>
                <td>{{ l1["Student id"] }}</td>
                <td>{{ l1["Course id"] }}</td>
                <td>{{ l1["Marks"] }}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan=2 align="center">Total Marks</td>
                <td>{{ s }}</td>
            </tr>
        </table>
    </body>
</html>
"""

# template for course info 
CTemplate = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Course Data</title>
    </head>
    <body>
        <h1>Course Details</h1>
        <table border=1> 
            <tr>
                <td>Average Marks</td>
                <td>Maximum Marks</td>
            </tr>
            <tr>
                <td> {{ avg_marks }} </td>
                <td> {{ max_marks }} </td>
            </tr> 
         </table>
         <p> 
         <img src={{ img }} />
         </p>
    </body>
</html>
"""

#Template for wrong input
WTemplate = """ 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Something Went Wrong</title>
    </head>
    <body>
        <h1>Wrong Inputs</h1>
        <p>Something went wrong </p>
    </body>
</html>
""" 

def student_info(l,s):
    # l = list containing student id, course id and marks of student
    # s = sum of marks of a student
    template = Template(STemplate)
    content = template.render(l=l, s=s)
    output = open("output.html", "w")
    output.write(content)
    output.close()
    
    
def course_info(avg_marks, max_marks, img):   
    template = Template(CTemplate)
    content = template.render(avg_marks=avg_marks, max_marks=max_marks,img=img)
    output = open("output.html", "w")
    output.write(content)
    output.close()
    
def wrong_input():
    template = Template(WTemplate)
    content = template.render()
    output = open("output.html", "w")
    output.write(content)
    output.close()

f = open("data.csv", "r")
header = f.readline().strip().split(",") # extract header row
l = []
for row in f: # go through each row in file
    r = row.strip().split(",") # convert row into list
    d = {header[0]:r[0], header[1].strip():r[1].strip(), header[2].strip():r[2].strip()} # convert row into dictionary with respective header
    l.append(d)
f.close()

if __name__ == '__main__':
    li = []
    s = 0
    
    if arg1 == '-s':
        for r in l:
            if r["Student id"] == arg2:
                s += int(r["Marks"])
                li.append(r)     
        student_info(li, s)

    elif arg1 == '-c':
        for r in l:
            if r["Course id"] == arg2:
                li.append(r["Marks"])
                s += int(r["Marks"])
        try:
            avg_marks = s / len(li)
            max_marks = max(li)
            fig = plt.hist(li)
            plt.xlabel("Marks")
            plt.ylabel("Frequency")
            plt.savefig("abc.png")
            course_info(avg_marks, max_marks, "abc.png")
            
        except ZeroDivisionError:
            wrong_input()
            
        
    
    elif arg1 != "-s" or arg2 != '-c' or li == []:
        wrong_input()
        

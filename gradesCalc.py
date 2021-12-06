#### PART 1 ####
# calcGrade: Calculate the total final grade of a student
# student_id: the student's id as string
# avg: the student's homework averege as a string
def calcGrade(student_id: str, avg: str) -> int:
    length = len(student_id)
    sub = student_id[length-2:length]
    digits = int(sub)
    total = (digits+int(avg))//2
    return total

# nuoOfDigits: Calculates the number of digits that a integer number contains, and return it
# number: integer number 
def numOfDigits(number: int) -> int:
    n = int(number)
    count = 0
    while(n > 0):
        count = count+1
        n = n//10
    return count

# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    input_f = open(input_path, 'r')
    output_f = open(output_path, 'w')
    lines = input_f.readlines()
    dict = {}
    # get info from input and put in dict:
    for line in lines:
        line=line.replace(' ', '').replace('\n', '')
        info = line.split(',')
        student_id = info[0]
        name = info[1]
        semester = info[2]
        avg = info[3]
        if(student_id.isnumeric() and student_id[0] != '0' and numOfDigits(student_id)
           and name.isalpha()
           and semester.isnumeric() and int(semester) >= 1
           and avg.isnumeric() and int(avg) > 50 and int(avg) <= 100):
            dict[student_id] = avg

    totalgrade = 0
    # write the dict to the output file and calculate the course avg:
    for key, val in sorted(dict.items()):
        final_grade = calcGrade(key, val)
        totalgrade += final_grade
        line=", ".join((key,val,str(final_grade)))+'\n'
        output_f.write(line)

    # close files and return avg:
    input_f.close()
    output_f.close()
    return totalgrade//len(dict)
    raise NotImplementedError


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    hist1 = [0]*26
    hist2 = [0]*26
    s1 = s1.lower()
    s2 = s2.lower()
    for s in s1 :
        hist1[ord(s) - ord('a')] += 1
    for s in s2 :
        hist2[ord(s) - ord('a')] += 1
    for i in range(0, 26, 1) :
        if hist1[i] > 0 and hist2[i] == 0 :
            return False
        if hist1[i] > 0 and hist2[i] > 0 and hist1[i] > hist2[i] :
            return False
    return True
    raise NotImplementedError



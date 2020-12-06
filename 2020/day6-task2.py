# open data, split into groups
# with open("2020/day6testdata.txt") as f:
with open("2020/day6answers.txt") as f:
    groups = f.read().split("\n\n")

sum_of_counts = 0
for group in groups:
    same_answers = {}
    no_of_people = group.count("\n") + 1
    answers = group.replace("\n", "")
    
    # print(no_of_people)
    # print(answers)
    
    # create a count
    for answer in answers:
        # the number of answers == no_of_people == everyone provided that answer
        if answers.count(answer) == no_of_people:
            # use a dict to remove duplicates
            same_answers[answer] = True

    count = len(same_answers.keys()) 
    sum_of_counts += count

print(sum_of_counts)
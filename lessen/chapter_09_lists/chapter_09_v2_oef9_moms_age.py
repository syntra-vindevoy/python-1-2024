opdracht = '''
Exercise 9   Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits that make up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often this has happened over the years but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times so far. I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would happen one more time after that. In other words, it would have happened 8 times over all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string method zfill useful.
'''

# age_me = x - y
# age_mom = x
# 6 times reversable until now
# 8 times reversable in total

solutions = []
solution_count = 0
minimum_age_for_birth = 10
maximum_age_for_birth = 75
maximum_age = 110

solutions = []
for moms_age_at_birth in range(minimum_age_for_birth,maximum_age_for_birth):
    matching_ages = []
    for my_age in range (0,maximum_age):
        moms_age = my_age + moms_age_at_birth
        if str(my_age).zfill(2) == str(moms_age).zfill(2)[::-1]:
            matching_ages.append([my_age, moms_age])
    solutions.append(matching_ages)

for solution in solutions:
    if len(solution) == 8:
        match_8_solutions = solution
        break

print(solution)


print(f"zesde keer op leeftijd van {solution[5]}")
print(f"zevende keer op leeftijd van {solution[6]}")
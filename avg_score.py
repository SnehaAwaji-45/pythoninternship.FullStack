def average_score(marks):
    total=sum(marks)
    return total/len(marks)
def rating(score):
    if score>=90:
        return"Excellent"
    elif score>=75:
        return"Very Good"
    elif sccore>=60:
        return"Good"
    elif score>=40:
        return "Average"
    else:
        return"Needs improvement"

def bonus(score,salary):
        if score>=90:
            return salary*20/100
        elif score>=75:
            return salary*10/100
        else:
            return salary*5/100

marks=[92,80,83]
salary=50000
score=average_score(marks)
print("Average Score:",(score))
print("Rating:",rating(score))
print("Bonus:",bonus(score,salary))
                                

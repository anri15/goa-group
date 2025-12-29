# 4)მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group"
score = input("enter your score: ")
if score == 100:
    print("a group")
elif int(score) >= 80 or int(score) > 99:
    print("b group")
elif int(score) >= 40 or int(score) < 70:
    print("c group")
else:
    print("d group")
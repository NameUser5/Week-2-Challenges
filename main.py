print("Hello, student!")
first = input("Please enter your first name. ")
first = first.upper()
first_initial = first[0]

      #first = list() <--- This did not work. Difference b/t lists and indices?
last = input("Please enter your last name. ")
last = last.upper()
last_initial = last[0]

print(f"Thank you, {first_initial + last_initial}.")

number = input("From 0 to 100, what score did you get on the last test? ")
grade = float(number)
      #grade = int(number) <--- can I merge w/ floats?

      #type(grade)
      #float(grade)
      #class 'int'   <--- I tried all 3 of these. What was wrong?

if grade >= 0 and grade <= 60:
  print("F")
elif grade > 60 and grade <= 69:
  print("D")
elif grade > 69 and grade <= 79:
  print("C")
elif grade > 79 and grade <= 89:
  print("B")
elif grade > 89 and grade <= 100:
  print("A")
elif grade > 100 and grade <=150:
  print("You're a genius! You automatically pass!")
elif grade > 150:
  print("Stop trolling.")
elif grade < 0:
  print("...How??")
#elif grade == "-0":
 # print("...Are you okay?")

    #How do I loop to new inputs?
    #How do I prevent letters and other symbols from input?
    #What about decimals AND integers being accepted simultaneously? What about the length of the decimals?
    #How can I do: (79.5) -> "Aaah, so close to a B!" I know I'd have to switch the operators, but what else?
    #How can I format the text?



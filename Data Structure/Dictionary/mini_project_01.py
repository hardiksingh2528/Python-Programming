"""Project Description
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact on the screen.
Next, change a fact about one of the people.
Also add an additional person and corresponding fact.
Display the new list of people and facts.
Run the program multiple times and notice if the order changes.

Sample Output
Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

After modifying one fact and adding a new person:

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance."""

fact_dict = {"Mayank":"He sleeps most" ,
             "Hardik":"He cooks 2 times daily" ,
             "Kishan":"He is from chitrakoot"}
print("\n Original Info : ")
for name, fact in fact_dict.items():
    print(name,":",fact)
fact_dict["Kishan"]="He is from prayagraj"

fact_dict["Kuldeep"]="He is settled in Bhopal"
print("\n Updated Info : ")
for name, fact in fact_dict.items():
    print(name,":",fact)
# დაწერე რამე კითხვა მაგალითად ყველაზე მაღალი მწვერვალი სანამ “Everest” არ ჩაწერს ან “exit” ჩაეციკლოს და შეეკითხოს “ყველაზე მაღალი მწვერვალი”


for i in range(1000):
    question = input("what is the highest mountain: ")

    if question == "everest":
        print("correct")
        break
    elif question == "exit":
        print("programe stoped working")
        break

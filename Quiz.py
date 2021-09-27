import time
import json

superuser={'user': 'admin', 'password': 'admin'}

#user panel
def user_panel(name,mobile,email):
    with open('questions.json') as json_file:
        questions = json.load(json_file)
    
    with open('result.json') as json_file:
        result = json.load(json_file)
    
    print('\nTOPICS:')
    for i in questions.keys():
        print(i)
        
    topic=input('Enter topic you want to attend:')
    score=0
    
    for j in questions[topic].keys():
        print('\n',j,'.',questions[topic][j]['question'])
        print('Difficulty level:',questions[topic][j]['level'])
        print('\nOption 1:',questions[topic][j]['option1'])
        print('Option 2:',questions[topic][j]['option2'])
        print('Option 3:',questions[topic][j]['option3'])
        print('Option 4:',questions[topic][j]['option4'])
        ans=input('Enter the answer::')
        if ans=='1':
            res=questions[topic][j]['option1']==questions[topic][j]['answer']
        elif ans=='2':
            res=questions[topic][j]['option2']==questions[topic][j]['answer']
        elif ans=='3':
            res=questions[topic][j]['option3']==questions[topic][j]['answer']
        elif ans=='4':
            res=questions[topic][j]['option4']==questions[topic][j]['answer']
        else:
            res=False

        if res==True:
            score+=10
            print("Correct answer")
        else:
            print("Wrong answer")
            print("The correct answer is:",questions[topic][j]['answer'])
        time.sleep(2)

    print('\n*****Result*****')
    print('Name:',name)
    print('Mobile:',mobile)
    print('Email:',email)
    print('Marks scored:',score)
    
    result[len(result)+1]={'name':name,'mobile':mobile,'email':email,'topic':topic,'score':score}
    
    with open("result.json","w") as fi:
        json.dump(result,fi)
    
    temp=input('Do you want to attend other quiz:')
    if temp=='yes':
        user_panel(name,mobile,email)

#view results
def view_results():
    with open('result.json') as json_file:
        result = json.load(json_file)

    for i in result.keys():
        print(i,'.',end=' ')
        print('Name:',result[i]['name'],end='    ')
        print('Mobile:',result[i]['mobile'],end='    ')
        print('Email:',result[i]['email'],end='    ')
        print('Topic:',result[i]['topic'],end='    ')
        print('Score:',result[i]['score'])


#view questions
def view_question_set():
    with open('questions.json') as json_file:
        questions = json.load(json_file)
        
    for i in questions.keys():
        print('\nQuiz Topic:',i,'\n')
        for j in questions[i].keys():
            print(j,'.',questions[i][j]['question'])
            print('Difficulty level:',questions[i][j]['level'])
            print('Option 1:',questions[i][j]['option1'],end='     ')
            print('Option 2:',questions[i][j]['option2'],end='     ')
            print('Option 3:',questions[i][j]['option3'],end='     ')
            print('Option 4:',questions[i][j]['option4'])
            print('Answer:',questions[i][j]['answer'],'\n')
    

#add question
def add_question_set():
    temp={}
    topic=input('\nEnter new quiz topic:')
    no=int(input('No of questions you want to add:'))
    for i in range(1,no+1):
        ques=input('Enter Question:')
        op1=input('Enter Option 1:')
        op2=input('Enter Option 2:')
        op3=input('Enter Option 3:')
        op4=input('Enter Option 4:')
        ans=input('Enter Answer:')
        level=input('Enter difficulty level:')
        temp[i]={'question': ques, 'option1': op1, 'option2': op2, 'option3': op3, 'option4': op4, 'answer': ans, 'level': level}

    with open('questions.json') as json_file:
        questions = json.load(json_file)

    questions[topic]=temp

    with open("questions.json","w") as fi:
        json.dump(questions,fi)
    print('Question set added successfully :)')

#update question
def update_question_set():
    with open('questions.json') as json_file:
        questions = json.load(json_file)
    
    print('\nTOPICS:')
    for i in questions.keys():
        print(i)
        
    topic=input('Enter topic you want to udpate:')
    
    print('\nTopic:',topic,'\n')
    for j in questions[topic].keys():
        print(j,'.',questions[topic][j]['question'])
        print('Difficulty level:',questions[topic][j]['level'])
        print('Option 1:',questions[topic][j]['option1'],end='     ')
        print('Option 2:',questions[topic][j]['option2'],end='     ')
        print('Option 3:',questions[topic][j]['option3'],end='     ')
        print('Option 4:',questions[topic][j]['option4'])
        print('Answer:',questions[topic][j]['answer'],'\n')
    
    index=int(input('Enter question no you want to update:'))
    level=input('Enter difficulty level:')
    ques=input('Enter Question:')
    op1=input('Enter Option 1:')
    op2=input('Enter Option 2:')
    op3=input('Enter Option 3:')
    op4=input('Enter Option 4:')
    ans=input('Enter Answer:')
    
    questions[topic][index]={'question': ques, 'option1': op1, 'option2': op2, 'option3': op3, 'option4': op4, 'answer': ans, 'level': level}

    with open("questions.json","w") as fi:
        json.dump(questions,fi)
    print('Topic updated successfully :)')
    

#delete question
def delete_question_set():
    with open('questions.json') as json_file:
        questions = json.load(json_file)
        
    print('\nTOPICS:')
    for i in questions.keys():
        print(i)
    
    topic=input('Enter topic you want to delete:')
    del questions[topic]

    with open("questions.json","w") as fi:
        json.dump(questions,fi)
    print('Topic deleted sucessfully :)')


# Superuser Panel
def superuser_panel():
    print("\nChoose Your Option")
    print("1. Create Question Set")
    print("2. View Question Set")
    print("3. Update Question Set")
    print("4. Delete Question Set")
    print("5. View past results")
    print("6. Go back")
    print("7. Exit")
    choice = int(input("Enter your choice(1-7)::"))

    if choice == 1:
        add_question_set()
    elif choice == 2:
        view_question_set()
    elif choice == 3:
        update_question_set()
    elif choice == 4:
        delete_question_set()
    elif choice == 5:
        view_results()
    elif choice == 6:
        main()
    elif choice == 7:
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(2)
    superuser_panel()


# Check Id aand password validity for Admin
def superuser_check():
    uname = input("Enter your username::")
    pwd = input("Enter your password::")
    flag = -1
    
    if superuser['user'] == uname and superuser['password'] == pwd:
        flag = 1
        
    if flag == -1:
        print("Wrong credentials!!!")
        superuser_check()
    return flag


# Main function
def main():
    usertype = input("Who are you (super user or user) or exit::")

    # Admin type
    if usertype == 'super user':
        flag = int(superuser_check())
        if flag == 1:
            print("Login Successful...")
            superuser_panel()

    elif usertype == 'user':
        name=input('Enter your name:')
        mobile=int(input('Enter mobile number:'))
        email=input('Enter email:')
        user_panel(name,mobile,email)
        
    elif usertype == 'exit':
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!\nPlease try again...")
    time.sleep(2)
    main()


# Start of MCQ Quiz App
print("*****WECLOME TO MCQ QUIZ APP*****")
main()
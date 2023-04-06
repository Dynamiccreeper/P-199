import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("Server has started...")

questions =[
    "what is the italian word for pie? \n a.Mozarella \n b.Patty\n d.Pizza",
    "water boils at 212 Units at which scale \n a.Fabrenheit \n b.Celains \n c.Rankine \n d.Kelvin"

]

answers = ['d','a']

def get_random_question_answer(conn):
    random_index=random.randint(0,len(questions)-1)
    random_question=questions[random_index]
    random_answer=answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def clientthread(conn):
    score=0
    conn.send("Welcome to this quiz game!".encode('itf-8'))
    conn.send("you will receive a question. The answer to that question should be one of a,b,c,d")
    conn.send("Good Luck! \n\n".encode('wtf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower()== answer:
                    score +=1
                    conn.send(f"Bravo! your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("inccorect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue

def remove_question(index):
    questions.pop(index)
    answers.pop(index)
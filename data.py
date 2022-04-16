import requests

parameters = {
  "amount": 10,
  "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_data = [
#     {
#       "category": "Geography",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "The flag of South Africa features 7 colours.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Sports",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "Manchester United won the 2013-14 English Premier League.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Science: Computers",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Science: Computers",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "Linus Torvalds created Linux and Git.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Science & Nature",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Science: Computers",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "Ada Lovelace is often considered the first computer programmer.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Entertainment: Video Games",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "In the &quot;Half-Life&quot; series, &quot;H.E.V&quot; stands for &quot;Hazardous Evasiveness Vest&quot;",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Geography",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "St. Louis is the capital of the US State Missouri.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Entertainment: Music",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "The alternative rock band, They Might Be Giants, released their album &#039;Flood&#039; in 1990. ",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Politics",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "During the 2016 United States presidential election, the State of California possessed the most electoral votes, having 55.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     }
#   ]

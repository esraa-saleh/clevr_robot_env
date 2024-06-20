# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script demonstrate the usage of CLEVR-ROBOT environment."""

from __future__ import absolute_import, division, print_function
from absl import app, flags
from matplotlib import pyplot as PLT
from env import ClevrEnv
import random

FLAGS = flags.FLAGS
COLORS = ['red', 'blue', 'green', 'magenta', 
          # 'cyan', 'purple', 'white', 
          # 'red2', 'blue2', 'green2', 'magenta2', 'cyan2', 'purple2', 'white2', 
          # 'red3', 'blue3', 'green3', 'magenta3', 'cyan3', 'purple3', 'white3',
          # 'red4', 'blue4', 'green4', 'magenta4', 'cyan4', 'purple4', 'white4',
          # 'red5', 'blue5', 'green5', 'magenta5', 'cyan5', 'purple5', 'white5',
          # 'red6', 'blue6', 'green6', 'magenta6', 'cyan6', 'purple6', 'white6',
          # 'red7', 'blue7', 'green7', 'magenta7', 'cyan7', 'purple7', 'white7',
          # 'red8', 'blue8', 'green8', 'magenta8', 'cyan8', 'purple8', 'white8',
          # 'red9', 'blue9', 'green9', 'magenta9', 'cyan9', 'purple9', 'white9',
          # 'red10', 'blue10', 'green10', 'magenta10', 'cyan10', 'purple10', 'white10',
          # 'red11', 'blue11', 'green11', 'magenta11', 'cyan11', 'purple11', 'white11',
          # 'red12', 'blue12', 'green12', 'magenta12', 'cyan12', 'purple12', 'white12',
          # 'red13', 'blue13', 'green13', 'magenta13', 'cyan13', 'purple13', 'white13',
          # 'red14', 'blue14', 'green14', 'magenta14', 
          'cyan14', 'purple14', 'white14', 'red15', 'blue15']
DIRECTIONS = ['left', 'right', 'front', 'behind']
DIRECT_COMB = [('left', 'front'), ('left', 'behind'), ('right', 'front'), ('right', 'behind')]

def main(_):
  env = ClevrEnv(num_object=100)
  
  description = env.get_coordinates_description()
  print('Descriptions: ', description)
  # print('Colors left out: ', colors_leftout)
  all_questions = env.generate_all_questions(COLORS, DIRECT_COMB, DIRECTIONS)
  
  rgb = env.render(mode='rgb_array')
  PLT.imshow(rgb)
  PLT.show()
  
  # Get all questions
  questions_and_programs = []
  for questions in all_questions:
    program = []
    for question in questions:
      program.append(env.get_program_from_question(question))
    questions_and_programs.append((questions, program))
  
  print(len(questions_and_programs))
  # Answer all questions
  questions_answers = []
  for q, p in questions_and_programs:
    answer = True
    for program in p:
      answer = answer and env.answer_question(program)
    questions_answers.append((q, answer))
    
  true_questions = []
  false_questions = []

  # Iterate through the list of tuples
  for question, value in questions_answers:
    if value:
      true_questions.append((question, value))
    else:
      false_questions.append((question, value))

  # Ensure exactly 25 true and 25 false questions
  selected_true_questions = true_questions[:50]
  selected_false_questions = false_questions[:50]

  # Combine the selected questions
  selected_questions = selected_true_questions + selected_false_questions

  # Format question for LLM input
  formatted_questions = env.format_questions([q[0] for q in selected_questions])
  
  all_questions_answers = []
  for i in range(len(formatted_questions)):
    all_questions_answers.append((formatted_questions[i], selected_questions[i][1]))
    
  random.shuffle(all_questions_answers)
  
  with open('llm_.txt', 'w') as file:
    for item in all_questions_answers:
      file.write(f"{item[0]}, {item[1]}\n")
      
  print('hey')
      
  # # Get llm questions
  # llm_questions = env.generate_llm_questions(formatted_questions, colors_leftout)
  # llm_questions_answers = []
  # for i in range(len(llm_questions)):
  #   llm_questions_answers.append((llm_questions[i][0], questions_answers[llm_questions[i][1]][1]))
  
if __name__ == '__main__':
  app.run(main)

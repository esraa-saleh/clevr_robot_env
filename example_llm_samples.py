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

import json

FLAGS = flags.FLAGS
COLORS = ['red', 'blue', 'green', 'purple', 'cyan']
DIRECTIONS = ['left', 'right', 'front', 'behind']
DIRECT_COMB = [('left', 'front'), ('left', 'behind'), ('right', 'front'), ('right', 'behind')]

def main(_):
  env = ClevrEnv()
  
  description, colors_leftout = env.get_formatted_description()
  print('Descriptions: ', description)
  print('Colors left out: ', colors_leftout)
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
  
  # Answer all questions
  questions_answers = []
  for q, p in questions_and_programs:
    answer = True
    for program in p:
      answer = answer and env.answer_question(program)
    questions_answers.append((q, answer))

  # Format question for LLM input
  formatted_questions = env.format_questions(all_questions)
  
  all_questions_answers = []
  for i in range(len(formatted_questions)):
    all_questions_answers.append((formatted_questions[i], questions_answers[i][1]))
      
  # Get llm questions
  llm_questions = env.generate_llm_questions(formatted_questions, colors_leftout)
  llm_questions_answers = []
  for i in range(len(llm_questions)):
    llm_questions_answers.append({'Description': description, 'Question': llm_questions[i][0], 'Answer': questions_answers[llm_questions[i][1]][1]})
    
  def change_directions(data):
    direction_map = {
        'left': 'West',
        'right': 'East',
        'front': 'South',
        'behind': 'North'
    }

    def replace_description(text):
      new_text = []
      for description in text:
        for old_direction, cardinal_direction in direction_map.items():
          description = description.replace(old_direction, cardinal_direction)
        new_text.append(description)
      return new_text
    
    def replace_question(text):
      for old_direction, cardinal_direction in direction_map.items():
        text = text.replace(old_direction, cardinal_direction)
      return text

    for sample in data:
      sample['Description'] = replace_description(sample['Description'])
      sample['Question'] = replace_question(sample['Question'])
    
    return data
  
  llm_questions_answers = change_directions(llm_questions_answers)
  
  with open('llm_data_5.txt', 'w') as convert_file: 
    convert_file.write(json.dumps(llm_questions_answers))
  
if __name__ == '__main__':
  app.run(main)

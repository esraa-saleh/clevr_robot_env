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
from env import ClevrGridEnv

FLAGS = flags.FLAGS
COLORS = ['red', 'blue', 'green', 'purple', 'cyan']
DIRECTIONS = ['West', 'East', 'South', 'North']
DIRECT_COMB = [('West', 'South'), ('West', 'North'), ('East', 'South'), ('East', 'North')]

def main(_):
  env = ClevrGridEnv(clevr_seed=0, mujoco_seed=0)
  
  rgb = env.render(mode='rgb_array')
  PLT.imshow(rgb)
  PLT.savefig("test_scene1.png")
  
  id1 = 1
  id2 = 2
  color1 = env.scene_graph[id1]["color"]
  color2 = env.scene_graph[id2]["color"]
  direc = "left"
  
  print("Imagine moving the", color1, "ball so that it is one unit", direc, "of the", color2, "ball.")
  success = env.step_place_object_in_relation(id1, direc, id2)
  print("Did placement succed? ", success)
  
  # description, colors_leftout = env.get_formatted_description()
  # print('Descriptions: ', description)
  # print('Colors left out: ', colors_leftout)
  # all_questions = env.generate_all_questions(COLORS, DIRECT_COMB, DIRECTIONS)
  
  rgb = env.render(mode='rgb_array')
  PLT.imshow(rgb)
  PLT.savefig("test_scene2.png")
  
  
  # # Get all questions
  # questions_and_programs = []
  # for questions in all_questions:
  #   program = []
  #   for question in questions:
  #     program.append(env.get_program_from_question(question))
  #   questions_and_programs.append((questions, program))
  
  # # Answer all questions
  # questions_answers = []
  # for q, p in questions_and_programs:
  #   answer = True
  #   for program in p:
  #     answer = answer and env.answer_question(program)
  #   questions_answers.append((q, answer))

  # # Format question for LLM input
  # formatted_questions = env.format_questions(all_questions)
  
  # all_questions_answers = []
  # for i in range(len(formatted_questions)):
  #   all_questions_answers.append((formatted_questions[i], questions_answers[i][1]))
      
  # # Get llm questions
  # llm_questions = env.generate_llm_questions(formatted_questions, colors_leftout)
  # llm_questions_answers = []
  # for i in range(len(llm_questions)):
  #   llm_questions_answers.append((llm_questions[i][0], questions_answers[llm_questions[i][1]][1]))
  
if __name__ == '__main__':
  app.run(main)

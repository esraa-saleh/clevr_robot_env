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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from matplotlib import pyplot as PLT

from env import ClevrEnv

import numpy as np

FLAGS = flags.FLAGS
COLORS = ['red', 'blue', 'green', 'purple', 'cyan']
DIRECTIONS = ['left', 'right', 'front', 'behind']
DIRECT_COMB = [('left', 'front'), ('left', 'behind'), ('right', 'front'), ('right', 'behind')]


def main(_):
  env = ClevrEnv()
  print(len(env.descriptions))
  print(env.descriptions)
  print(len(env.all_questions))
  
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
  
  llm_examples = []
  for i in range(len(formatted_questions)):
    llm_examples.append((formatted_questions[i], questions_answers[i][1]))

if __name__ == '__main__':
  app.run(main)
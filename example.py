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
import re

from env import ClevrEnv
from utils.rendering_utils import show_scene

FLAGS = flags.FLAGS


def main(_):
  env = ClevrEnv()
  description, colors_leftout = env.get_formatted_description()
  print('Descriptions: ', description)
  show_scene(env)
  print('Colors left out: ', colors_leftout)
  # questions = env.sample_missing_questions(colors_leftout)
  
  # def rephrase(sentence):
  #   sentence = sentence.replace(' rubber', "")
  #   sentence = sentence.replace(' matte', "")
  #   sentence = sentence.replace('ball', "sphere")
  #   sentence = sentence.replace('balls', "spheres")
    
  #   # Extract the relevant parts using regex
  #   match_1 = re.match(r'There is a (\w+) sphere[;,] are there any (\w+) spheres (\w+) it\?', sentence)
  #   match_2 = re.match(r'There is a (\w+) sphere[;,] are there any (\w+) spheres in (\w+) of it\?', sentence)
  #   if match_1:
  #     main_color = match_1.group(1)
  #     other_color = match_1.group(2)
  #     position = match_1.group(3)
  #     # Switch "behind" and "front" and handle the "of"
  #     if position == "behind":
  #       return f'There is a {main_color} sphere; are there any {other_color} spheres in front of it?'
  #   elif match_2:
  #     main_color = match_2.group(1)
  #     other_color = match_2.group(2)
  #     position = match_2.group(3)
  #     if position == "front":
  #       return f'There is a {main_color} sphere; are there any {other_color} spheres behind it?'
  #   else:
  #     return sentence

  # question_answer = [(question[0], env.answer_question(question[1])) for question in questions]       
  # rephrased_question_answer = [
  #   (rephrase(question), answer) for question, answer in question_answer
  # ]

  # print('Questions and answers: ', list(set(rephrased_question_answer)))
  

if __name__ == '__main__':
  app.run(main)

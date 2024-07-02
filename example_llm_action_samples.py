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
import random
FLAGS = flags.FLAGS
COLORS = ['red', 'blue', 'green', 'purple', 'cyan']
DIRECTIONS = ['left', 'right', 'front', 'behind']
DIRECT_COMB = [('left', 'front'), ('left', 'behind'), ('right', 'front'), ('right', 'behind')]

def generate_spatial_action_examples(num_scenes, max_num_question, qa_seed=97):
  
  scenario_qa = {}
  qa_rng = random.Random(qa_seed)
  for i in range(num_scenes):
    env = ClevrGridEnv(seed=i) # this samples a random scene with a fixed seed
    
    rgb = env.render(mode='rgb_array')
    PLT.imshow(rgb)
    PLT.savefig("test_scene_"+str(i)+".png")
    
    actions = env.get_placement_actions()
    scene_description, _ = env.get_formatted_description()
    scene_description = ' '.join(scene_description)
    # TODO might need to have a reset method of our own to reset to initial scene.
    len_objects = len(env.scene_graph)

    for o1 in range(len_objects):
      for o2 in range(len_objects):
        for a in actions:
                    
          env.step_place_object_in_relation(o1, a, o2)
          description_before, colors_leftout = env.get_formatted_description()
          description_before = ' '.join(description_before) + ". "
          str_action = "Imagine moving the " + env.shape_name(o1) + " " + str(a) + " of the " + env.shape_name(o2) + " ."
          relations_with_action =  description_before + str_action
          
          all_questions = env.generate_all_questions(COLORS, DIRECT_COMB, DIRECTIONS)
          
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
            
          description_after_action, colors_leftout = env.get_formatted_description()
          description_after_action = ' '.join(description_after_action)
          print("Description before matches after action: ", description_after_action==description_before)
          env.reset()
          description_after_reset, colors_leftout = env.get_formatted_description()
          description_after_reset = ' '.join(description_after_reset)
          print("Description before matches after reset: ", description_after_reset==description_before)
          
          # print(scene_description)
          scenario_qa[(env.shape_name(o1), a, env.shape_name(o2))] = {"description": relations_with_action, "qa": qa_rng.sample(questions_answers, max_num_question)}
          break
        break
      break
    
  return scenario_qa

def main(_):
  # TODO: testing in depth with answer checking manually
  scenario_qa = generate_spatial_action_examples(2, 10)
  print(scenario_qa[next(iter(scenario_qa))])
  # env = ClevrGridEnv()
  
  # rgb = env.render(mode='rgb_array')
  # PLT.imshow(rgb)
  # PLT.savefig("test_scene1.png")
  
  # id1 = 1
  # id2 = 2
  # color1 = env.scene_graph[id1]["color"]
  # color2 = env.scene_graph[id2]["color"]
  # direc = "left"
  
  # print("Imagine moving the", color1, "ball so that it is one unit", direc, "of the", color2, "ball.")
  # success = env.step_place_object_in_relation(id1, direc, id2)
  # print("Did placement succed? ", success)
  
  # description, colors_leftout = env.get_formatted_description()
  # print('Descriptions: ', description)
  # print('Colors left out: ', colors_leftout)
  # all_questions = env.generate_all_questions(COLORS, DIRECT_COMB, DIRECTIONS)
  
  # rgb = env.render(mode='rgb_array')
  # PLT.imshow(rgb)
  # PLT.savefig("test_scene2.png")
  
  
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

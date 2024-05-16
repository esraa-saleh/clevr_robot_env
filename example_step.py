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

"""This script demonstrates the usage of CLEVR-ROBOT environment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from matplotlib import pyplot as PLT

from env import ClevrEnv
from utils.rendering_utils import save_scene

FLAGS = flags.FLAGS

def QA(env, questions):
    for q, p in questions:  
        print(q, env.answer_question(p))
    
    rgb = env.render(mode='rgb_array')
    PLT.imshow(rgb)
    PLT.show()
  
def main(_):
  obj_pos=[(0., 0., 0.13), 
            (0., 0.25, 0.13), 
            (0.25, 0., 0.13), 
            (0., -0.25, 0.13), 
            (-0.25, 0., 0.13)] 
  
  questions = [('There is a red matte sphere; are there any cyan spheres in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['red']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
               ('There is a purple matte ball; are there any cyan balls in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
               ('There is a cyan rubber sphere, are there any red spheres in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['red']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
  ] 
    
  # First initialization
  env = ClevrEnv(
      action_type="perfect",
      obs_type="order_invariant",
      direct_obs=True,
      use_subset_instruction=True,
      obj_pos=obj_pos,
  )
  print('Initialization: ')
  QA(env, questions, "init")
  
  # Action
  action = [4, ((-0.25, -0.25, 0.13))] # Cyan sphere to lower left corner
  env.step_no_physics(action)
  print('\n After action:')
  QA(env, questions, "action")
  return

if __name__ == '__main__':
  app.run(main)

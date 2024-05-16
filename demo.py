"""This script demonstrate the usage of CLEVR-ROBOT environment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from matplotlib import pyplot as PLT

from env import ClevrEnv

FLAGS = flags.FLAGS


def main(_):
  env = ClevrEnv(
      action_type="perfect",
      obs_type="order_invariant",
      direct_obs=True,
      use_subset_instruction=True,
      obj_pos=[(0., 0., 0.13), 
            (0., 0.25, 0.13), 
            (0.25, 0., 0.13), 
            (0., -0.25, 0.13), 
            (-0.25, 0., 0.13)],
  )
  questions = [('There is a red matte sphere; are there any cyan spheres in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['red']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
               ('There is a purple matte ball; are there any cyan balls in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
               ('There is a cyan rubber sphere, are there any red spheres in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['red']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]), 
               ('There is a purple ball; are there any blue rubber spheres to the left of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['purple']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['left']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['blue']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a purple matte sphere; are there any cyan rubber spheres right of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['right']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_material', 'inputs': [6], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [7], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [8]}]),
               ('There is a blue sphere; are there any green rubber balls behind it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['blue']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['behind']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['green']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a cyan rubber sphere, are there any red balls in front of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['front']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['red']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a red ball; are there any blue rubber balls on the left side of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['red']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['left']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['blue']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a cyan sphere, are there any blue spheres behind it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['behind']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['blue']}, {'type': 'filter_shape', 'inputs': [5], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [6]}]),
               ('There is a green sphere, are there any red rubber spheres behind it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['green']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['behind']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['red']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a cyan matte sphere, are there any red rubber balls to the right of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['right']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['red']}, {'type': 'filter_material', 'inputs': [6], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [7], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [8]}]),
               ('There is a green matte sphere, are there any red spheres on the right side of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['green']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['right']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['red']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a cyan sphere, are there any purple matte balls left of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['left']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a purple rubber sphere; are there any cyan balls behind it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [1], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [2], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [3]}, {'type': 'relate', 'inputs': [3], 'side_inputs': ['behind']}, {'type': 'filter_color', 'inputs': [5], 'side_inputs': ['cyan']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}]),
               ('There is a blue sphere; are there any purple matte balls on the right side of it?', [{'type': 'scene', 'inputs': []}, {'type': 'filter_color', 'inputs': [0], 'side_inputs': ['blue']}, {'type': 'filter_shape', 'inputs': [1], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [2]}, {'type': 'relate', 'inputs': [2], 'side_inputs': ['right']}, {'type': 'filter_color', 'inputs': [4], 'side_inputs': ['purple']}, {'type': 'filter_material', 'inputs': [5], 'side_inputs': ['rubber']}, {'type': 'filter_shape', 'inputs': [6], 'side_inputs': ['sphere']}, {'type': 'exist', 'inputs': [7]}])]
  
  answers = []
  for q, p in questions:  
    answers.append((q, env.answer_question(p)))
  print(answers)
  rgb = env.render()
  PLT.imshow(rgb)
  PLT.show()
  action = env.sample_fixed_action(4, 3) # color = Cyan, direction = [-1, 0]
  env.step(action)
  rgb = env.render()
  PLT.imshow(rgb)
  PLT.show()
  new_answers = []
  for q, p in questions:  
    new_answers.append((q, env.answer_question(p)))
  print(new_answers)
  

if __name__ == '__main__':
  app.run(main)
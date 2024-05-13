"""This script demonstrate the usage of CLEVR-ROBOT environment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags

from env import ClevrEnv

FLAGS = flags.FLAGS


def main(_):
  env = ClevrEnv(
    #   action_type="perfect",
    #   obs_type="order_invariant",
    #   direct_obs=True,
    #   use_subset_instruction=True,
  )
#   env.step(env.sample_random_action())

if __name__ == '__main__':
  app.run(main)

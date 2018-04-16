import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='gym_foo-v0',
    entry_point='gym_foo.envs:fooEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='foo_extrahard_env-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
    timestep_limit=1000,
    reward_threshold=10.0,
    nondeterministic = True,
)









#from gym.envs.registration import registry, register, make, spec

#register(
#    id='foo-v0',
#    entry_point='gym_foo.envs:fooEnv',
#)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)

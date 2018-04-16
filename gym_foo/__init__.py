from gym.envs.registration import registry, register, make, spec

register(
    id='foo-v0',
    entry_point='gym_foo.envs:fooEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)

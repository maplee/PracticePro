from pyvirtualdisplay import Display
import gym

# Start virtual display
# display = Display(visible=0, size=(1400, 900))
# display.start()

env = gym.make('CartPole-v1', render_mode="rgb_array")
state = env.reset()

try:
    for t in range(1000):
        env.render()
        # print(state)

        action = env.action_space.sample()
        state, reward, done, info,_ = env.step(action)

        if done:
            print(state, reward, done, info)
            print('Finished')
            break

finally:
    env.close()

    # Stop virtual display
    # display.stop()

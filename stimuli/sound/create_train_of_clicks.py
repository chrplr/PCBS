import numpy as np
import generate_clicks

sr, click= generate_clicks.load_sound_as_array('click.wav')

click = np.zeros(len(click))
click[0:int(sr * 0.005)] = 16384

target = np.zeros(sr*120)
positions = [1 + i*0.5 for i in range(230)]
generate_clicks.multi_mix(target, click, positions)
generate_clicks.write_array_as_sound(target, sr, 'clicks_2hz.wav')

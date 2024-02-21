# lecture 2


# Dynamic displays


In a nutshell:

    repeat 
	   Draw something
	   pygame.display.flip()
	   pygame.time.wait(xxx)   # xxx in msec


* Goto [11.2 Dynamic visual stimuli](https://pcbs.readthedocs.io/en/latest/stimulus-creation.html#dynamic-visual-stimuli)

    * illusory line motion
    * flash-lag illusion
	
Have a look at `ebbinghaus-dynamic.py`, `lilac_chaser.py` and `lilac_chaser_blurred.py`

---

# Experiments


In a nutshell:

     # prepare stimuli

     for trial_num in range(number_of_trials):
	      present stimulus(trial_num)
		  record response  (button or key press)
		  
	 save responses
		  
		  
      

* Goto [12 Experiments](https://pcbs.readthedocs.io/en/latest/running-experiments.html). Do section 1 (simple stimuli)


* Check <https://chrplr.github.io/tutorial-expyriment/>














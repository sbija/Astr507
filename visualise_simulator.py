"""
    visualise_simulator.py
    =================

    Use this file to test your simulator by visualising the results and making sure everything looks okay.
    Note that you'll need to change your simulator.py code for this to actually work!!

"""
import simulator

# you probably want the size to be at least 750 as this is in pixels for the visualisation
size = 750

# change these to valid values (it will crash if you don't!)
E = None
mass = None
radius = None
N = None
steps = None

sim = simulator.Simulation(N=N, E=E, radius=radius, size=size, masses=mass, delay=20, visualise=True)
sim.run_simulation(steps)

import numpy as np
import tkinter as tk


class Simulation():
    def __init__(self, N, E, size, radius, masses, delay=20, visualise=True):
        """Simulation class initialisation. This class handles the entire particle in a box situation.

        Parameters
        ----------
        N : `int`
            Total number of particles
        E : `float`
            Kinetic energy for each particle to start with
        size : `float`
            Size of the box
        radius : `float/array`
            Radius of the particles
        masses : `float/array`
            Mass of the particles (either a single value for all or an array with different values for each)
        delay : `int`
            Delay in milliseconds between showing/running timesteps
        visualise : `boolean`
            Whether to animate the balls in the box
        """
        self.N = N
        self.E = E
        self.size = size
        self.radius = radius

        # save the masses as an array, whatever is inputted
        self.masses = np.repeat(masses, self.N) if isinstance(masses, (int, float)) else masses

        # TODO: initialise the positions of particles in the box
        # -- YOUR CODE HERE --
        x, y = np.zeros(N), np.zeros(N)
        self.pos = np.transpose([x, y])
        # --------------------

        # TODO: initialise the velocities of the particles (based on `E` and `masses`)
        # -- YOUR CODE HERE --
        vx, vy = np.ones(N), np.ones(N)
        self.vel = np.transpose([vx, vy])
        # --------------------

        # initialise visualisation if it is turned on
        self.visualise = visualise
        if visualise:
            self.delay = delay
            self.canvas = None
            self.root = None
            self.particle_handles = {}

            self._init_visualization()
            self.root.update()

    def _init_visualization(self):
        """ Start up the visualisation stuff and save it all in the class """
        # start the visualisation box
        self.root = tk.Tk()
        self.root.title("Particles in a Box!")

        # create a canvas with the right size
        self.canvas = tk.Canvas(self.root, width=self.size, height=self.size)
        self.canvas.pack()

        # add a close button
        self.button = tk.Button(self.root, text='Close', command=self._quit_visualisation)
        self.button.place(x=self.size, y=10, anchor="e")

        # add a message that keeps track of the timesteps
        self.timestep_message = self.canvas.create_text(self.size // 2, 10, text="Timestep = 0")

        # choose five random particles to make red (rest are green)
        reds = np.random.choice(self.N, size=5, replace=False)

        # add all of the particles
        for i in range(self.N):
            self._draw_particle(i, fill="green" if i not in reds else "red", outline="black")

        # update this all on the canvas
        self.root.update()

    def _quit_visualisation(self):
        """ End the visualisation and close the canvas """
        self.root.destroy()

    def _draw_particle(self, pid, fill="green", outline="black"):
        """Draw a circle on the canvas representing the particle

        Parameters
        ----------
        pid : `int`
            The particle ID
        fill : `str`, optional
            Particle fill colour, by default "green"
        outline : str, optional
            Particle outline colour, by default "black"
        """
        x0 = self.pos[pid, 0] - self.radius
        y0 = self.pos[pid, 1] - self.radius
        x1 = self.pos[pid, 0] + self.radius
        y1 = self.pos[pid, 1] + self.radius

        self.particle_handles[pid] = self.canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=outline)

    def resolve_wall_collisions(self):
        """Reverse the direction of any particles that hit walls"""
        # -- YOUR CODE HERE --
        # --------------------
        raise NotImplementedError

    def resolve_particle_collisions(self):
        """ Resolve all particles collisions during this timestep """
        # -- YOUR CODE HERE --
        # --------------------
        raise NotImplementedError

    def run_simulation(self, seconds=1000):
        """Run the simulation of particles! It can either be run for a set amount of time or until a steady
        state is reached.

        Parameters
        ----------
        seconds : `int`, optional
            How many seconds to evolve for, by default 1000
        """
        # TODO: you may want to experiment with different timesteps or even ~adaptive~ timesteps
        dt = 1
        time = 0
        while time < seconds:
            # TODO: update all particle positions based on current speeds
            # -- YOUR CODE HERE --
            change_in_pos = np.zeros_like(self.pos)
            # --------------------
            self.pos += change_in_pos

            if self.visualise:
                for j in range(self.N):
                    self.canvas.move(self.particle_handles[j], change_in_pos[j, 0], change_in_pos[j, 1])

            # TODO: resolve whether any particles hit the wall and reflect them
            # self.resolve_wall_collisions()

            # TODO: resolve any particle collisions and transfer momentum
            # self.resolve_particle_collisions()

            if self.visualise:
                # update visualization with a delay
                self.root.after(self.delay, self.root.update())

                # change the timestep message as well
                self.canvas.itemconfig(self.timestep_message, text="Timestep = {}".format(time))

            # update the time
            time += dt

        # if visualising then block (wait without polling) until the canvas is closed by the user
        if self.visualise:
            self.root.mainloop()

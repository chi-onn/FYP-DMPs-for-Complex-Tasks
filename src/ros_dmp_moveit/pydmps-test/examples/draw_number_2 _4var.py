"""
Copyright (C) 2016 Travis DeWolf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy as np
import matplotlib.pyplot as plt

import pydmps
import pydmps.dmp_discrete

import pandas as pd
import numpy as np

# y_des = np.load("2.npz")["arr_0"].T
# y_des -= y_des[:, 0][:, None]
df = pd.read_csv('/home/chionn/fyp_ws/src/ros_dmp_moveit/pydmps-test/examples/traj_files/draw_2.traj',header=None)
df_2 = np.transpose(df.loc[:,0:3])
y_des = df_2.to_numpy()
#y_des = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6],[0.7,0.8,0.9]])

# test normal run
dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=4, n_bfs=500, ay=np.ones(4) * 10.0)
y_track = []
dy_track = []
ddy_track = []

dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()
plt.figure(1, figsize=(6, 6))

plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2)
plt.title("DMP system - draw number 2")

plt.axis("equal")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()

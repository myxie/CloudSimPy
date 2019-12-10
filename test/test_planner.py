# Copyright (C) 27/11/19 RW Bunney

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import unittest
import simpy
import os

from core.planner import Planner, Plan
from core.cluster import Cluster
from core.scheduler import Scheduler
from core.telescope import Observation
from core.buffer import Buffer

from scheduler.fifo_algorithm import FifoAlgorithm

import test_data

current_dir = os.path.abspath('.')

# Globals
OBS_START_TME = 0
OBS_DURATION = 10
OBS_DEMAND = 15
OBS_WORKFLOW = "{0}/{1}".format(current_dir, test_data.test_plan_workflow)


PLAN_ALGORITHM = test_data.planning_algorithm
MACHINE_CONFIG = "{0}/{1}".format(current_dir, test_data.machine_config)


class TestPlanner(unittest.TestCase):

	def setUp(self):
		self.env = simpy.Environment()
		sched_algorithm = FifoAlgorithm()
		self.planner = Planner(self.env, PLAN_ALGORITHM, MACHINE_CONFIG)
		self.cluster = Cluster(test_data.machine_config)
		# self.buffer = Buffer(self.env, self.cluster)
		# self.scheduler = Scheduler(self.env, sched_algorithm, self.buffer, self.cluster)
		self.observation = Observation('planner_observation',
									OBS_START_TME,
									OBS_DURATION,
									OBS_DEMAND,
									OBS_WORKFLOW)
		pass

	def tearDown(self):
		pass

	def testShadowIntegration(self):
		pass

	def testPlanReadsFromFile(self):
		# Return a "Plan" object for provided workflow/observation
		self.planner.wfname = self.observation.name
		self.planner.wfconfig = self.observation.workflow
		plan = self.planner.plan(PLAN_ALGORITHM)
		self.assertEqual(plan.id, 'planner_observation')  # Expected ID for the workflow
		self.assertEqual(plan.makespan, 98)  # Expected makespan for the given graph

	def testPlannerRun(self):
		next(self.planner.run(self.observation))
		# because run() is a generator (we call yield for simpy), we use(next()) to 'get the return value',
		# and thus run the rest of the code in run()
		# next(val)
		self.assertTrue(self.observation.plan is not None)

	def testGracefulExit(self):
		pass

	def testIncorrectParameters(self):
		pass

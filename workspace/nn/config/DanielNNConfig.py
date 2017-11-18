from enum import Enum
from torchvision import transforms, models
import pathlib
import torch
import torch.nn as nn
import DataUtil
import os
from DefaultNNConfig import DefaultConfig
#
# Class to use the default configuration.
class Config(DefaultConfig):
    #
    # Initialize.
    def __init__(self):
        super(Config, self).__init__()
        self.hyperparam.numEpochs = 32
        self.epochSaveInterval = 1

        self.modelSavePath = '/disk1/model/'
        # self.modelLoadPath = '/disk1/model/model_best.pth.tar'
        # # super(Config, self).loadModel()
        self.dataTrainList = [
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-07-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-03-04/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-34-41/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-43-16/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-04-59/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-25-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-15-37/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-20-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-03-54/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-17-56/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-43-14/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-33-27/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-40-13/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-49-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-58-57/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-20-07/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-06-17/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-11-58/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-05-24/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-15-08/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-32-55/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-37-41/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-29-06/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-56-44/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-50-13/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-06-00/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-10-43/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-53-48/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-01-32/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-26-15/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-39-41/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-51-37/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-26-45/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-29-26/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-45-31/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-25-08/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-03-58/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-40-50/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-16-13/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-07-44/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-31-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-14-18/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-53-58/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-42-00/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-52-22/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-46-32/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-09-33/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-45-32/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-37-46/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-32-04/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-41-11/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-27-26/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-48-22/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-57-53/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-38-10/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-47-02/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-10-07/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-56-57/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-34-20/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-22-40/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-54-00/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-10-54/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-48-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-50-27/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-13-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-25-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-13-51/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-22-49/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-38-09/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-49-54/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-36-48/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-11-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-58-59/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-20-53/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-16-03/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-35-17/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-06-58/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-27-43/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-20-40/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-08-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-24-33/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-55-58/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-50-20/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-15-31/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-48-41/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-43-14/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-30-42/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-18-00/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-24-13/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-17-41/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-19-21/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-36-21/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-09-39/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-20-29/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-17-38/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-23-11/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-05-53/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-35-40/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-02-23-48/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-57-32/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-11-30/',
        # round 1 dagger.
'/disk1/data/20171118-124720/daggerAgent_EnvironmentTypes.AirSim_18-11-2017-12-47-32/',
        ]
        self.dataValList = [
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-48-33/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-27-57/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-01-44/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-14-14/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-16-55/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-01-06/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-24-16/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-38-24/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-08-17-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-48-01/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-33-34/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-03-30/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-51-35/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-47-37/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-52-26/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-31-34/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-41-02/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-03-01-56/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-04-22-39/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-05-13-14/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-01-30-37/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-06-22-36/',
        '/disk1/data/20171111-012402/dumbAgent_EnvironmentTypes.AirSim_11-11-2017-07-00-04/',
        #round 1 dagger


        ]
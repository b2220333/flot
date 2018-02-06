from torchvision import transforms, models
import pathlib2 as pathlib
import torch
import torch.nn as nn
from nn.util import DataUtil
from nn.util import Perterbations
import os
from debug import *
from models import GenericModel
#
# The hyper parameters.
class HyperParam():
    #
    # Image shape
    image_shape = (224, 224)
    #
    # Number of images in a batch.
    batchSize = 32
    #
    # How many epochs to train for.
    numEpochs = 10
    #
    # Criteria.
    criteria = nn.CrossEntropyLoss()
    #
    # Scheduler.
    scheduler = None
    #
    # Network modification fn.
    networkModification = None
    #
    # How far to shift the image.
    shiftBounds = int(224/3)
    #
    # The number of shift bins.
    nSteps = (0, 0)
    #
    # The intermadiate shape of the data, in order to gain more information,
    # within a single image we downscale.
    cropShape = (448, 448)

    def __init__(self, model):
        #
        # The model being used.
        self.model = model
        #
        # Optimizer.
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=1e-3)
#
# Default configuration that is overriden by subsequent configurations.
class DefaultConfig(object):
    #
    # The default data path.
    dataTrainList = [
    ]
    #
    # The default validation set.
    dataValList = [
        # '/disk1/val/data1'
    ]
    #
    # The csv file name.
    csvFileName = 'labels.csv'
    #
    # The image type name.
    imgName = 'front_camera'
    #
    # Transform relative to absolute paths.
    @staticmethod
    def getAbsPath(path):
        return os.path.abspath(path)
    #
    # Assume that cuda should be used if it is available. 
    usegpu = torch.cuda.is_available()
    #
    # Save tensorboard data.
    useTensorBoard = False
    #
    # Number of workers for loading data.
    numWorkers = 8
    #
    # Resize the network as needed.
    networkModification = None
    #
    # Save every x epochs.
    epochSaveInterval = 1
    #
    # Model save path.
    modelSavePath = ''
    #
    # Load a model.
    modelLoadPath = None
    ###########################################################################
    # Initialization that may be different across configurations.
    ###########################################################################
    def __init__(self, model = GenericModel.GenericModel(models.resnet18(pretrained=True)), loadPath = None):
        #
        # The hyper parameters.
        self.hyperparam = HyperParam(model)
        #
        # Create paths for saving models.
        pathlib.Path(self.modelSavePath).mkdir(parents=True, exist_ok=True)
        #
        # Check if cuda is available.
        # if not torch.cuda.is_available():
            # printError('CUDA is not available!')
        self.usegpu = (torch.cuda.is_available() and self.usegpu)
        if self.usegpu:
            self.hyperparam.model.cuda()
        #
        # Transforms.
        self.transforms = transforms.Compose([
            Perterbations.CenterCrop(self.hyperparam.image_shape),
            DataUtil.ToTensor(),
        ])
        #
        # Load the model.
        self.modelLoadPath = loadPath
        self.loadModel(loadPath)

    def loadModel(self, loadPath):
        ''' Load model from a specified directory.
        '''
        if loadPath != None and os.path.isfile(loadPath):
            # 
            # Load the model based on where on whether it needs to go to the cpu / gpu.
            checkpoint = None
            if self.usegpu:
                checkpoint = torch.load(self.modelLoadPath)
            else:
                print(self.modelLoadPath)
                checkpoint = torch.load(self.modelLoadPath, map_location={'cuda:0': 'cpu'})
            # 
            # Ensure that the model type matches and load.
            if type(checkpoint['model']) == type(self.hyperparam.model):
                self.modelLoadPath = loadPath
                self.hyperparam.model = checkpoint['model']
                self.hyperparam.model.load_state_dict(checkpoint['state_dict'])
                self.hyperparam.optimizer.load_state_dict(checkpoint['optimizer'])
                printColour('Loaded model from path: %s'%loadPath, colours.OKBLUE)
            else:
                printError('Loaded model from path: %s is of type: (%s) while the specified model is of type: (%s)'%(loadPath, type(checkpoint['model']), type(self.hyperparam.model)))
        elif loadPath != None:
            printError('Unable to load specified model: %s'%(loadPath))
#
# Class to use the default configuration.
class Config(DefaultConfig):
    #
    # Initialize.
    def __init__(self):
        super(Config, self).__init__()
        self.modelSavePath = '/disk1/model/'
        self.dataTrainList = ['/Users/daniel/data/20180123_205116/']
        # self.dataTrainList = ['/home/rae/flot/workspace/data/test_dataset/']
# 
# Return the default set of transformations to obtain usable data.
def getDefaultTransform(conf):
    t = transforms.Compose([
        Perterbations.CenterCrop(conf.hyperparam.cropShape),
        DataUtil.Rescale(conf.hyperparam.image_shape),
        DataUtil.ToTensor(),
    ])
    return t
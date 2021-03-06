import os
from os.path import join

import matplotlib.pyplot as plt

# defined some constants values
CLASSES = ['Type_1', 'Type_2', 'Type_3']
dataset_name = 'data001_size512'
train_name = 'detector_002'
batch_size = 64
LR = 0.0001
n_epoch = 5  # testing
img_size = (512, 512)  # size (1024, 1024) requiring 1.5TB of memory

try:
    SageMakerTrainingRoot_dir = os.path.dirname(os.environ['SM_MODEL_DIR'])  # '/opt/ml'
except:
    SageMakerTrainingRoot_dir = ""

if SageMakerTrainingRoot_dir:
    SageMakerRoot_dir = SageMakerTrainingRoot_dir
    TRAIN_DATA_DIR = join(SageMakerRoot_dir, 'input/data/train')
    TEST_DATA_DIR = join(SageMakerRoot_dir, 'input/data/test')
    ADD_DATA_DIR = join(SageMakerRoot_dir, 'input/data/additional')
    BBOX_FILES = join(SageMakerRoot_dir, 'input/data/bboxes/%s_bbox.tsv')
    SAMPLE_PATH = join(SageMakerRoot_dir, 'input/data/sample_submission.csv')
    dataset_in_pickle = join(SageMakerRoot_dir, 'input/data/train_val.pickle')
    aug_output_dir = join(SageMakerRoot_dir, 'input/data/detect_data/{0}'.format(dataset_name))
    pred_aug_output_dir = join(SageMakerRoot_dir, 'pred_aug_output')
    model_save_dir = os.path.join(os.environ['SM_OUTPUT_DATA_DIR'], 'models/{0}/{1}'.format(dataset_name, train_name))
    dataset_in_numpy = os.path.join(SageMakerRoot_dir, 'input/data/dataset_in_numpy')

else:
    SageMakerRoot_dir = "/home/ec2-user/SageMaker"
    TRAIN_DATA_DIR = join(SageMakerRoot_dir, 'CervicalCancer_dataset/train')
    TEST_DATA_DIR = join(SageMakerRoot_dir, 'CervicalCancer_dataset/test')
    ADD_DATA_DIR = join(SageMakerRoot_dir, 'CervicalCancer_dataset/additional')
    BBOX_FILES = join(SageMakerRoot_dir, 'CervicalCancer_dataset/bboxes/%s_bbox.tsv')
    SAMPLE_PATH = join(SageMakerRoot_dir, 'CervicalCancer_dataset/sample_submission.csv')
    dataset_in_pickle = join(SageMakerRoot_dir, 'CervicalCancer_dataset/train_val.pickle')
    aug_output_dir = join(SageMakerRoot_dir, 'CervicalCancer_dataset/detect_data/{0}'.format(dataset_name))
    pred_aug_output_dir = join(SageMakerRoot_dir, 'CervicalCancer_dataset/pred_aug_output')
    model_save_dir = os.path.join(SageMakerRoot_dir,
                                  'CervicalCancer_dataset/models/{0}/{1}'.format(dataset_name, train_name))
    dataset_in_numpy = os.path.join(SageMakerRoot_dir, 'CervicalCancer_dataset/dataset_in_numpy')


# data_dir = aug_output_dir


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def show_bgr(img):
    plt.figure(figsize=(7, 7))
    plt.imshow(img[:, :, (2, 1, 0)])

import sys

sys.path.append('..')

from src.scripts.train_kfolds import train_kfolds

from src.scripts.utils import SageMakerRoot_dir
import os

data_dir = os.path.join(SageMakerRoot_dir, 'preproc_data/data002_kfold_val_detector002_size256_scale1.0')
save_dir = os.path.join(SageMakerRoot_dir, 'kfold_train/10fold_vgg16_002')
params = {
    'data_dir': data_dir,
    'save_dir': save_dir,
    'arch': "vgg16",
    'batch_size': 16,
    'lr': 0.0001,
    'n_epoch': 25
}

if __name__ == '__main__':
    train_kfolds(params)

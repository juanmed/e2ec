from .base import commen, data, model, train, test

data.scale = None

model.heads['ct_hm'] = 5

train.batch_size = 24
train.epoch = 140
train.dataset = 'coco_train'
train.num_workers = 10

test.dataset = 'coco_val'

class config(object):
    commen = commen
    data = data
    model = model
    train = train
    test = test
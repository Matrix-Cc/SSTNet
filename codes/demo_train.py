
from option import args
import data
import model
import utils
import loss
import trainer
import torch

#----
import random
import numpy as np
import os


if __name__ == '__main__':


    checkpoint = utils.checkpoint(args)

    if checkpoint.ok:
        dataloaders = data.create_dataloaders(args)
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        sr_model = model.Model(args, checkpoint).to(device)  # modify
        sr_loss = loss.Loss(args, checkpoint) if not args.test_only else None
        t = trainer.Trainer(args, dataloaders, sr_model, sr_loss, checkpoint)


        while not t.terminate():
            t.train()
            t.test()

    checkpoint.done()

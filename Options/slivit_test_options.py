import argparse
from Options.base_options import BaseOptions
class TestOptions():

    def initialize(self, parser):
        self.parser = parser
        parser = BaseOptions.initialize(self, parser) 
        parser.add_argument('--dataset3d',type=str, help='nodulemnist, ukbb, or custom3d')
        parser.add_argument('--checkpoint',type=str, default='./Pre-trained_Backbones/backbone.pth',  help='Path to fine tuned Slivit')
        parser.add_argument('--depth', type=int, default=3, help='ViT depth')
        parser.add_argument('--dim', type=int, default=64, help='ViT depth')
        parser.add_argument('--nslc', type=int, default=28, help='# of slices to use for 3D Fine-tuning')
        parser.add_argument('--heads', type=int, default=10, help='# of heads for multihead attention')
        parser.add_argument('--pathology',type=str,  help='Label to predict')
        parser.add_argument('--metric',type=str,  help='ROC-AUC,PR-AUC,R2')
        return self.parser
    
    def parse(self):
        opt = self.gather_options()
        self.opt = opt
        return self.opt
    
    def gather_options(self):
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser = self.initialize(parser)
        # get the basic options
        opt, _ = parser.parse_known_args()
        self.parser = parser
        return parser.parse_args()
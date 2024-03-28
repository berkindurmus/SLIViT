import argparse
from Options.base_options import BaseOptions
class TrainOptions():

    def initialize(self, parser):
        self.parser = parser
        parser = BaseOptions.initialize(self, parser) 
        parser.add_argument('--bbpath',type=str, default='./Pre-trained_Backbones/backbone.pth',  help='Path to pre-rained Convnext Backbone')
        parser.add_argument('--pathology',type=str,  help='Label to predict for 3D Fine-tuning')
        parser.add_argument('--depth', type=int, default=3, help='ViT depth')
        parser.add_argument('--dim', type=int, default=64, help='ViT depth')
        parser.add_argument('--nslc', type=int, default=28, help='# of slices to use for 3D Fine-tuning')
        parser.add_argument('--heads', type=int, default=10, help='# of heads for multihead attention')
        parser.add_argument('--dropout', type=float, default=0.2)
        parser.add_argument('--emb_dropout', type=float, default=0.1)
        

        
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
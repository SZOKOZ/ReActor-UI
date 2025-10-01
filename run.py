#!/usr/bin/env python3
import sys
import types
from torchvision.transforms.functional import rgb_to_grayscale
from modules import core

# Create a module for `torchvision.transforms.functional_tensor`
functional_tensor = types.ModuleType("torchvision.transforms.functional_tensor")
functional_tensor.rgb_to_grayscale = rgb_to_grayscale

# Add this module to sys.modules so other imports can access it
sys.modules["torchvision.transforms.functional_tensor"] = functional_tensor

if __name__ == '__main__':
    core.run()

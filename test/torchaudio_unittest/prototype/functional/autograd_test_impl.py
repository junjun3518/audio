import torch
import torchaudio.prototype.functional as F
from parameterized import parameterized
from torch.autograd import gradcheck, gradgradcheck
from torchaudio_unittest.common_utils import TestBaseMixin


class AutogradTestImpl(TestBaseMixin):
    @parameterized.expand(
        [
            (F.convolve,),
            (F.fftconvolve,),
        ]
    )
    def test_convolve(self, fn):
        leading_dims = (4, 3, 2)
        L_x, L_y = 23, 40
        x = torch.rand(*leading_dims, L_x, dtype=self.dtype, device=self.device, requires_grad=True)
        y = torch.rand(*leading_dims, L_y, dtype=self.dtype, device=self.device, requires_grad=True)
        self.assertTrue(gradcheck(fn, (x, y)))
        self.assertTrue(gradgradcheck(fn, (x, y)))

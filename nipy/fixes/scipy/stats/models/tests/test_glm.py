# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Test functions for models.GLM
"""

import numpy as np
import numpy.random as R
from numpy.testing import *

import nipy.fixes.scipy.stats.models as S
import nipy.fixes.scipy.stats.models.glm as models

W = R.standard_normal

class TestRegression(TestCase):

    def test_Logistic(self):
        X = W((40,10))
        Y = np.greater(W((40,)), 0)
        family = S.family.Binomial()
        cmodel = models(design=X, family=S.family.Binomial())
        results = cmodel.fit(Y)
        self.assertEquals(results.df_resid, 30)

    def test_Logisticdegenerate(self):
        X = W((40,10))
        X[:,0] = X[:,1] + X[:,2]
        Y = np.greater(W((40,)), 0)
        family = S.family.Binomial()
        cmodel = models(design=X, family=S.family.Binomial())
        results = cmodel.fit(Y)
        self.assertEquals(results.df_resid, 31)




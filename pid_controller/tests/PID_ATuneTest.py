#!/usr/bin/python

import unittest
import random

from .. import PID_ATune

class PID_ATuneTest(unittest.TestCase):
    
    def setUp(self):
        self.PAT = PID_ATune.PID_ATune(None, None)
        
    def test_construct(self):
        self.assertIsInstance(self.PAT, PID_ATune.PID_ATune)
    
    def test_init(self):
        self.assertEquals(self.PAT.control_type, True)
    
    def test_outputstep(self):
        self.PAT.output_step = 3.2
        self.assertEquals(self.PAT.output_step, 3.2)

    def test_controltype(self):
        self.PAT.control_type = PID_ATune.ControlType.PID
        self.assertTrue(self.PAT.control_type)
        
    def test_controltypeparam(self):
        with self.assertRaises(TypeError):
            self.PAT.control_type = "foo"
        
    def test_lookbacksec0(self):
        self.PAT.lookback_sec = 0
        self.assertEquals(self.PAT.lookback_sec, 1)
        
    def test_lookbacksec10(self):
        self.PAT.lookback_sec = 10
        self.assertEquals(self.PAT.lookback_sec, 10)
           
    def test_lookbacksec43(self):
        self.PAT.lookback_sec = 43
        self.assertEquals(self.PAT.lookback_sec, 43)

    def test_lookbacksec100(self):
        self.PAT.lookback_sec = 100
        self.assertEquals(self.PAT.lookback_sec, 100)
        
    def test_noiseband(self):
        self.PAT.noise_band = 4.6
        self.assertEquals(self.PAT.noise_band, 4.6)

class PID_ATune_StabilityTest(unittest.TestCase):
    """
    Test the stability verification method with dummy input/output functions.
    """
    
    def setUp(self):
        self._last = True
    
    def stable_input_func(self):
        return 5  # arbitrary value
    
    def stable_output_func(self, _):
        return 10 # arbitrary value
    
    def unstable_output_func(self, _):
        self._last = not self._last
        #if random.random() < 0.5:
        if self._last:
            return 1
        else:
            return 10
            
    def test_stable(self):
        print('test_stable')
        self.PAT = PID_ATune.PID_ATune(self.stable_input_func, self.stable_output_func)
        print('test_stable1')
        self.assertTrue(self.PAT.verify_stability())
        print('test_stable2')
        
    def test_unstable(self):
        print('test_unstable')
        self.PAT = PID_ATune.PID_ATune(self.stable_input_func, self.unstable_output_func)
        self.assertRaises(PID_ATune.PIDNotStableError, self.PAT.verify_stability)

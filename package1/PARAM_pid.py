# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:59:17 2025

@author: Melen
"""

class Param:
    
    def __init__(self,gains):
        # Number of states to be integrated by RK4
       self.number_of_states = gains.number_of_states
       # Length of the array vector that will be exported 
       self.size_DATA = gains.size_DATA 

       # **Translational** PID parameters 
       self.KP_tran = gains.KP_tran
       self.KD_tran = gains.KD_tran
       self.KI_tran = gains.KI_tran

       # **Rotational** PID parameters
       self.KP_rot = gains.KP_rot
       self.KD_rot = gains.KD_rot
       self.KI_rot = gains.KI_rot

       # ----------------------------------------------------------------
       #                   Safety Mechanism Parameters
       # ----------------------------------------------------------------

       # Mu - sphere intersection
       self.sphereEpsilon = gains.sphereEpsilon
       self.maximumThrust = gains.maximumThrust  

       # Mu - elliptic cone intersection
       self.EllipticConeEpsilon = gains.EllipticConeEpsilon
       self.maximumRollAngle = gains.maximumRollAngle
       self.maximumPitchAngle = gains.maximumPitchAngle

       # Mu - plane intersection
       self.planeEpsilon = gains.planeEpsilon
       self.alphaPlane = gains.alphaPlane 
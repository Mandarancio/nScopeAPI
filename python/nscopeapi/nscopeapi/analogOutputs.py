from ctypes import POINTER, c_int, c_bool, c_double
from nScopeDefs import *

nScopeAPI.nScope_set_AX_on.restype = c_int
nScopeAPI.nScope_set_AX_on.argtypes = [POINTER(scopeDev), c_int, c_bool]
nScopeAPI.nScope_get_AX_on.restype = c_int
nScopeAPI.nScope_get_AX_on.argtypes = [POINTER(scopeDev), c_int, POINTER(c_bool)]

nScopeAPI.nScope_set_AX_frequency_in_hz.restype = c_int
nScopeAPI.nScope_set_AX_frequency_in_hz.argtypes = [POINTER(scopeDev), c_int, c_double]
nScopeAPI.nScope_get_AX_frequency_in_hz.restype = c_int
nScopeAPI.nScope_get_AX_frequency_in_hz.argtypes = [POINTER(scopeDev), c_int, POINTER(c_double)]

nScopeAPI.nScope_set_AX_wave_type.restype = c_int
nScopeAPI.nScope_set_AX_wave_type.argtypes = [POINTER(scopeDev), c_int ,c_int]
nScopeAPI.nScope_get_AX_wave_type.restype = c_int
nScopeAPI.nScope_get_AX_wave_type.argtypes = [POINTER(scopeDev), c_int, POINTER(c_int)]

nScopeAPI.nScope_set_AX_unipolar.restype = c_int
nScopeAPI.nScope_set_AX_unipolar.argtypes = [POINTER(scopeDev), c_int, c_bool]
nScopeAPI.nScope_get_AX_unipolar.restype = c_int
nScopeAPI.nScope_get_AX_unipolar.argtypes = [POINTER(scopeDev), c_int, POINTER(c_bool)]

nScopeAPI.nScope_set_AX_amplitude.restype = c_int
nScopeAPI.nScope_set_AX_amplitude.argtypes = [POINTER(scopeDev), c_int, c_double]
nScopeAPI.nScope_get_AX_amplitude.restype = c_int
nScopeAPI.nScope_get_AX_amplitude.argtypes = [POINTER(scopeDev), c_int, POINTER(c_double)]

    	# 	if rtrn == -101:
    	# 		raise RuntimeError("nScope is not connected")
    	# 		return
            	# 	if wave.lower() == 'sine' or wave.lower() == 'sin':
            	# 		rtrn = nScopeAPI.nScope_set_A1_wave_type(self.handle,0)
            	# 	elif wave.lower() == 'triangle' or wave.lower() == 'tri':
            	# 		rtrn = nScopeAPI.nScope_set_A1_wave_type(self.handle,1)
            	# 	else:
            	# 		raise ValueError("Unknown wave type: "+wave)
            	# 		return
            	# 	if rtrn is 0:
            	# 		return 'Sine'
            	# 	elif rtrn is 1:
            	# 		return 'Triangle'

class Implementation:
    def setAXOn(self,ax,axOn):
        axOn = bool(axOn)
        nScopeAPI.nScope_set_AX_on(self.handle,ax,axOn)
        return

    def getAXOn(self,ax):
        axOn = c_bool()
        nScopeAPI.nScope_get_AX_on(self.handle,ax,byref(axOn))
        return axOn.value

    def setAXFrequencyInHz(self,ax,axFrequency):
        nScopeAPI.nScope_set_AX_frequency_in_hz(self.handle,ax,axFrequency)
        return

    def getAXFrequencyInHz(self,ax):
        axFrequency = c_double()
        nScopeAPI.nScope_get_AX_frequency_in_hz(self.handle,ax,byref(axFrequency))
        return axFrequency.value

    def setAXWaveType(self,ax,axWave):
        nScopeAPI.nScope_set_AX_wave_type(self.handle,ax,axWave)
        return

    def getAXWaveType(self,ax):
        axWave = c_int()
        nScopeAPI.nScope_get_AX_wave_type(self.handle,ax,byref(axWave))
        return axWave.value

    def setAXUnipolar(self,ax,axUnipolar):
        axUnipolar = bool(axUnipolar)
        nScopeAPI.nScope_set_AX_unipolar(self.handle,ax,axUnipolar)
        return

    def getAXUnipolar(self,ax):
        axUnipolar = c_bool()
        nScopeAPI.nScope_get_AX_unipolar(self.handle,ax,byref(axUnipolar))
        return axUnipolar.value

    def setAXAmplitude(self,ax,axAmplitude):
        nScopeAPI.nScope_set_AX_amplitude(self.handle,ax,axAmplitude)
        return

    def getAXAmplitude(self,ax):
        axAmplitude = c_double()
        nScopeAPI.nScope_get_AX_amplitude(self.handle,ax,byref(axAmplitude))
        return axAmplitude.value

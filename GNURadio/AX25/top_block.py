#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun 23 18:53:36 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.Modus_upper = Modus_upper = 431e6
        self.Modus = Modus = 431e6
        self.samp_rate = samp_rate = 192e3
        self.refresh_rate = refresh_rate = 5
        self.low_pass_cutoff_freq = low_pass_cutoff_freq = 5000
        self.center_freq = center_freq = Modus_upper-Modus
        self.baseband_freq = baseband_freq = 0
        self.IFGain = IFGain = 7
        self.FrequencyOffset = FrequencyOffset = 10
        self.Decim = Decim = 4
        self.Decay = Decay = 0.1
        self.Attack = Attack = 0.8

        ##################################################
        # Blocks
        ##################################################
        self._low_pass_cutoff_freq_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.low_pass_cutoff_freq,
        	callback=self.set_low_pass_cutoff_freq,
        	label='low_pass_cutoff_freq',
        	choices=[5000, 15000, 14900],
        	labels=['5000', '15000', '14900'],
        )
        self.Add(self._low_pass_cutoff_freq_chooser)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(100e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/4, low_pass_cutoff_freq, 1000, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(1)
        self._Modus_upper_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.Modus_upper,
        	callback=self.set_Modus_upper,
        	label='Modus_upper',
        	choices=[144.18e6, 431e6],
        	labels=['144.2 MHz', '431 MHz'],
        )
        self.Add(self._Modus_upper_chooser)
        self._Modus_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.Modus,
        	callback=self.set_Modus,
        	label='Modus',
        	choices=[144.18e6, 431e6, 438e6],
        	labels=['144.2 MHz', '431 MHz', '438 MHz'],
        )
        self.Add(self._Modus_chooser)
        _IFGain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._IFGain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_IFGain_sizer,
        	value=self.IFGain,
        	callback=self.set_IFGain,
        	label='IFGain',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._IFGain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_IFGain_sizer,
        	value=self.IFGain,
        	callback=self.set_IFGain,
        	minimum=1,
        	maximum=25,
        	num_steps=25,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_IFGain_sizer)
        _FrequencyOffset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._FrequencyOffset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_FrequencyOffset_sizer,
        	value=self.FrequencyOffset,
        	callback=self.set_FrequencyOffset,
        	label='FrequencyOffset',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._FrequencyOffset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_FrequencyOffset_sizer,
        	value=self.FrequencyOffset,
        	callback=self.set_FrequencyOffset,
        	minimum=-20,
        	maximum=20,
        	num_steps=40,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_FrequencyOffset_sizer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))    


    def get_Modus_upper(self):
        return self.Modus_upper

    def set_Modus_upper(self, Modus_upper):
        self.Modus_upper = Modus_upper
        self._Modus_upper_chooser.set_value(self.Modus_upper)
        self.set_center_freq(self.Modus_upper-self.Modus)

    def get_Modus(self):
        return self.Modus

    def set_Modus(self, Modus):
        self.Modus = Modus
        self._Modus_chooser.set_value(self.Modus)
        self.set_center_freq(self.Modus_upper-self.Modus)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/4, self.low_pass_cutoff_freq, 1000, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_refresh_rate(self):
        return self.refresh_rate

    def set_refresh_rate(self, refresh_rate):
        self.refresh_rate = refresh_rate

    def get_low_pass_cutoff_freq(self):
        return self.low_pass_cutoff_freq

    def set_low_pass_cutoff_freq(self, low_pass_cutoff_freq):
        self.low_pass_cutoff_freq = low_pass_cutoff_freq
        self._low_pass_cutoff_freq_chooser.set_value(self.low_pass_cutoff_freq)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/4, self.low_pass_cutoff_freq, 1000, firdes.WIN_HAMMING, 6.76))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_baseband_freq(self):
        return self.baseband_freq

    def set_baseband_freq(self, baseband_freq):
        self.baseband_freq = baseband_freq

    def get_IFGain(self):
        return self.IFGain

    def set_IFGain(self, IFGain):
        self.IFGain = IFGain
        self._IFGain_slider.set_value(self.IFGain)
        self._IFGain_text_box.set_value(self.IFGain)

    def get_FrequencyOffset(self):
        return self.FrequencyOffset

    def set_FrequencyOffset(self, FrequencyOffset):
        self.FrequencyOffset = FrequencyOffset
        self._FrequencyOffset_slider.set_value(self.FrequencyOffset)
        self._FrequencyOffset_text_box.set_value(self.FrequencyOffset)

    def get_Decim(self):
        return self.Decim

    def set_Decim(self, Decim):
        self.Decim = Decim

    def get_Decay(self):
        return self.Decay

    def set_Decay(self, Decay):
        self.Decay = Decay

    def get_Attack(self):
        return self.Attack

    def set_Attack(self, Attack):
        self.Attack = Attack


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun May 15 21:53:24 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.Modus_upper = Modus_upper = 431e6
        self.Modus = Modus = 144.18e6
        self.samp_rate = samp_rate = 9600*20
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
        self.wxgui_waterfallsink2_0_0_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=baseband_freq,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=refresh_rate,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.Add(self.wxgui_waterfallsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0_1_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=baseband_freq,
        	y_per_div=20,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=refresh_rate,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0_1_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(Modus-FrequencyOffset, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(IFGain, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/4, low_pass_cutoff_freq, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self._Modus_upper_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.Modus_upper,
        	callback=self.set_Modus_upper,
        	label='Modus_upper',
        	choices=[144.18e6, 431e6, 438e6],
        	labels=['144.2 MHz', '431 MHz', '438 MHz'],
        )
        self.Add(self._Modus_upper_chooser)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0_0_1_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_waterfallsink2_0_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    

    def get_Modus_upper(self):
        return self.Modus_upper

    def set_Modus_upper(self, Modus_upper):
        self.Modus_upper = Modus_upper
        self.set_center_freq(self.Modus_upper-self.Modus)
        self._Modus_upper_chooser.set_value(self.Modus_upper)

    def get_Modus(self):
        return self.Modus

    def set_Modus(self, Modus):
        self.Modus = Modus
        self._Modus_chooser.set_value(self.Modus)
        self.rtlsdr_source_0.set_center_freq(self.Modus-self.FrequencyOffset, 0)
        self.set_center_freq(self.Modus_upper-self.Modus)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_1_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/4, self.low_pass_cutoff_freq, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

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
        self.wxgui_waterfallsink2_0_0_0.set_baseband_freq(self.baseband_freq)
        self.wxgui_fftsink2_0_0_1_0.set_baseband_freq(self.baseband_freq)

    def get_IFGain(self):
        return self.IFGain

    def set_IFGain(self, IFGain):
        self.IFGain = IFGain
        self._IFGain_slider.set_value(self.IFGain)
        self._IFGain_text_box.set_value(self.IFGain)
        self.rtlsdr_source_0.set_if_gain(self.IFGain, 0)

    def get_FrequencyOffset(self):
        return self.FrequencyOffset

    def set_FrequencyOffset(self, FrequencyOffset):
        self.FrequencyOffset = FrequencyOffset
        self._FrequencyOffset_slider.set_value(self.FrequencyOffset)
        self._FrequencyOffset_text_box.set_value(self.FrequencyOffset)
        self.rtlsdr_source_0.set_center_freq(self.Modus-self.FrequencyOffset, 0)

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


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

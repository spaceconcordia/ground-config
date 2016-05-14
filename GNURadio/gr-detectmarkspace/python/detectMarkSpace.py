# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Detectmarkspace
# Generated: Fri May 13 19:57:30 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes


class detectMarkSpace(gr.hier_block2):

    def __init__(self, decay=0.001, samp_rate=48000, attack=0.1, Frequency=1200):
        gr.hier_block2.__init__(
            self, "Detectmarkspace",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signaturev(2, 2, [gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.decay = decay
        self.samp_rate = samp_rate
        self.attack = attack
        self.Frequency = Frequency

        ##################################################
        # Variables
        ##################################################
        self.Baud = Baud = 1200

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, Baud, 0.35, samp_rate/Baud))
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.5, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -Frequency, 1, 0)
        self.analog_agc2_xx_0 = analog.agc2_ff(attack, decay, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(1.0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_sub_xx_0, 0), (self, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    

    def get_decay(self):
        return self.decay

    def set_decay(self, decay):
        self.decay = decay
        self.analog_agc2_xx_0.set_decay_rate(self.decay)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.Baud, 0.35, self.samp_rate/self.Baud))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack
        self.analog_agc2_xx_0.set_attack_rate(self.attack)

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self.analog_sig_source_x_0.set_frequency(-self.Frequency)

    def get_Baud(self):
        return self.Baud

    def set_Baud(self, Baud):
        self.Baud = Baud
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.Baud, 0.35, self.samp_rate/self.Baud))

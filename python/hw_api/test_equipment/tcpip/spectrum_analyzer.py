import socket
from time import sleep

def wait(secs):
    time.sleep(secs)
    

class SpecAnAgilent:

    # Input Parameters: host [string] and port [integer]
    def __init__(self, host, port):
        self.h = host
        self.p = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.h, self.p))
        self.s.send(('*cls\n').encode())

    def get_identity(self):
        self.s.send(('*idn?\n').encode())
        sleep(0.5)
        return (self.s.recv(4096)).decode().rstrip()

    def set_reset(self):
        self.s.send(('*rst' + '\n').encode())           #resets specan
        self.s.send((':init:cont on' + '\n').encode())  #sets measurement to continuous mode

    def set_clear(self):
        self.s.send(('*cls\n').encode())

    def set_freq_center(self, input1):
        self.s.send((':freq:center ' + input1 + '\n').encode())

    def set_freq_start(self, input1):
        self.s.send((':freq:start ' + input1 + '\n').encode())

    def set_freq_stop(self, input1):
        self.s.send((':freq:stop ' + input1 + '\n').encode())

    def set_freq_span(self, input1):
        self.s.send((':freq:span ' + input1 + '\n').encode())

    def set_rbw(self, input1):
        self.s.send((':band ' + input1 + '\n').encode())

    def set_vbw(self, input1):
        self.s.send((':band:vid ' + input1 + '\n').encode())

    def set_ref_level(self, input1):
        self.s.send((':disp:wind:trac:y:rlev ' + input1 + '\n').encode())

    def get_freq(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':x? \n').encode())
        sleep(0.1)
        return (self.s.recv(4096)).decode().rstrip()

    def get_ampl(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':y? \n').encode())
        sleep(0.1)
        return (self.s.recv(4096)).decode().rstrip()

    def set_peak_search(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':state on \n :calc:mark' + marker_num + ':max:peak \n').encode())

    def set_next_peak(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':max:next \n').encode())

    def set_next_peak_right(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':max:right \n').encode())

    def set_next_peak_left(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':max:left \n').encode())

    def set_marker_on(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':state on' + '\n').encode())

    def set_marker_normal(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':mode pos' + '\n').encode())

    def set_marker_delta(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':mode delta' + '\n').encode())
    
    def set_marker_off(self, marker_num):
        self.s.send((':calc:mark' + marker_num + ':mode off' + '\n').encode())

    def get_meas_marker(self, rbw, vbw, span, ref_level):
        self.set_rbw(rbw)
        self.set_vbw(vbw)
        self.set_freq_span(span)
        self.set_ref_level(ref_level)
        freq = self.get_freq()
        ampl = self.get_ampl()
        return freq, ampl    

    def set_save_image(self, filename):
        self.s.send((':mmem:stor:scr \"' + filename + '\"' + '\n').encode())

    def set_scpi_command(self, scpi_text):
        self.s.send((scpi_text + '\n').encode())

    def close(self):
        self.s.close()

    '''
    # Future Functions
    def get_channel_power(input1):
        return 'need to implement'


    Test Script
    from spectrum_analyzer import SpecAnAgilent
    
    host = '127.0.0.1'
    port = 5025  #default SCPI port
    sa = SpecAnAgilent(host, port)
    print(sa.get_identity())
    sa.close()
    '''


function [delta_f] = doppler_shift(v_r, f_a, c)

%--------------------------------------------------------------------------
% Title:            Doppler Shift
% Description:      Find frequency shift due to Doppler Effect
% Author:           Shawn Bulger
%
% REFERENCES:        
%   http://www.grc.nasa.gov/WWW/K-12/airplane/doppler.html
%   http://www.wseas.us/e-library/conferences/2006madrid/papers/502-497.pdf
%
% INPUT PARAMETERS
% v_r           -   relative velocity of emitter to the receiver
% f_a           -   actual (known) frequency of wave
% c             -   speed of wave (sound or light speed)

% INTERNAL PARAMETERS
% lambda_a      -   apparent wavelength

% OUTPUT PARAMETERS
% delta_f       -   the change in frequency as a result of doppler shift
%--------------------------------------------------------------------------

lambda_a = f_a * ( c / (c + v_r) )
delta_f = c / lambda_a

% END FUNCTION
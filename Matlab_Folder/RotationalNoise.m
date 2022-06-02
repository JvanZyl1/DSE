function SPL = RotationalNoise(theta,S,m,B,omega,a,T,Q,R_e,rho,N,c,t_max)
    %https://tud365.sharepoint.com/sites/UrbanTurbulence/Gedeelde%20documenten/Forms/AllItems.aspx?FolderCTID=0x0120000A9B2D4B22DBA94F9BFBB3D4E117EB61&id=%2Fsites%2FUrbanTurbulence%2FGedeelde%20documenten%2FGeneral%2FLiterature%2FApproach%20for%20aeroacoustics%2FNoiseModel%2Epdf&parent=%2Fsites%2FUrbanTurbulence%2FGedeelde%20documenten%2FGeneral%2FLiterature%2FApproach%20for%20aeroacoustics
    %theta is azimuthal angle ( angle of observer with respect to the
    %vehicle -Z axis) [rad]
    %S is the radial distance from the vehicle to the observer [m]
    %m is the harmonic number [positive integer]
    %B is the amount of blades per rotor [-]
    % omega is the rotational velocity of the rotor [rad/s]
    % a is the speed of sound [m/s]
    % T is the thrust created by a rotor [N]
    % Q is the torque on a rotor [Nm]
    % R_e is the effective rotor radius (0.8*R_rotor) [m]
    % rho is the air density [kg m^-3]
    % N is the number of rotors [N]
    % Rotors are assumed to be identical. Ask me if you want it different.
    
    pref = 2e-5; %Reference pressure [Pa]

    function p_m_L = LoadingNoise(theta,S,m,B,omega,a,T,Q,R_e)
        % Estimation of loading noise root mean square sound pressure
        J=besselj(m*B,(m*B*omega/a)*R_e.*sin(theta)); %Bessel function of first kind
        p_m_L= m*B*omega/(2*sqrt(2)*pi*a*S)*(T.*cos(theta)-Q.*a./(omega*R_e^2)).*J;
    end
    function p_m_T = ThicknessNoise(theta,S,rho,m,B,omega,c,t_max,R_e,a)
        % Estimation of thickness noise root mean square sound pressure
        J=besselj(m*B,(m*B*omega/a)*R_e.*sin(theta)); %Bessel function of first kind
        p_m_T = -rho*(m*B*omega)^2*B/(3*sqrt(2)*pi*S)*c*t_max*R_e.*J;
    end 
    pmL = LoadingNoise(theta,S,m,B,omega,a,T,Q,R_e);
    pmT = ThicknessNoise(theta,S,rho,m,B,omega,c,t_max,R_e,a);
    %Sound pressure level in dB from sound pressure
    display(N*(pmL.^2+pmT.^2)/pref^2)
    SPL = 10*log10(N*(pmL.^2+pmT.^2)/pref^2);
end
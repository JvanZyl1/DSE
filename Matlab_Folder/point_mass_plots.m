%%% For this export the simulink outputs as timeseries


subplot(1,3,1)
plot(out.g_force)
title("Load factor under control maneuver.")
xlabel("Time [s]")
ylabel("g's")

subplot(1,3,2)
plot(out.r)
title("Deviation from trajectory under gust model.")
xlabel("Time [s]")
ylabel("Deviation [m]")

subplot(1,3,3)
plot(out.F_control_minustau)
title("Time-delayed control force.")
xlabel("Time [s]")
ylabel("Force [N]")
sgtitle("Gust control for, C_D:" + C_D + ", S:" + S + ", m:" + m)

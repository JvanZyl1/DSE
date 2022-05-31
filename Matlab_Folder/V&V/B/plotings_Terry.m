legend_tags =  [];
for i = 1:length(a_list)
    i
    a_mg = a_list(i,1);
    c_mg = c_list(i,1);
    K_mg = K_list(i,1);
    tag = "a:" + a_mg + "c:" + c_mg + "Time Delay:" + K_mg;
    legend_tags = [legend_tags, tag];
end

subplot(1,3,1)
plot(xe_list)
legend(legend_tags)
T = readtable('proparms.txt','Delimiter',' ');
[r,c] = size(T);
for ii = 1:r
    eval([T.Var1{ii} '=' num2str(T.Var2(ii))])
end
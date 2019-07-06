f = zeros(1, 150);
ff = zeros(1, 150);

 for i = 1:15
        x = -10^(-i);
        f = -(1-x)/(1+x) + 1/(1+2*x);
        ff = 1/(1+2*x) - (2)/ (x + 1) + 1; 
        fprintf('%10.2e %22.15e %22.15e %12.4e\n', x, f, ff, (f-ff)/ff);
end
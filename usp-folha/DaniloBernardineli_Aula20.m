%Aula 20 - Modelo de Ising em 1D
clear;

%parametros
J = 1;
h = 0;
T = 2;
k_b = 1;

%quantidade de spins
n = 10;
N = 1000;



spin0 = ones(n, 1);

E0 = energiaSpin(spin0, n, J, h);

t_m = 0:0.1:4
avg_m = zeros(length(t_m), 1);
t_i = 1;

for t = t_m
    m = zeros(n,N);
    T = t;
    for j = 1:N
        for i = 1:n
            spin = spin0;

            spin(i) = -spin(i);
            E = energiaSpin(spin, n, J, h);
            Eflip = E - E0;

            if Eflip < 0
                spin0 = spin
            else
                Pflip = exp(-Eflip / T);
                r = rand;
                if r < Pflip
                    spin0 = spin;
                end
            end
            m(i, j) = sum(spin0) / n;        
        end
    end
    avg_m(t_i) = mean2(m);
    t_i = t_i + 1;
end

plot(t_m, avg_m, '+-');
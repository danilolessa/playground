function [ E ] = energiaSpin( listSpin, n, J, h )
%Calcula a energia dos spins
    E = 0;
    for i = 1:n
        if i ~= n
            E = E - J * listSpin(i) * listSpin(i+1) - h * listSpin(i);
        else
            E = E - J * listSpin(i) * listSpin(1) - h * listSpin(i);
        end
    end

end


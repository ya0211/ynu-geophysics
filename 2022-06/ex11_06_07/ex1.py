from digitalSignal import darray, dft, fft_
from digitalSignal.utils import draw


def x(n):
    if 0 <= n <= 8:
        return 1
    else:
        return 0


L = 64
T = 0.4
a = darray(range(0, L), [x(n*T) for n in range(0, L)])
r = fft_(a)
r.round(10)
print(r)

a = [a, abs(r), r.phase(), abs(r)**2]
text = [r'$x(n)$', 'Amplitude Spectrum', 'Phase Spectrum', 'Energy Spectrum']
xlabel = [r'n'] + [r'k']*3
ylabel = [r'$x(n)$', r'$\left | X(k) \right |$', r'$\theta (k)$', r'$\left | X(k) \right |^{2}$']
draw(a=a, text=text,
     xlabel=xlabel, ylabel=ylabel,
     style="plot", grid='--',
     file_name="figure-fft-L{0}.pdf".format(L))

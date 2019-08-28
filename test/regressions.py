from collections import namedtuple

Regression = namedtuple("Regression", ["wave", "hscale", "period", "phase", "expected"])
Regression.__new__.__defaults__ = ("", 1, 1, 0, [])


basic = [
    Regression(wave="P", expected=['Pclk', 'nclk']),
    Regression(wave="P", hscale=2, expected=['Pclk', '111', 'nclk', '000']),
    Regression(wave="P", period=2, expected=['Pclk', '111', 'nclk', '000']),
    Regression(wave="P", hscale=2, period=0.5, expected=['Pclk', 'nclk']),
    Regression(wave="P", phase=1, expected=['nclk']),
    Regression(wave="P", hscale=2, phase=2, expected=['nclk', '000']),
    Regression(wave="P.", expected=['Pclk', 'nclk', 'Pclk', 'nclk']),
    Regression(wave="P..", expected=['Pclk', 'nclk', 'Pclk', 'nclk', 'Pclk', 'nclk']),
    Regression(wave="P.", hscale=2, expected=['Pclk', '111', 'nclk', '000', 'Pclk', '111', 'nclk', '000']),
    Regression(wave="P..", hscale=2, expected=['Pclk', '111', 'nclk', '000', 'Pclk', '111', 'nclk', '000',
                                               'Pclk', '111', 'nclk', '000']),
    Regression(wave="px", expected=['pclk', 'nclk', '0mx', 'xxx']),
    Regression(wave="hx", expected=['111', '111', '1mx', 'xxx']),
    Regression(wave="nx", expected=['nclk', 'pclk', '1mx', 'xxx']),
    Regression(wave="lx", expected=['000', '000', '0mx', 'xxx']),
    Regression(wave="Px", expected=['Pclk', 'nclk', '0mx', 'xxx']),
    Regression(wave="Hx", expected=['111', '111', '1mx', 'xxx']),
    Regression(wave="Nx", expected=['Nclk', 'pclk', '1mx', 'xxx']),
    Regression(wave="Lx", expected=['000', '000', '0mx', 'xxx']),
    Regression(wave="xpx", expected=['xxx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx']),
    Regression(wave="xhx", expected=['xxx', 'xxx', 'pclk', '111', '1mx', 'xxx']),
    Regression(wave="xnx", expected=['xxx', 'xxx', 'nclk', 'pclk', '1mx', 'xxx']),
    Regression(wave="xlx", expected=['xxx', 'xxx', 'nclk', '000', '0mx', 'xxx']),
    Regression(wave="xPx", expected=['xxx', 'xxx', 'Pclk', 'nclk', '0mx', 'xxx']),
    Regression(wave="xHx", expected=['xxx', 'xxx', 'Pclk', '111', '1mx', 'xxx']),
    Regression(wave="xNx", expected=['xxx', 'xxx', 'Nclk', 'pclk', '1mx', 'xxx']),
    Regression(wave="xLx", expected=['xxx', 'xxx', 'Nclk', '000', '0mx', 'xxx']),
    Regression(wave="0", expected=['000', '000']),
    Regression(wave="1", expected=['111', '111']),
    Regression(wave="01", expected=['000', '000', '0m1', '111']),
    Regression(wave="01", hscale=2, expected=['000', '000', '000', '000', '0m1', '111', '111', '111']),
    Regression(wave="01.0", expected=['000', '000', '0m1', '111', '111', '111', '1m0', '000']),
    Regression(wave="01.zx=ud.23.45",
               expected=['000', '000', '0m1', '111', '111', '111', '1mz', 'zzz', 'zmx', 'xxx', 'xmv-2', 'vvv-2',
                         'vmu-2', 'uuu', 'umd', 'ddd', 'ddd', 'ddd', 'dmv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vvv-3',
                         'vvv-3', 'vmv-3-4', 'vvv-4', 'vmv-4-5', 'vvv-5']),
    Regression(wave="01.zx=ud.23.45", hscale=2,
               expected=['000', '000', '000', '000', '0m1', '111', '111', '111', '111', '111', '111', '111', '1mz',
                         'zzz', 'zzz', 'zzz', 'zmx', 'xxx', 'xxx', 'xxx', 'xmv-2', 'vvv-2', 'vvv-2', 'vvv-2', 'vmu-2',
                         'uuu', 'uuu', 'uuu', 'umd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'dmv-2', 'vvv-2',
                         'vvv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3',
                         'vvv-3', 'vmv-3-4', 'vvv-4', 'vvv-4', 'vvv-4', 'vmv-4-5', 'vvv-5', 'vvv-5', 'vvv-5']),
    Regression(wave="phnlPHNL", expected=['pclk', 'nclk', 'pclk', '111', 'nclk', 'pclk', 'nclk', '000', 'Pclk', 'nclk',
                                          'Pclk', '111', 'Nclk', 'pclk', 'Nclk', '000']),
    Regression(wave="xhlhLHl.", expected=['xxx', 'xxx', 'pclk', '111', 'nclk', '000', 'pclk', '111', 'Nclk', '000',
                                          'Pclk', '111', 'nclk', '000', '000', '000']),
    Regression(wave="hpHplnLn", expected=['111', '111', '111', 'nclk', 'Pclk', '111', '111', 'nclk', '000', '000',
                                          '000', 'pclk', 'Nclk', '000', '000', 'pclk']),
    Regression(wave="nhNhplPl", expected=['nclk', 'pclk', '111', '111', 'Nclk', 'pclk', '111', '111', '111', 'nclk',
                                          '000', '000', 'Pclk', 'nclk', '000', '000']),
    Regression(wave="xlh.L.Hx", expected=['xxx', 'xxx', 'nclk', '000', 'pclk', '111', '111', '111', 'Nclk', '000',
                                          '000', '000', 'Pclk', '111', '1mx', 'xxx'])
]

period = [
    Regression(wave="h.nh.nh.l..hlx.hlx.hlx.hlx.hlx.hlx.hlx.hlx.hnh.l..hlx.hlx.h", period=0.5,
               expected=['111', '111', 'nclk', 'pclk', '111', '111', 'nclk', 'pclk', '111', '111', 'nclk', '000', '000',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', 'pclk', '111',
                         '111', 'nclk', '000', '000', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk']),
    Regression(wave="h.lh..lh..l..hlx.hlx.hlx.hlx.hlx.hlx.hlx.hlx.hnh.l..hlx.hlx.h", period=0.5,
               expected=['111', '111', 'nclk', 'pclk', '111', '111', 'nclk', 'pclk', '111', '111', 'nclk', '000', '000',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', 'pclk', '111',
                         '111', 'nclk', '000', '000', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk']),
    Regression(wave="0..............................................50.............", period=0.5,
               expected=['000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
                         '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
                         '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
                         '000', '000', '000', '000', '000', '000', '000', '000', '0mv-5', 'vm0-5', '000', '000', '000',
                         '000', '000', '000', '000', '000', '000', '000', '000', '000', '000']),
]

subcycle = [
    Regression(wave="0<10>1", expected=['000', '000', '0m1', '1m0', '0m1', '111']),
    Regression(wave="<10>10", expected=['111', '1m0', '0m1', '111', '1m0', '000']),
    Regression(wave="<x0>1x", expected=['xxx', 'xm0', '0m1', '111', '1mx', 'xxx']),
    Regression(wave="<01>", expected=['000', '0m1']),
    Regression(wave="x.<01...0>x", expected=['xxx', 'xxx', 'xxx', 'xxx', 'xm0', '0m1', '111', '111', '111', '1m0',
                                             '0mx', 'xxx']),
    Regression(wave="==2<30>2<0xx1>2333444555",
               expected=['vvv-2', 'vvv-2', 'vmv-2-2', 'vvv-2', 'vmv-2-2', 'vvv-2', 'vmv-2-3', 'vm0-3', '0mv-2', 'vvv-2',
                         'vm0-2', '0mx', 'xmx', 'xm1', '1mv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vmv-3-3', 'vvv-3',
                         'vmv-3-3', 'vvv-3', 'vmv-3-4', 'vvv-4', 'vmv-4-4', 'vvv-4', 'vmv-4-4', 'vvv-4', 'vmv-4-5',
                         'vvv-5', 'vmv-5-5', 'vvv-5', 'vmv-5-5', 'vvv-5']),
    Regression(wave="=2<15.1>2<01>2355",
               expected=['vvv-2', 'vvv-2', 'vmv-2-2', 'vvv-2', 'vm1-2', '1mv-5', 'vvv-5', 'vm1-5', '1mv-2', 'vvv-2',
                         'vm0-2', '0m1', '1mv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vmv-3-5', 'vvv-5', 'vmv-5-5', 'vvv-5']),
    Regression(wave="=2<1001.1>2<01.5>3",
               expected=['vvv-2', 'vvv-2', 'vmv-2-2', 'vvv-2', 'vm1-2', '1m0', '0m0', '0m1', '111', '1m1', '1mv-2',
                         'vvv-2', 'vm0-2', '0m1', '111', '1mv-5', 'vmv-5-3', 'vvv-3']),
    Regression(wave="=2<10zuzd1x.1>2",
               expected=['vvv-2', 'vvv-2', 'vmv-2-2', 'vvv-2', 'vm1-2', '1m0', '0mz', 'zmu', 'umz', 'zmd', 'dm1', '1mx',
                         'xxx', 'xm1', '1mv-2', 'vvv-2']),
    Regression(wave="<=|>.x", expected=['vvv-2', 'vvv-2', 'vvv-2', 'vvv-2', 'vmx-2', 'xxx']),
    Regression(wave="x<=|>.x", expected=['xxx', 'xxx', 'xmv-2', 'vvv-2', 'vvv-2', 'vvv-2', 'vmx-2', 'xxx']),
    Regression(wave="x<.|>0x", expected=['xxx', 'xxx', 'xxx', 'xxx', 'xm0', '000', '0mx', 'xxx']),
    Regression(wave="hnhnhln<lx.h><lx.h><lx.h><lx.h><lx.h><lx.h><lx.h><lx.h>nhln<lx.h><lx.h>",
               expected=['111', '111', 'nclk', 'pclk', '111', '111', 'nclk', 'pclk', '111', '111', 'nclk', '000', '000',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', 'pclk', '111',
                         '111', 'nclk', '000', '000', 'pclk', 'nclk', '0mx', 'xxx', 'pclk', 'nclk', '0mx', 'xxx',
                         'pclk']),
]

all = basic + period + subcycle
//spartacous
/*
A module that computes analytic sigmoids, useful to interpolate between the two different scalings of x(a) = m_pacdr/T_pacdr(a), and their derivatives. They are written in terms of alpha = a/a_tr.

Currently only two sigmoids are implemented: Tanh-based, and an asymmetric exponentials-based. The asymmetric one fits better, but its parameters have a slightly larger dependence on r_g.

These are analytical methods, and they are accurate down to ~O(1%) level, according to my tests.

The purpose of these methods is to serve as a good initial guess of x(a) for the full numerical solution, found in numericx.c

Written by: Manuel A. Buen-Abad, 2022.
*/
#if !defined(_sigmoids_)
#define _sigmoids_

extern double tanh_sigmoid( double, double, double );
extern double d_tanh_sigmoid( double, double, double );
extern double asym_sigmoid( double, double, double, double, double );
extern double d_asym_sigmoid( double, double, double, double, double );
extern double x_over_alpha( double, double );
extern double dx_dalpha( double, double );

// best-fit shape parameters for the sigmoids used. Obtained in Mathematica, fitting with quadratures.
#define _tanh_Delta_  2.40794
#define _tanh_alpha0_ 2.23585

#define _asym_Delta_  2.2841
#define _asym_alpha0_ 3.07686
#define _asym_powL_   0.560665
#define _asym_powR_   1.40871

#endif
//spartacous

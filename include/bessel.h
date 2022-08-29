//spartacous: shamelessly copied from the one place I found with modified Bessel functions of the second kind implemented in C: https://github.com/kapteyn-astro/gipsy
// NOTE: this is a slightly modified version of the original, in order to suit our purposes.
#if !defined(_bessel_h_)
#define _bessel_h_
extern double bessj( int, double );
extern double bessy( int, double );
extern double bessi( int, double );
extern double bessk( int, double );
#endif
//spartacous

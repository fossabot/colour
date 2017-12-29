#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from colour.utilities import CaseInsensitiveMapping, filter_kwargs

from .delta_e import (delta_E_CIE1976, delta_E_CIE1994, delta_E_CIE2000,
                      delta_E_CMC)
from .delta_e_cam02_ucs import (delta_E_CAM02LCD, delta_E_CAM02SCD,
                                delta_E_CAM02UCS)
from .delta_e_cam16_ucs import (delta_E_CAM16LCD, delta_E_CAM16SCD,
                                delta_E_CAM16UCS)
__all__ = [
    'delta_E_CIE1976', 'delta_E_CIE1994', 'delta_E_CIE2000', 'delta_E_CMC'
]
__all__ += ['delta_E_CAM02LCD', 'delta_E_CAM02SCD', 'delta_E_CAM02UCS']
__all__ += ['delta_E_CAM16LCD', 'delta_E_CAM16SCD', 'delta_E_CAM16UCS']

DELTA_E_METHODS = CaseInsensitiveMapping({
    'CIE 1976': delta_E_CIE1976,
    'CIE 1994': delta_E_CIE1994,
    'CIE 2000': delta_E_CIE2000,
    'CMC': delta_E_CMC,
    'CAM02-LCD': delta_E_CAM02LCD,
    'CAM02-SCD': delta_E_CAM02SCD,
    'CAM02-UCS': delta_E_CAM02UCS,
    'CAM16-LCD': delta_E_CAM16LCD,
    'CAM16-SCD': delta_E_CAM16SCD,
    'CAM16-UCS': delta_E_CAM16UCS,
})
"""
Supported :math:`\Delta E_{ab}` computations methods.

DELTA_E_METHODS : CaseInsensitiveMapping
    **{'CIE 1976', 'CIE 1994', 'CIE 2000', 'CMC', 'CAM02-LCD', 'CAM02-SCD',
    'CAM02-UCS', 'CAM16-LCD', 'CAM16-SCD', 'CAM16-UCS'}**

Aliases:

-   'cie1976': 'CIE 1976'
-   'cie1994': 'CIE 1994'
-   'cie2000': 'CIE 2000'
"""
DELTA_E_METHODS['cie1976'] = DELTA_E_METHODS['CIE 1976']
DELTA_E_METHODS['cie1994'] = DELTA_E_METHODS['CIE 1994']
DELTA_E_METHODS['cie2000'] = DELTA_E_METHODS['CIE 2000']


def delta_E(a, b, method='CIE 2000', **kwargs):
    """
    Returns the difference :math:`\Delta E_{ab}` between two given
    *CIE L\*a\*b\** or :math:`J'a'b'` colourspace arrays using given method.

    Parameters
    ----------
    a : array_like
        *CIE L\*a\*b\** or :math:`J'a'b'` colourspace array :math:`a`.
    b : array_like
        *CIE L\*a\*b\** or :math:`J'a'b'` colourspace array :math:`b`.
    method : unicode, optional
        **{'CIE 2000', 'CIE 1976', 'CIE 1994', 'CMC', 'CAM02-LCD', 'CAM02-SCD',
        'CAM02-UCS', 'CAM16-LCD', 'CAM16-SCD', 'CAM16-UCS'}**
        Computation method.

    Other Parameters
    ----------------
    textiles : bool, optional
        {:func:`delta_E_CIE1994`, :func:`delta_E_CIE2000`},
        Textiles application specific parametric factors
        :math:`k_L=2,\ k_C=k_H=1,\ k_1=0.048,\ k_2=0.014` weights are used
        instead of :math:`k_L=k_C=k_H=1,\ k_1=0.045,\ k_2=0.015`.
    l : numeric, optional
        {:func:`delta_E_CIE2000`},
        Lightness weighting factor.
    c : numeric, optional
        {:func:`delta_E_CIE2000`},
        Chroma weighting factor.

    Returns
    -------
    numeric or ndarray
        Colour difference :math:`\Delta E_{ab}`.

    Examples
    --------
    >>> import numpy as np
    >>> a = np.array([100.00000000, 21.57210357, 272.22819350])
    >>> b = np.array([100.00000000, 426.67945353, 72.39590835])
    >>> delta_E(a, b)  # doctest: +ELLIPSIS
    94.0356490...
    >>> delta_E(a, b, method='CIE 2000')  # doctest: +ELLIPSIS
    94.0356490...
    >>> delta_E(a, b, method='CIE 1976')  # doctest: +ELLIPSIS
    451.7133019...
    >>> delta_E(a, b, method='CIE 1994')  # doctest: +ELLIPSIS
    83.7792255...
    >>> delta_E(a, b, method='CIE 1994', textiles=False)
    ... # doctest: +ELLIPSIS
    83.7792255...
    >>> a = np.array([54.90433134, -0.08450395, -0.06854831])
    >>> b = np.array([54.90433134, -0.08442362, -0.06848314])
    >>> delta_E(a, b, method='CAM02-UCS')  # doctest: +ELLIPSIS
    0.0001034...
    >>> delta_E(a, b, method='CAM16-LCD')  # doctest: +ELLIPSIS
    0.0001034...
    """

    function = DELTA_E_METHODS[method]

    return function(a, b, **filter_kwargs(function, **kwargs))


__all__ += ['delta_E']

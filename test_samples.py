import numpy as np

"""year 2024"""
sample1 = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.23,0.46,0.00,0.00,0.00,0.00,0.00,0.08,5.64,7.40,2.06,0.00,0.00,0.00,0.00,2.52,7.62,7.47,5.34,0.00,0.00,0.00,0.00,0.46,2.59,6.10,5.34,0.00,0.00,0.00,0.00,0.00,0.38,7.01,4.96,0.00,0.00,0.00,0.00,0.00,3.97,7.62,7.47,6.25,5.72,1.53,0.00,0.00,2.29,3.89,3.89,4.58,6.48,2.67],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.61,0.15,0.00,0.00,0.00,0.00,0.00,2.75,7.55,7.09,4.27,0.00,0.00,0.00,3.35,7.55,5.65,5.03,7.62,2.59,0.00,1.76,7.62,5.12,0.38,0.00,6.41,6.40,0.00,2.90,7.62,1.30,0.00,0.00,3.05,7.63,1.98,0.77,7.55,5.72,2.37,0.23,0.84,7.62,3.05,0.00,3.05,7.32,7.62,7.56,6.71,7.62,1.83],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.97,4.57,3.89,0.31,0.00,0.00,0.00,0.69,7.47,6.79,7.55,5.56,0.00,0.00,0.00,0.54,5.80,1.14,5.57,6.10,0.00,0.00,0.00,0.00,0.00,3.28,7.55,4.27,0.00,0.00,0.00,0.00,3.43,7.62,7.63,5.42,1.37,0.00,0.00,2.98,7.62,7.62,7.47,7.09,5.57,0.00,0.00,6.03,6.86,3.90,0.53,0.30,0.31,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.23,4.27,0.69,0.00,0.00,0.00,5.72,5.34,1.98,7.62,1.98,0.00,0.00,0.92,7.62,7.55,6.25,7.62,4.35,0.23,0.00,0.00,2.06,4.04,6.94,7.62,7.40,0.99,0.00,0.00,0.00,0.00,2.29,7.62,1.53,0.00,0.00,0.00,0.00,0.00,1.53,7.62,1.98,0.00]
])

"""year 2035"""
sample2 = np.array(
    [
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.76,
            4.50,
            4.12,
            0.69,
            0.00,
            0.00,
            0.00,
            0.00,
            4.20,
            7.47,
            7.55,
            4.27,
            0.00,
            0.00,
            0.00,
            0.00,
            1.07,
            1.98,
            6.86,
            4.57,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.15,
            7.55,
            4.04,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            1.99,
            7.62,
            4.35,
            1.15,
            0.00,
            0.00,
            0.00,
            0.00,
            5.95,
            7.62,
            7.62,
            7.62,
            6.64,
            5.11,
            0.00,
            0.00,
            1.98,
            2.06,
            1.38,
            3.36,
            5.04,
            4.88,
        ],
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            1.98,
            5.11,
            1.91,
            0.00,
            0.00,
            0.00,
            0.99,
            5.04,
            7.62,
            7.62,
            5.95,
            1.68,
            0.00,
            0.00,
            6.48,
            7.17,
            3.66,
            3.20,
            7.09,
            7.40,
            0.53,
            0.00,
            7.01,
            5.34,
            0.00,
            0.00,
            1.99,
            7.62,
            2.14,
            0.00,
            3.74,
            7.55,
            2.21,
            0.00,
            1.68,
            7.62,
            2.29,
            0.00,
            0.38,
            6.02,
            7.55,
            4.35,
            3.73,
            7.62,
            1.07,
            0.00,
            0.00,
            0.31,
            4.42,
            7.47,
            7.62,
            6.79,
            0.08,
            0.00,
        ],
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.38,
            5.64,
            5.57,
            0.23,
            0.00,
            0.00,
            0.00,
            0.00,
            1.38,
            7.55,
            7.62,
            2.67,
            0.00,
            0.00,
            0.00,
            0.00,
            1.83,
            7.47,
            7.62,
            7.55,
            1.98,
            0.00,
            0.00,
            0.00,
            0.69,
            3.66,
            1.68,
            7.63,
            3.81,
            0.00,
            0.00,
            0.00,
            0.38,
            1.68,
            2.36,
            7.63,
            3.66,
            0.00,
            0.00,
            7.17,
            7.62,
            7.62,
            7.62,
            7.55,
            1.60,
            0.00,
            0.00,
            3.05,
            3.59,
            2.37,
            0.84,
            0.53,
            0.00,
            0.00,
            0.00,
        ],
        [
            0.00,
            0.15,
            0.76,
            0.76,
            0.76,
            0.76,
            0.23,
            0.00,
            0.00,
            3.97,
            7.62,
            7.62,
            7.62,
            7.62,
            4.81,
            0.00,
            0.00,
            3.81,
            7.63,
            2.29,
            2.29,
            2.29,
            0.92,
            0.00,
            0.00,
            3.22,
            7.62,
            7.02,
            7.63,
            3.50,
            0.00,
            0.00,
            0.00,
            2.44,
            7.55,
            4.73,
            5.95,
            6.94,
            0.15,
            0.00,
            0.00,
            0.00,
            0.61,
            0.00,
            3.81,
            7.62,
            0.76,
            0.00,
            0.00,
            2.29,
            4.35,
            4.73,
            7.40,
            5.64,
            0.00,
            0.00,
            0.00,
            2.82,
            7.62,
            7.32,
            4.35,
            0.69,
            0.00,
            0.00,
        ],
    ]
)

"""year 3011"""
sample3 = np.array(
    [
        [
            0.00,
            0.00,
            0.31,
            1.45,
            0.76,
            0.00,
            0.00,
            0.00,
            0.00,
            0.23,
            7.17,
            7.62,
            7.17,
            1.60,
            0.00,
            0.00,
            0.00,
            0.00,
            3.36,
            2.83,
            7.25,
            6.79,
            0.00,
            0.00,
            0.00,
            0.00,
            2.52,
            6.56,
            7.62,
            5.49,
            0.00,
            0.00,
            0.00,
            0.92,
            7.62,
            6.87,
            7.62,
            6.41,
            1.91,
            0.00,
            0.00,
            0.00,
            1.98,
            0.23,
            3.89,
            7.63,
            5.11,
            0.00,
            0.00,
            3.97,
            6.10,
            6.79,
            7.62,
            7.55,
            2.21,
            0.00,
            0.00,
            2.97,
            4.88,
            4.58,
            2.90,
            0.38,
            0.00,
            0.00,
        ],
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            2.29,
            0.76,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            1.30,
            7.63,
            7.24,
            4.27,
            0.00,
            0.00,
            0.00,
            0.00,
            4.58,
            7.24,
            5.11,
            7.62,
            1.68,
            0.00,
            0.00,
            0.00,
            6.10,
            5.64,
            0.38,
            7.40,
            4.43,
            0.00,
            0.00,
            0.00,
            4.65,
            7.32,
            2.29,
            7.09,
            4.57,
            0.00,
            0.00,
            0.00,
            0.99,
            6.86,
            7.62,
            7.62,
            3.81,
            0.00,
            0.00,
            0.00,
            0.00,
            1.07,
            2.59,
            0.99,
            0.00,
            0.00,
        ],
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.69,
            0.53,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            5.72,
            5.11,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            6.10,
            5.34,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            6.10,
            5.34,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            6.10,
            5.34,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            5.87,
            5.26,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            1.15,
            0.92,
            0.00,
            0.00,
        ],
        [
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.08,
            2.06,
            0.08,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            1.68,
            7.62,
            2.21,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.54,
            7.63,
            3.51,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            7.41,
            4.20,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            6.19,
            5.27,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            5.04,
            6.41,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            0.00,
            4.04,
            7.39,
            0.16,
            0.00,
        ],
    ]
)

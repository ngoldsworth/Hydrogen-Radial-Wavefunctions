## Module Imports.
import numpy as np
import matplotlib.pyplot as plt

## Function definitions.
def ang_mom_nums(n):
    """
    Creates the angular momentum quantum number from the principle quantum number.
    ---
    Parameters:
        n, int: The princple quantum number.
    ---
    Returns:
        l, list: A list of all the possible l values.
    """

    l = []
    for i in range(n):
        l.append(i)
    
    return l

def radial_func(Z, n, l):
    """
    This function provides the formal definition of the radial part of the hydrogen wavefunction which are Laguerre polynomials.
    ---
    Parameters:
        r, array: An array of the r values.
        n, int: The principle quantum number of the hydrogen system.
        l, int: The angular momentum quantum number of the hydrogen system.
    ---
    Returns:
        prob_amps, array: An array of the radial components of the hydrogen wavefunction.
    """
    
    ## Importing sympy modules that are only used in this function.
    from sympy import Symbol
    from sympy.physics.hydrogen import R_nl
    from sympy.utilities.lambdify import lambdify

    # Making r into a variable.
    r = Symbol('r', real=True, positive=True)

    ## Generating the r array.
    stop = 10
    r_vals = np.linspace(0, stop, num=stop**4)

    ## Creating the radial arrays.
    prob_amps = []
    for i in l:
        rad_func = lambdify([r], R_nl(n, i, r, Z))
        values = []
        for j in r_vals:
            values.append(rad_func(j))
        prob_amps.append(values)
    
    return r_vals, prob_amps

def plotting(n, x, y):
    """
    This function plots x and y on a standard abscissa, ordinate plot.
    ---
    Parameters:
        n, int: The principle quantum number of the hydrogen atom.
        x, array: An array of the x values to be plotted.
        y, array: An array of the y values to be plotted.
    ---
    Returns: None.
    """
    
    ## Describing parameters for the plot(s).
    plt.figure(figsize=(15,9))
    plt.xlabel('r')
    plt.ylabel('Probability')
    plt.title('Hydrogen Wavefunction, n={}'.format(n))

    ## The actual plotting when n=1.
    if len(y) == 1:
        print(y)
        plt.plot(x, x**2 * y[0])
        plt.show()
    
    ## The actual plotting for if n != 1.
    else:
        for i in range(len(y)):
            plt.plot(x, x**2 * y[i], label='l = {}'.format(i))
        plt.legend()
        plt.show()

def main():
    """
    The main function that runs all the other functions and any other code that make the script do its thing.
    ---
    Parameters: None.
    ---
    Returns: None.
    """
    
    ## Asking the user for the number of protons in the nucleus.
    Z = ''
    while type(Z) is not int:
        Z = input('How many protons are in the nucleus of this hydrogenic atom? ')
        try:
            Z = int(Z)
        except:
            print("That's not an integer.")

    ## Asking the user for the value of the principle quantum number.
    n = ''
    while type(n) is not int:
        n = input('What is the value of the principle quantum number? ')
        try:
            n = int(n)
        except:
            print("That is not an integer.")
    
    ## Determining the angular momentum quantum number.
    l = ang_mom_nums(n)

    ## Generating the 'R_nl' values.
    r, prob_amps = radial_func(Z, n, l)
    
    ## Plotting the probability amplitudes.
    plotting(n, r, prob_amps)

## Main Call.
if __name__ == '__main__':
    main()

# INSTRUMENT DOCS

Here you can define the instrument you want to use.

You can define it overriding the "timbre" method.


# TIMBRE CRAFTER DOCS

*truncate*
    This function is used to truncate a decimal number the decimals you want

*class CsvCrafter*

    This class is to load a dataset as a timbre you want to define for the instrument you want to build. For example, you load some (x,y) points, and then you can build the timbre using a Polinomial Regression or a Bezier Curve.

    This class is intended to be abstract, because you can create the algorithm you want to use to define the custom timbre of your instrument.

    generate()
        This method specifies how the curve should be calculated

    use(x,trunc_decimal)
        This method is overriden by the subclasses that represents the function you want to use to define the timbre.

    set_csv_directory(dir):
        This sets the directory you want to load the csv files for the subclasses.

    load_csv(name, columns_names=False)
        This loads the (x,y) points you want to use to define the timbre function

    save_csv(name)
        This save the data you created into a csv file in the csv directory specified in the method set_csv_directory

    
import numpy as np
from pandas import Series
import logging
        
def check_5median_outlier(value: float, time_series: Series, log_file: str = None) -> int:
    """
    Determines the median of the time series and then whether the value is 
    an outlier by checking the value for outliers in 5 medians
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
    
    try:
        median = np.median(time_series)
        median_5 = 5 * median
        if abs(value - median) <= median_5:
            return 0
        else:
            return 1
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")

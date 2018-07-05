Statistic Computation (stats.py)
================================

.. automodule:: remote.client.stats
  :members:

  .. automethod:: remote.client.stats.names_to_data(df, computed_data)
  
  Associate values in *computed_data* Series with the names from *df* Dataframe. Paired based on indices.

  :param df: Pandas Dataframe containg parsed csv with data.
  :param compute_data: Series with computed data, such as those coming out of statistic functions.
  :returns: Pandas Dataframe with names and values of the computed data.

Statistic Computation (stats.py)
================================

.. automodule:: remote.client.stats
  :members:

  .. automethod:: remote.client.stats.names_to_data(df, computed_data)

  Associate values in *computed_data* Series with the names from *df* Dataframe. Paired based on the indices.

  :param df: Pandas Dataframe containing parsed csv with the data.
  :param compute_data: Series with computed data, such as those coming out of the statistic functions.
  :returns: Pandas Dataframe with the names and values of the computed data.

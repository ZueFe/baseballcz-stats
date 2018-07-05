Worker.py
=========

.. automodule:: remote.client.worker
  :members:

  .. automethod:: remote.server.worker.work_data():
    Schedules job, downloads all data from the page and stores them locally,
    then sends all downloaded data to remote FTP.
    Scheduled to run every day at midnight.
    Uses *BlockingScheduler* class from *APScheduler* library.

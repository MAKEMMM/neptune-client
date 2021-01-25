#
# Copyright (c) 2020, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import TYPE_CHECKING, Optional

from neptune.alpha.attributes.constants import MONITORING_STDOUT_ATTRIBUTE_PATH, MONITORING_STDERR_ATTRIBUTE_PATH
from neptune.alpha.internal.background_job import BackgroundJob
from neptune.alpha.internal.streams.std_stream_capture_logger import StdoutCaptureLogger, StderrCaptureLogger

if TYPE_CHECKING:
    from neptune.alpha.experiment import Experiment


class StdoutCaptureBackgroundJob(BackgroundJob):

    def __init__(self, attribute_name: str = MONITORING_STDOUT_ATTRIBUTE_PATH):
        self._attribute_name = attribute_name
        self._logger = None

    def start(self, experiment: 'Experiment'):
        self._logger = StdoutCaptureLogger(experiment, self._attribute_name)

    def stop(self):
        self._logger.close()

    def join(self, seconds: Optional[float] = None):
        pass


class StderrCaptureBackgroundJob(BackgroundJob):

    def __init__(self, attribute_name: str = MONITORING_STDERR_ATTRIBUTE_PATH):
        self._attribute_name = attribute_name
        self._logger = None

    def start(self, experiment: 'Experiment'):
        self._logger = StderrCaptureLogger(experiment, self._attribute_name)

    def stop(self):
        self._logger.close()

    def join(self, seconds: Optional[float] = None):
        pass

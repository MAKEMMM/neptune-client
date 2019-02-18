#
# Copyright (c) 2019, Neptune Labs Sp. z o.o.
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
import io
import os

import six
from PIL import Image


def get_image_content(image):
    if isinstance(image, six.string_types):
        if not os.path.exists(image):
            raise ValueError("File {} doesn't exist".format(image))
        with open(image, 'r') as image_file:
            return image_file.read()

    elif isinstance(image, Image.Image):
        with io.BytesIO() as image_buffer:
            image.save(image_buffer, format='PNG')
            return image_buffer.getvalue()

    raise ValueError("Unsupported image value")

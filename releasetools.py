# Copyright (C) 2012 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import struct

def FullOTA_PostValidate(info):
  # run e2fsck
  info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/platform/dw_mmc.0/by-name/system");');
  # resize2fs: run and delete
  info.script.AppendExtra('run_program("/sbin/resize2fs", "/dev/block/platform/dw_mmc.0/by-name/system");');
  # run e2fsck
  info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/platform/dw_mmc.0/by-name/system");');


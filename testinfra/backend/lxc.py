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

from typing import Any

from testinfra.backend import base


class LxcBackend(base.BaseBackend):
    NAME = "lxc"

    def __init__(self, name: str, *args: Any, **kwargs: Any):
        self.name = name
        super().__init__(self.name, *args, **kwargs)

    def run(self, command: str, *args: str, **kwargs: Any) -> base.CommandResult:
        cmd = self.get_command(command, *args)
        out = self.run_local(
            "lxc exec %s --mode=non-interactive -- /bin/sh -c %s", self.name, cmd
        )
        out.command = self.encode(cmd)
        return out

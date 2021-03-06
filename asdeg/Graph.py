# A* and Dijkstra Example Generator (ASDEG)
# Copyright (C) 2018 EduMake Limited and Stephen Parry
#
# This file is part of ASDEG (the A* and Dikstra Example Generator)
#
# ASDEG is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ASDEG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ASDEG.  If not, see <https://www.gnu.org/licenses/>.

from asdeg.Node import *


class Graph:
    def __init__(self):
        self._nodes = []
        self._origin_id = None
        self._destination_id = None

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    @property
    def origin_node(self) -> Node:
        return None if self._origin_id is None else self._nodes[self._origin_id]

    @property
    def origin_id(self) -> int:
        return self._origin_id

    @origin_id.setter
    def origin_id(self, new_origin_id : int) :
        self._origin_id = new_origin_id

    @property
    def destination_node(self) -> Node:
        return None if self._destination_id is None else self._nodes[self._destination_id]

    @property
    def destination_id(self) -> Node:
        return self._destination_id

    @destination_id.setter
    def destination_id(self, new_destination_id : int) :
        self._destination_id = new_destination_id


# Copyright 1999-2020 Alibaba Group Holding Ltd.
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

from ... import opcodes
from ...serialization.serializables import FieldTypes, StringField, ListField
from .base import Operand
from .core import TileableOperandMixin


class Fetch(Operand):
    _op_type_ = opcodes.FETCH

    to_fetch_key = StringField('to_fetch_key', default=None)


class FetchMixin(TileableOperandMixin):
    def check_inputs(self, inputs):
        # no inputs
        if inputs and len(inputs) > 0:
            raise ValueError(f"{type(self).__name__} has no inputs")

    @classmethod
    def tile(cls, op):
        raise NotImplementedError('Fetch tile cannot be handled by operand itself')

    @classmethod
    def execute(cls, ctx, op):
        """
        Fetch operand needs nothing to do.
        """


class FetchShuffle(Operand):
    _op_type_ = opcodes.FETCH_SHUFFLE

    to_fetch_keys = ListField('to_fetch_keys', FieldTypes.string)
    to_fetch_idxes = ListField('to_fetch_idxes', FieldTypes.tuple(FieldTypes.uint64))

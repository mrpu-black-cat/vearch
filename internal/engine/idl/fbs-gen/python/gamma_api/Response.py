# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gamma_api

import flatbuffers

class Response(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Response()
        x.Init(buf, n + offset)
        return x

    # Response
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Response
    def Results(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .SearchResult import SearchResult
            obj = SearchResult()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Response
    def ResultsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ResponseStart(builder): builder.StartObject(1)
def ResponseAddResults(builder, results): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(results), 0)
def ResponseStartResultsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ResponseEnd(builder): return builder.EndObject()

# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1l1l1ll_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll11111_opy_:
    bstack1ll1ll111ll_opy_ = bstack11l11ll_opy_ (u"ࠣࡤࡨࡲࡨ࡮࡭ࡢࡴ࡮ࠦል")
    context: bstack1lll1l1l1ll_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1l1l1ll_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll11111_opy_.bstack1ll1ll111ll_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩሎ"), bstack11l11ll_opy_ (u"ࠪ࠴ࠬሏ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll111l1_opy_(self, target: object):
        return bstack1ll1ll11111_opy_.create_context(target) == self.context
    def bstack1ll1llll111_opy_(self, context: bstack1lll1l1l1ll_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack11111l1lll_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll11111_opy_.bstack1ll1ll111ll_opy_][key] += value
    def bstack1ll1ll1111l_opy_(self) -> dict:
        return self.data[bstack1ll1ll11111_opy_.bstack1ll1ll111ll_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1l1l1ll_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
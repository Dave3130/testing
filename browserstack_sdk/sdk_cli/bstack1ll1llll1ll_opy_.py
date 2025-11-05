# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1llllll_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1l1lllll_opy_:
    bstack1ll1ll111l1_opy_ = bstack11111_opy_ (u"ࠧࡨࡥ࡯ࡥ࡫ࡱࡦࡸ࡫ࠣሑ")
    context: bstack1lll1llllll_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1llllll_opy_):
        self.context = context
        self.data = dict({bstack1ll1l1lllll_opy_.bstack1ll1ll111l1_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ሒ"), bstack11111_opy_ (u"ࠧ࠱ࠩሓ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll1111l_opy_(self, target: object):
        return bstack1ll1l1lllll_opy_.create_context(target) == self.context
    def bstack1ll1llll11l_opy_(self, context: bstack1lll1llllll_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1llll1l111_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1l1lllll_opy_.bstack1ll1ll111l1_opy_][key] += value
    def bstack1ll1ll11111_opy_(self) -> dict:
        return self.data[bstack1ll1l1lllll_opy_.bstack1ll1ll111l1_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1llllll_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1l1111l_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll111ll_opy_:
    bstack1ll1ll111l1_opy_ = bstack11l1l11_opy_ (u"ࠥࡦࡪࡴࡣࡩ࡯ࡤࡶࡰࠨᇺ")
    context: bstack1lll1l1111l_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1l1111l_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll111ll_opy_.bstack1ll1ll111l1_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᇻ"), bstack11l1l11_opy_ (u"ࠬ࠶ࠧᇼ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll11l11_opy_(self, target: object):
        return bstack1ll1ll111ll_opy_.create_context(target) == self.context
    def bstack1ll1lll1ll1_opy_(self, context: bstack1lll1l1111l_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack111lllllll_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll111ll_opy_.bstack1ll1ll111l1_opy_][key] += value
    def bstack1ll1ll11l1l_opy_(self) -> dict:
        return self.data[bstack1ll1ll111ll_opy_.bstack1ll1ll111l1_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1l1111l_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
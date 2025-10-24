# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1llll111111_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll11ll1_opy_:
    bstack1ll1ll1l11l_opy_ = bstack1l1_opy_ (u"ࠥࡦࡪࡴࡣࡩ࡯ࡤࡶࡰࠨᇳ")
    context: bstack1llll111111_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1llll111111_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll11ll1_opy_.bstack1ll1ll1l11l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᇴ"), bstack1l1_opy_ (u"ࠬ࠶ࠧᇵ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll1l111_opy_(self, target: object):
        return bstack1ll1ll11ll1_opy_.create_context(target) == self.context
    def bstack1lll111111l_opy_(self, context: bstack1llll111111_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack111l1l11l1_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll11ll1_opy_.bstack1ll1ll1l11l_opy_][key] += value
    def bstack1ll1ll11lll_opy_(self) -> dict:
        return self.data[bstack1ll1ll11ll1_opy_.bstack1ll1ll1l11l_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1llll111111_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1l111l1_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll11l1l_opy_:
    bstack1ll1ll11ll1_opy_ = bstack11ll_opy_ (u"ࠦࡧ࡫࡮ࡤࡪࡰࡥࡷࡱࠢሂ")
    context: bstack1lll1l111l1_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1l111l1_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll11l1l_opy_.bstack1ll1ll11ll1_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬሃ"), bstack11ll_opy_ (u"࠭࠰ࠨሄ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll11l11_opy_(self, target: object):
        return bstack1ll1ll11l1l_opy_.create_context(target) == self.context
    def bstack1ll1llll1l1_opy_(self, context: bstack1lll1l111l1_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1llllll11l_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll11l1l_opy_.bstack1ll1ll11ll1_opy_][key] += value
    def bstack1ll1ll111ll_opy_(self) -> dict:
        return self.data[bstack1ll1ll11l1l_opy_.bstack1ll1ll11ll1_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1l111l1_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1ll1l1l_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll11ll1_opy_:
    bstack1ll1ll11l11_opy_ = bstack1lllll1l_opy_ (u"ࠢࡣࡧࡱࡧ࡭ࡳࡡࡳ࡭ࠥᇾ")
    context: bstack1lll1ll1l1l_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1ll1l1l_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll11ll1_opy_.bstack1ll1ll11l11_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᇿ"), bstack1lllll1l_opy_ (u"ࠩ࠳ࠫሀ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll11l1l_opy_(self, target: object):
        return bstack1ll1ll11ll1_opy_.create_context(target) == self.context
    def bstack1ll1llll11l_opy_(self, context: bstack1lll1ll1l1l_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1lll11llll_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll11ll1_opy_.bstack1ll1ll11l11_opy_][key] += value
    def bstack1ll1ll11lll_opy_(self) -> dict:
        return self.data[bstack1ll1ll11ll1_opy_.bstack1ll1ll11l11_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1ll1l1l_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
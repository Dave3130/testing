# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1lll1llll11_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1ll1ll1ll11_opy_:
    bstack1ll1ll1ll1l_opy_ = bstack11111_opy_ (u"ࠢࡣࡧࡱࡧ࡭ࡳࡡࡳ࡭ࠥᇍ")
    context: bstack1lll1llll11_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1llll11_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll1ll11_opy_.bstack1ll1ll1ll1l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᇎ"), bstack11111_opy_ (u"ࠩ࠳ࠫᇏ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll1lll1_opy_(self, target: object):
        return bstack1ll1ll1ll11_opy_.create_context(target) == self.context
    def bstack1lll1111lll_opy_(self, context: bstack1lll1llll11_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1l1l111l1_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll1ll11_opy_.bstack1ll1ll1ll1l_opy_][key] += value
    def bstack1ll1ll1llll_opy_(self) -> dict:
        return self.data[bstack1ll1ll1ll11_opy_.bstack1ll1ll1ll1l_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1lll1llll11_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )
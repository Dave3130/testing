# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
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
class bstack1ll1ll1lll1_opy_:
    bstack1ll1ll1ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠧࡨࡥ࡯ࡥ࡫ࡱࡦࡸ࡫ࠣᇙ")
    context: bstack1lll1l111l1_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1l111l1_opy_):
        self.context = context
        self.data = dict({bstack1ll1ll1lll1_opy_.bstack1ll1ll1ll1l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᇚ"), bstack1l1lll1_opy_ (u"ࠧ࠱ࠩᇛ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll1llll_opy_(self, target: object):
        return bstack1ll1ll1lll1_opy_.create_context(target) == self.context
    def bstack1lll1111111_opy_(self, context: bstack1lll1l111l1_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1111l11111_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1ll1lll1_opy_.bstack1ll1ll1ll1l_opy_][key] += value
    def bstack1ll1ll1ll11_opy_(self) -> dict:
        return self.data[bstack1ll1ll1lll1_opy_.bstack1ll1ll1ll1l_opy_]
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
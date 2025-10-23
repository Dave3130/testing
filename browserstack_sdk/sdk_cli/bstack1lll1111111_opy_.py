# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
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
class bstack1ll1lll1111_opy_:
    bstack1ll1lll111l_opy_ = bstack111111l_opy_ (u"ࠨࡢࡦࡰࡦ࡬ࡲࡧࡲ࡬ࠤᇓ")
    context: bstack1lll1l1111l_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1lll1l1111l_opy_):
        self.context = context
        self.data = dict({bstack1ll1lll1111_opy_.bstack1ll1lll111l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᇔ"), bstack111111l_opy_ (u"ࠨ࠲ࠪᇕ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1ll1ll1llll_opy_(self, target: object):
        return bstack1ll1lll1111_opy_.create_context(target) == self.context
    def bstack1lll1111lll_opy_(self, context: bstack1lll1l1111l_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack11l1l1lll_opy_(self, key: str, value: timedelta):
        self.data[bstack1ll1lll1111_opy_.bstack1ll1lll111l_opy_][key] += value
    def bstack1ll1ll1lll1_opy_(self) -> dict:
        return self.data[bstack1ll1lll1111_opy_.bstack1ll1lll111l_opy_]
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
# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack111lll11l1_opy_:
    def __init__(self):
        self._111ll1lll11_opy_ = deque()
        self._111ll1ll111_opy_ = {}
        self._111ll1l11l1_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1l1l11_opy_(self, test_name, bstack111ll1l111l_opy_):
        with self._lock:
            bstack111ll1l11ll_opy_ = self._111ll1ll111_opy_.get(test_name, {})
            return bstack111ll1l11ll_opy_.get(bstack111ll1l111l_opy_, 0)
    def bstack111ll1l1lll_opy_(self, test_name, bstack111ll1l111l_opy_):
        with self._lock:
            bstack111ll1l1l1l_opy_ = self.bstack111ll1l1l11_opy_(test_name, bstack111ll1l111l_opy_)
            self.bstack111ll1ll11l_opy_(test_name, bstack111ll1l111l_opy_)
            return bstack111ll1l1l1l_opy_
    def bstack111ll1ll11l_opy_(self, test_name, bstack111ll1l111l_opy_):
        with self._lock:
            if test_name not in self._111ll1ll111_opy_:
                self._111ll1ll111_opy_[test_name] = {}
            bstack111ll1l11ll_opy_ = self._111ll1ll111_opy_[test_name]
            bstack111ll1l1l1l_opy_ = bstack111ll1l11ll_opy_.get(bstack111ll1l111l_opy_, 0)
            bstack111ll1l11ll_opy_[bstack111ll1l111l_opy_] = bstack111ll1l1l1l_opy_ + 1
    def bstack1ll1l1l11l_opy_(self, bstack111ll1l1ll1_opy_, bstack111ll1ll1ll_opy_):
        bstack111ll1lll1l_opy_ = self.bstack111ll1l1lll_opy_(bstack111ll1l1ll1_opy_, bstack111ll1ll1ll_opy_)
        event_name = bstack11l11lll1ll_opy_[bstack111ll1ll1ll_opy_]
        bstack1l111111111_opy_ = bstack1lllll1_opy_ (u"ࠦࢀࢃ࠭ࡼࡿ࠰ࡿࢂࠨᯅ").format(bstack111ll1l1ll1_opy_, event_name, bstack111ll1lll1l_opy_)
        with self._lock:
            self._111ll1lll11_opy_.append(bstack1l111111111_opy_)
    def bstack111l11111_opy_(self):
        with self._lock:
            return len(self._111ll1lll11_opy_) == 0
    def bstack1111l1111l_opy_(self):
        with self._lock:
            if self._111ll1lll11_opy_:
                bstack111ll1ll1l1_opy_ = self._111ll1lll11_opy_.popleft()
                return bstack111ll1ll1l1_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1l11l1_opy_
    def bstack1lll11l1ll_opy_(self):
        with self._lock:
            self._111ll1l11l1_opy_ = True
    def bstack1ll11ll11_opy_(self):
        with self._lock:
            self._111ll1l11l1_opy_ = False
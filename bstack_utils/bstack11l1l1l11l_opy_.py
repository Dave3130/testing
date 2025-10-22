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
import threading
from collections import deque
from bstack_utils.constants import *
class bstack11l1l11l1l_opy_:
    def __init__(self):
        self._111ll1l1111_opy_ = deque()
        self._111ll11l111_opy_ = {}
        self._111ll11ll1l_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll111ll1_opy_(self, test_name, bstack111ll11l1ll_opy_):
        with self._lock:
            bstack111ll11l11l_opy_ = self._111ll11l111_opy_.get(test_name, {})
            return bstack111ll11l11l_opy_.get(bstack111ll11l1ll_opy_, 0)
    def bstack111ll11ll11_opy_(self, test_name, bstack111ll11l1ll_opy_):
        with self._lock:
            bstack111ll11l1l1_opy_ = self.bstack111ll111ll1_opy_(test_name, bstack111ll11l1ll_opy_)
            self.bstack111ll111l11_opy_(test_name, bstack111ll11l1ll_opy_)
            return bstack111ll11l1l1_opy_
    def bstack111ll111l11_opy_(self, test_name, bstack111ll11l1ll_opy_):
        with self._lock:
            if test_name not in self._111ll11l111_opy_:
                self._111ll11l111_opy_[test_name] = {}
            bstack111ll11l11l_opy_ = self._111ll11l111_opy_[test_name]
            bstack111ll11l1l1_opy_ = bstack111ll11l11l_opy_.get(bstack111ll11l1ll_opy_, 0)
            bstack111ll11l11l_opy_[bstack111ll11l1ll_opy_] = bstack111ll11l1l1_opy_ + 1
    def bstack11ll1l111l_opy_(self, bstack111ll11llll_opy_, bstack111ll11lll1_opy_):
        bstack111ll111lll_opy_ = self.bstack111ll11ll11_opy_(bstack111ll11llll_opy_, bstack111ll11lll1_opy_)
        event_name = bstack11l11l1lll1_opy_[bstack111ll11lll1_opy_]
        bstack11llll1lll1_opy_ = bstack11l1l11_opy_ (u"ࠦࢀࢃ࠭ࡼࡿ࠰ࡿࢂࠨᯡ").format(bstack111ll11llll_opy_, event_name, bstack111ll111lll_opy_)
        with self._lock:
            self._111ll1l1111_opy_.append(bstack11llll1lll1_opy_)
    def bstack1ll111lll_opy_(self):
        with self._lock:
            return len(self._111ll1l1111_opy_) == 0
    def bstack1lllll1ll1_opy_(self):
        with self._lock:
            if self._111ll1l1111_opy_:
                bstack111ll111l1l_opy_ = self._111ll1l1111_opy_.popleft()
                return bstack111ll111l1l_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll11ll1l_opy_
    def bstack1llll11ll1_opy_(self):
        with self._lock:
            self._111ll11ll1l_opy_ = True
    def bstack111ll1l1l_opy_(self):
        with self._lock:
            self._111ll11ll1l_opy_ = False
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
import threading
from collections import deque
from bstack_utils.constants import *
class bstack11l1l1111_opy_:
    def __init__(self):
        self._111ll1ll1ll_opy_ = deque()
        self._111ll1l1l1l_opy_ = {}
        self._111ll1ll1l1_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1ll111_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            bstack111ll11llll_opy_ = self._111ll1l1l1l_opy_.get(test_name, {})
            return bstack111ll11llll_opy_.get(bstack111ll1l1111_opy_, 0)
    def bstack111ll1l1lll_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            bstack111ll1ll11l_opy_ = self.bstack111ll1ll111_opy_(test_name, bstack111ll1l1111_opy_)
            self.bstack111ll1l1l11_opy_(test_name, bstack111ll1l1111_opy_)
            return bstack111ll1ll11l_opy_
    def bstack111ll1l1l11_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            if test_name not in self._111ll1l1l1l_opy_:
                self._111ll1l1l1l_opy_[test_name] = {}
            bstack111ll11llll_opy_ = self._111ll1l1l1l_opy_[test_name]
            bstack111ll1ll11l_opy_ = bstack111ll11llll_opy_.get(bstack111ll1l1111_opy_, 0)
            bstack111ll11llll_opy_[bstack111ll1l1111_opy_] = bstack111ll1ll11l_opy_ + 1
    def bstack1l1llll1l1_opy_(self, bstack111ll1l1ll1_opy_, bstack111ll1l11ll_opy_):
        bstack111ll1l111l_opy_ = self.bstack111ll1l1lll_opy_(bstack111ll1l1ll1_opy_, bstack111ll1l11ll_opy_)
        event_name = bstack11l1l11111l_opy_[bstack111ll1l11ll_opy_]
        bstack11lllllllll_opy_ = bstack111111l_opy_ (u"ࠢࡼࡿ࠰ࡿࢂ࠳ࡻࡾࠤᮺ").format(bstack111ll1l1ll1_opy_, event_name, bstack111ll1l111l_opy_)
        with self._lock:
            self._111ll1ll1ll_opy_.append(bstack11lllllllll_opy_)
    def bstack1111ll1l1l_opy_(self):
        with self._lock:
            return len(self._111ll1ll1ll_opy_) == 0
    def bstack1lllll1l11_opy_(self):
        with self._lock:
            if self._111ll1ll1ll_opy_:
                bstack111ll1l11l1_opy_ = self._111ll1ll1ll_opy_.popleft()
                return bstack111ll1l11l1_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1ll1l1_opy_
    def bstack1l1lllllll_opy_(self):
        with self._lock:
            self._111ll1ll1l1_opy_ = True
    def bstack1111lll111_opy_(self):
        with self._lock:
            self._111ll1ll1l1_opy_ = False
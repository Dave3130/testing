# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack111l1111l1_opy_:
    def __init__(self):
        self._111l1lllll1_opy_ = deque()
        self._111ll111l11_opy_ = {}
        self._111ll111111_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1111ll_opy_(self, test_name, bstack111ll11l111_opy_):
        with self._lock:
            bstack111l1llllll_opy_ = self._111ll111l11_opy_.get(test_name, {})
            return bstack111l1llllll_opy_.get(bstack111ll11l111_opy_, 0)
    def bstack111ll11111l_opy_(self, test_name, bstack111ll11l111_opy_):
        with self._lock:
            bstack111l1llll11_opy_ = self.bstack111ll1111ll_opy_(test_name, bstack111ll11l111_opy_)
            self.bstack111ll1111l1_opy_(test_name, bstack111ll11l111_opy_)
            return bstack111l1llll11_opy_
    def bstack111ll1111l1_opy_(self, test_name, bstack111ll11l111_opy_):
        with self._lock:
            if test_name not in self._111ll111l11_opy_:
                self._111ll111l11_opy_[test_name] = {}
            bstack111l1llllll_opy_ = self._111ll111l11_opy_[test_name]
            bstack111l1llll11_opy_ = bstack111l1llllll_opy_.get(bstack111ll11l111_opy_, 0)
            bstack111l1llllll_opy_[bstack111ll11l111_opy_] = bstack111l1llll11_opy_ + 1
    def bstack11l1ll1lll_opy_(self, bstack111ll111lll_opy_, bstack111ll111l1l_opy_):
        bstack111ll111ll1_opy_ = self.bstack111ll11111l_opy_(bstack111ll111lll_opy_, bstack111ll111l1l_opy_)
        event_name = bstack11l11l11lll_opy_[bstack111ll111l1l_opy_]
        bstack11llll1ll11_opy_ = bstack11111_opy_ (u"ࠢࡼࡿ࠰ࡿࢂ࠳ࡻࡾࠤᰕ").format(bstack111ll111lll_opy_, event_name, bstack111ll111ll1_opy_)
        with self._lock:
            self._111l1lllll1_opy_.append(bstack11llll1ll11_opy_)
    def bstack1ll111llll_opy_(self):
        with self._lock:
            return len(self._111l1lllll1_opy_) == 0
    def bstack11l1l1l1l_opy_(self):
        with self._lock:
            if self._111l1lllll1_opy_:
                bstack111l1llll1l_opy_ = self._111l1lllll1_opy_.popleft()
                return bstack111l1llll1l_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll111111_opy_
    def bstack1111llll1l_opy_(self):
        with self._lock:
            self._111ll111111_opy_ = True
    def bstack11l1llll1l_opy_(self):
        with self._lock:
            self._111ll111111_opy_ = False
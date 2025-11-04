# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack1llllll11l_opy_:
    def __init__(self):
        self._111l1lllll1_opy_ = deque()
        self._111l1lll1ll_opy_ = {}
        self._111ll111111_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1111ll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111ll111l11_opy_ = self._111l1lll1ll_opy_.get(test_name, {})
            return bstack111ll111l11_opy_.get(bstack111ll111l1l_opy_, 0)
    def bstack111l1llllll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111l1llll1l_opy_ = self.bstack111ll1111ll_opy_(test_name, bstack111ll111l1l_opy_)
            self.bstack111ll111lll_opy_(test_name, bstack111ll111l1l_opy_)
            return bstack111l1llll1l_opy_
    def bstack111ll111lll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            if test_name not in self._111l1lll1ll_opy_:
                self._111l1lll1ll_opy_[test_name] = {}
            bstack111ll111l11_opy_ = self._111l1lll1ll_opy_[test_name]
            bstack111l1llll1l_opy_ = bstack111ll111l11_opy_.get(bstack111ll111l1l_opy_, 0)
            bstack111ll111l11_opy_[bstack111ll111l1l_opy_] = bstack111l1llll1l_opy_ + 1
    def bstack11l1llll11_opy_(self, bstack111ll11111l_opy_, bstack111l1llll11_opy_):
        bstack111ll111ll1_opy_ = self.bstack111l1llllll_opy_(bstack111ll11111l_opy_, bstack111l1llll11_opy_)
        event_name = bstack11l1l111ll1_opy_[bstack111l1llll11_opy_]
        bstack11llll1lll1_opy_ = bstack11l1111_opy_ (u"ࠨࡻࡾ࠯ࡾࢁ࠲ࢁࡽࠣᰔ").format(bstack111ll11111l_opy_, event_name, bstack111ll111ll1_opy_)
        with self._lock:
            self._111l1lllll1_opy_.append(bstack11llll1lll1_opy_)
    def bstack1ll1ll1lll_opy_(self):
        with self._lock:
            return len(self._111l1lllll1_opy_) == 0
    def bstack1l1l111l1_opy_(self):
        with self._lock:
            if self._111l1lllll1_opy_:
                bstack111ll1111l1_opy_ = self._111l1lllll1_opy_.popleft()
                return bstack111ll1111l1_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll111111_opy_
    def bstack111l11llll_opy_(self):
        with self._lock:
            self._111ll111111_opy_ = True
    def bstack11l11l1l1l_opy_(self):
        with self._lock:
            self._111ll111111_opy_ = False
# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack1l1l111l11_opy_:
    def __init__(self):
        self._111ll111lll_opy_ = deque()
        self._111ll11111l_opy_ = {}
        self._111ll1111l1_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1111ll_opy_(self, test_name, bstack111ll111l11_opy_):
        with self._lock:
            bstack111ll111l1l_opy_ = self._111ll11111l_opy_.get(test_name, {})
            return bstack111ll111l1l_opy_.get(bstack111ll111l11_opy_, 0)
    def bstack111l1llll1l_opy_(self, test_name, bstack111ll111l11_opy_):
        with self._lock:
            bstack111ll111111_opy_ = self.bstack111ll1111ll_opy_(test_name, bstack111ll111l11_opy_)
            self.bstack111ll11l111_opy_(test_name, bstack111ll111l11_opy_)
            return bstack111ll111111_opy_
    def bstack111ll11l111_opy_(self, test_name, bstack111ll111l11_opy_):
        with self._lock:
            if test_name not in self._111ll11111l_opy_:
                self._111ll11111l_opy_[test_name] = {}
            bstack111ll111l1l_opy_ = self._111ll11111l_opy_[test_name]
            bstack111ll111111_opy_ = bstack111ll111l1l_opy_.get(bstack111ll111l11_opy_, 0)
            bstack111ll111l1l_opy_[bstack111ll111l11_opy_] = bstack111ll111111_opy_ + 1
    def bstack111l11ll1_opy_(self, bstack111l1llllll_opy_, bstack111l1lllll1_opy_):
        bstack111ll111ll1_opy_ = self.bstack111l1llll1l_opy_(bstack111l1llllll_opy_, bstack111l1lllll1_opy_)
        event_name = bstack11l11ll1l1l_opy_[bstack111l1lllll1_opy_]
        bstack11llll11l1l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡽࢀ࠱ࢀࢃ࠭ࡼࡿࠥᰖ").format(bstack111l1llllll_opy_, event_name, bstack111ll111ll1_opy_)
        with self._lock:
            self._111ll111lll_opy_.append(bstack11llll11l1l_opy_)
    def bstack1ll1l1l1l1_opy_(self):
        with self._lock:
            return len(self._111ll111lll_opy_) == 0
    def bstack11l11l1l1_opy_(self):
        with self._lock:
            if self._111ll111lll_opy_:
                bstack111l1llll11_opy_ = self._111ll111lll_opy_.popleft()
                return bstack111l1llll11_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1111l1_opy_
    def bstack11111ll11l_opy_(self):
        with self._lock:
            self._111ll1111l1_opy_ = True
    def bstack1ll11ll11_opy_(self):
        with self._lock:
            self._111ll1111l1_opy_ = False
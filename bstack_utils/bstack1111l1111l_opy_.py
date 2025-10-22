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
import threading
from collections import deque
from bstack_utils.constants import *
class bstack1111ll1lll_opy_:
    def __init__(self):
        self._111ll11ll1l_opy_ = deque()
        self._111ll11ll11_opy_ = {}
        self._111ll11llll_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1l111l_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            bstack111ll11l111_opy_ = self._111ll11ll11_opy_.get(test_name, {})
            return bstack111ll11l111_opy_.get(bstack111ll1l1111_opy_, 0)
    def bstack111ll11l11l_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            bstack111ll11lll1_opy_ = self.bstack111ll1l111l_opy_(test_name, bstack111ll1l1111_opy_)
            self.bstack111ll111lll_opy_(test_name, bstack111ll1l1111_opy_)
            return bstack111ll11lll1_opy_
    def bstack111ll111lll_opy_(self, test_name, bstack111ll1l1111_opy_):
        with self._lock:
            if test_name not in self._111ll11ll11_opy_:
                self._111ll11ll11_opy_[test_name] = {}
            bstack111ll11l111_opy_ = self._111ll11ll11_opy_[test_name]
            bstack111ll11lll1_opy_ = bstack111ll11l111_opy_.get(bstack111ll1l1111_opy_, 0)
            bstack111ll11l111_opy_[bstack111ll1l1111_opy_] = bstack111ll11lll1_opy_ + 1
    def bstack1ll11l1l1_opy_(self, bstack111ll11l1l1_opy_, bstack111ll11l1ll_opy_):
        bstack111ll1l11l1_opy_ = self.bstack111ll11l11l_opy_(bstack111ll11l1l1_opy_, bstack111ll11l1ll_opy_)
        event_name = bstack11l1l11l1l1_opy_[bstack111ll11l1ll_opy_]
        bstack11llll1llll_opy_ = bstack1lllll1l_opy_ (u"ࠣࡽࢀ࠱ࢀࢃ࠭ࡼࡿࠥᯥ").format(bstack111ll11l1l1_opy_, event_name, bstack111ll1l11l1_opy_)
        with self._lock:
            self._111ll11ll1l_opy_.append(bstack11llll1llll_opy_)
    def bstack111l111ll1_opy_(self):
        with self._lock:
            return len(self._111ll11ll1l_opy_) == 0
    def bstack111ll111l1_opy_(self):
        with self._lock:
            if self._111ll11ll1l_opy_:
                bstack111ll111ll1_opy_ = self._111ll11ll1l_opy_.popleft()
                return bstack111ll111ll1_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll11llll_opy_
    def bstack1l1l1ll111_opy_(self):
        with self._lock:
            self._111ll11llll_opy_ = True
    def bstack1ll1l1l111_opy_(self):
        with self._lock:
            self._111ll11llll_opy_ = False
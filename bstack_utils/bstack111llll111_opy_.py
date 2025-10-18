# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack1ll1ll1l11_opy_:
    def __init__(self):
        self._111ll11l111_opy_ = deque()
        self._111ll11lll1_opy_ = {}
        self._111ll11l1l1_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll111lll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111ll111ll1_opy_ = self._111ll11lll1_opy_.get(test_name, {})
            return bstack111ll111ll1_opy_.get(bstack111ll111l1l_opy_, 0)
    def bstack111ll11ll1l_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111ll1l111l_opy_ = self.bstack111ll111lll_opy_(test_name, bstack111ll111l1l_opy_)
            self.bstack111ll11llll_opy_(test_name, bstack111ll111l1l_opy_)
            return bstack111ll1l111l_opy_
    def bstack111ll11llll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            if test_name not in self._111ll11lll1_opy_:
                self._111ll11lll1_opy_[test_name] = {}
            bstack111ll111ll1_opy_ = self._111ll11lll1_opy_[test_name]
            bstack111ll1l111l_opy_ = bstack111ll111ll1_opy_.get(bstack111ll111l1l_opy_, 0)
            bstack111ll111ll1_opy_[bstack111ll111l1l_opy_] = bstack111ll1l111l_opy_ + 1
    def bstack11l1ll1l1_opy_(self, bstack111ll11ll11_opy_, bstack111ll11l11l_opy_):
        bstack111ll11l1ll_opy_ = self.bstack111ll11ll1l_opy_(bstack111ll11ll11_opy_, bstack111ll11l11l_opy_)
        event_name = bstack11l11ll1111_opy_[bstack111ll11l11l_opy_]
        bstack11llll1ll1l_opy_ = bstack11ll_opy_ (u"ࠧࢁࡽ࠮ࡽࢀ࠱ࢀࢃࠢᯩ").format(bstack111ll11ll11_opy_, event_name, bstack111ll11l1ll_opy_)
        with self._lock:
            self._111ll11l111_opy_.append(bstack11llll1ll1l_opy_)
    def bstack11ll11111_opy_(self):
        with self._lock:
            return len(self._111ll11l111_opy_) == 0
    def bstack111ll11l1l_opy_(self):
        with self._lock:
            if self._111ll11l111_opy_:
                bstack111ll1l1111_opy_ = self._111ll11l111_opy_.popleft()
                return bstack111ll1l1111_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll11l1l1_opy_
    def bstack1llll1ll1l_opy_(self):
        with self._lock:
            self._111ll11l1l1_opy_ = True
    def bstack1l1ll1lll_opy_(self):
        with self._lock:
            self._111ll11l1l1_opy_ = False
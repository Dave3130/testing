# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack11ll1l1111_opy_:
    def __init__(self):
        self._111ll11ll11_opy_ = deque()
        self._111ll11lll1_opy_ = {}
        self._111ll1l1111_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll11l111_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111ll111lll_opy_ = self._111ll11lll1_opy_.get(test_name, {})
            return bstack111ll111lll_opy_.get(bstack111ll111l1l_opy_, 0)
    def bstack111ll111l11_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            bstack111ll11l11l_opy_ = self.bstack111ll11l111_opy_(test_name, bstack111ll111l1l_opy_)
            self.bstack111ll11llll_opy_(test_name, bstack111ll111l1l_opy_)
            return bstack111ll11l11l_opy_
    def bstack111ll11llll_opy_(self, test_name, bstack111ll111l1l_opy_):
        with self._lock:
            if test_name not in self._111ll11lll1_opy_:
                self._111ll11lll1_opy_[test_name] = {}
            bstack111ll111lll_opy_ = self._111ll11lll1_opy_[test_name]
            bstack111ll11l11l_opy_ = bstack111ll111lll_opy_.get(bstack111ll111l1l_opy_, 0)
            bstack111ll111lll_opy_[bstack111ll111l1l_opy_] = bstack111ll11l11l_opy_ + 1
    def bstack11llll1l11_opy_(self, bstack111ll111ll1_opy_, bstack111ll11ll1l_opy_):
        bstack111ll11l1l1_opy_ = self.bstack111ll111l11_opy_(bstack111ll111ll1_opy_, bstack111ll11ll1l_opy_)
        event_name = bstack11l11l1l1ll_opy_[bstack111ll11ll1l_opy_]
        bstack11lllll11l1_opy_ = bstack1l111ll_opy_ (u"ࠧࢁࡽ࠮ࡽࢀ࠱ࢀࢃࠢᯢ").format(bstack111ll111ll1_opy_, event_name, bstack111ll11l1l1_opy_)
        with self._lock:
            self._111ll11ll11_opy_.append(bstack11lllll11l1_opy_)
    def bstack111l111l11_opy_(self):
        with self._lock:
            return len(self._111ll11ll11_opy_) == 0
    def bstack1l1l11lll1_opy_(self):
        with self._lock:
            if self._111ll11ll11_opy_:
                bstack111ll11l1ll_opy_ = self._111ll11ll11_opy_.popleft()
                return bstack111ll11l1ll_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1l1111_opy_
    def bstack11llll1ll_opy_(self):
        with self._lock:
            self._111ll1l1111_opy_ = True
    def bstack11ll1lllll_opy_(self):
        with self._lock:
            self._111ll1l1111_opy_ = False
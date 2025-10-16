# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack1l1ll1llll_opy_:
    def __init__(self):
        self._111ll1l1l1l_opy_ = deque()
        self._111ll1l11ll_opy_ = {}
        self._111ll1ll11l_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1l111l_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            bstack111ll1lll11_opy_ = self._111ll1l11ll_opy_.get(test_name, {})
            return bstack111ll1lll11_opy_.get(bstack111ll1ll1l1_opy_, 0)
    def bstack111ll1ll111_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            bstack111ll1l1l11_opy_ = self.bstack111ll1l111l_opy_(test_name, bstack111ll1ll1l1_opy_)
            self.bstack111ll1l1lll_opy_(test_name, bstack111ll1ll1l1_opy_)
            return bstack111ll1l1l11_opy_
    def bstack111ll1l1lll_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            if test_name not in self._111ll1l11ll_opy_:
                self._111ll1l11ll_opy_[test_name] = {}
            bstack111ll1lll11_opy_ = self._111ll1l11ll_opy_[test_name]
            bstack111ll1l1l11_opy_ = bstack111ll1lll11_opy_.get(bstack111ll1ll1l1_opy_, 0)
            bstack111ll1lll11_opy_[bstack111ll1ll1l1_opy_] = bstack111ll1l1l11_opy_ + 1
    def bstack111lll1l1_opy_(self, bstack111ll1ll1ll_opy_, bstack111ll1lll1l_opy_):
        bstack111ll1l11l1_opy_ = self.bstack111ll1ll111_opy_(bstack111ll1ll1ll_opy_, bstack111ll1lll1l_opy_)
        event_name = bstack11l11ll1ll1_opy_[bstack111ll1lll1l_opy_]
        bstack11llllll1l1_opy_ = bstack1ll11_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧᯄ").format(bstack111ll1ll1ll_opy_, event_name, bstack111ll1l11l1_opy_)
        with self._lock:
            self._111ll1l1l1l_opy_.append(bstack11llllll1l1_opy_)
    def bstack1ll1111l1l_opy_(self):
        with self._lock:
            return len(self._111ll1l1l1l_opy_) == 0
    def bstack11ll1l11l_opy_(self):
        with self._lock:
            if self._111ll1l1l1l_opy_:
                bstack111ll1l1ll1_opy_ = self._111ll1l1l1l_opy_.popleft()
                return bstack111ll1l1ll1_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1ll11l_opy_
    def bstack11l1l1ll11_opy_(self):
        with self._lock:
            self._111ll1ll11l_opy_ = True
    def bstack1ll1ll1ll_opy_(self):
        with self._lock:
            self._111ll1ll11l_opy_ = False
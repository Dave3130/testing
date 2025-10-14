# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import threading
from collections import deque
from bstack_utils.constants import *
class bstack11ll1l111_opy_:
    def __init__(self):
        self._111ll1l111l_opy_ = deque()
        self._111ll1l1ll1_opy_ = {}
        self._111ll1l1lll_opy_ = False
        self._lock = threading.RLock()
    def bstack111ll1l1l11_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            bstack111ll1l11l1_opy_ = self._111ll1l1ll1_opy_.get(test_name, {})
            return bstack111ll1l11l1_opy_.get(bstack111ll1ll1l1_opy_, 0)
    def bstack111ll1ll11l_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            bstack111ll1ll1ll_opy_ = self.bstack111ll1l1l11_opy_(test_name, bstack111ll1ll1l1_opy_)
            self.bstack111ll1ll111_opy_(test_name, bstack111ll1ll1l1_opy_)
            return bstack111ll1ll1ll_opy_
    def bstack111ll1ll111_opy_(self, test_name, bstack111ll1ll1l1_opy_):
        with self._lock:
            if test_name not in self._111ll1l1ll1_opy_:
                self._111ll1l1ll1_opy_[test_name] = {}
            bstack111ll1l11l1_opy_ = self._111ll1l1ll1_opy_[test_name]
            bstack111ll1ll1ll_opy_ = bstack111ll1l11l1_opy_.get(bstack111ll1ll1l1_opy_, 0)
            bstack111ll1l11l1_opy_[bstack111ll1ll1l1_opy_] = bstack111ll1ll1ll_opy_ + 1
    def bstack11ll1lll1_opy_(self, bstack111ll11llll_opy_, bstack111ll1l1111_opy_):
        bstack111ll1l1l1l_opy_ = self.bstack111ll1ll11l_opy_(bstack111ll11llll_opy_, bstack111ll1l1111_opy_)
        event_name = bstack11l1l111l11_opy_[bstack111ll1l1111_opy_]
        bstack11lllllll1l_opy_ = bstack11l1l11_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧᮽ").format(bstack111ll11llll_opy_, event_name, bstack111ll1l1l1l_opy_)
        with self._lock:
            self._111ll1l111l_opy_.append(bstack11lllllll1l_opy_)
    def bstack11lllll11l_opy_(self):
        with self._lock:
            return len(self._111ll1l111l_opy_) == 0
    def bstack1ll1llll1l_opy_(self):
        with self._lock:
            if self._111ll1l111l_opy_:
                bstack111ll1l11ll_opy_ = self._111ll1l111l_opy_.popleft()
                return bstack111ll1l11ll_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111ll1l1lll_opy_
    def bstack1l1llllll_opy_(self):
        with self._lock:
            self._111ll1l1lll_opy_ = True
    def bstack1ll11lllll_opy_(self):
        with self._lock:
            self._111ll1l1lll_opy_ = False